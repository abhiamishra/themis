import requests
from bs4 import BeautifulSoup
import io
import os
from PyPDF2 import PdfFileReader
from tika import parser
import fitz
import spacy
import en_core_web_sm
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
import re

url = "https://www.supremecourt.gov/opinions/21pdf/20-1530_new_l537.pdf"

#Get webpage from PDF link

#PIPELINE from URL to EXTRACT WORD
def download_pdf(url):
    response = requests.get(url)
    
    filename = "file1.pdf"

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)

    return filename

downloaded_file = download_pdf(url)



def extract_pdf(filename):
    with fitz.open(filename) as doc:
        extract_text = ""
        hist_text = ""
        i = 0
        for page in doc:
            extract_text += page.get_text()
            if (i<5):
                hist_text += page.get_text()
            i = i + 1
    os.remove(filename)
    text = []
    text.append(extract_text)
    text.append(hist_text)
    return text

text = []
text = extract_pdf(downloaded_file)

i = 0
short_sum = []
for line in text[1].splitlines():
    if "Held:" in line:
        short_sum = (text[1].splitlines()[i+1:i+20])
    i = i+1

short_sum = ''.join(short_sum)
#print(short_sum)

#PIPELINE TO SUMMARIZE
nlp = spacy.load('en_core_web_sm')
doc = nlp(short_sum)
print(len(list(doc.sents)))

keyword = []
stopwords = list(STOP_WORDS)
stopwords.append("§")
stopwords.append("U.")
stopwords.append("S.")
stopwords.append("C.")
stopwords.append("Court")
stopwords.append("-")


pos_tag = ['PROPN','ADJ','NOUN','VERB']
for token in doc:
    if(token.text in stopwords or token.text in punctuation):
        continue
    if(token.pos_ in pos_tag):
        keyword.append(token.text)

freq_word = Counter(keyword)

max_freq = Counter(keyword).most_common(1)[0][1]
for word in freq_word.keys():
    freq_word[word] = (freq_word[word]/max_freq)

sent_strength = {}
for sent in doc.sents:
    for word in sent:
        if word.text in freq_word.keys():
            if sent in sent_strength.keys():
                sent_strength[sent]+=freq_word[word.text]
            else:
                sent_strength[sent]=freq_word[word.text]

sum_string = nlargest(1, sent_strength, key=sent_strength.get)

fin_sentence = [w.text for w in sum_string]
sum = ' '.join(fin_sentence)
#sum = re.sub(r"\s{2,}", "", sum)

print(sum)