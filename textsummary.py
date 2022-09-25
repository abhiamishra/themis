from lib2to3.pgen2 import token
from lib2to3.pgen2.token import tok_name
from optparse import Option
from sre_constants import CATEGORY_WORD
import requests
from bs4 import BeautifulSoup
import pandas as pd
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
import datetime
import string
from db import opinions_col
from nltk import tokenize

url = "https://www.supremecourt.gov/opinions/21pdf/19-1392_6j37.pdf"

dateEndJustice = { "Jackson" : 0,
    "Barrett" :  0,
    "Kavanaugh" : 0,
    "Gorsuch":  0,
    "Kagan" :  0,
    "Sotomayor" :  0,
    "Alito": 0,
    "Roberts": 0,
    "Breyer": 2022,
    "Ginsburg": 2020,
    "Thomas": 0,
    "Souter":  2009,
    "Kennedy":  2018,
    "Rehnquist" : 2005,
    "Scalia": 2016,
    "Connor": 2006,
    "Stevens": 2010
}

dateStartJustice = { "Jackson" : 2022,
    "Barrett" :  2020,
    "Kavanaugh" : 2018,
    "Gorsuch":  2017,
    "Kagan" :  2010,
    "Sotomayor" : 2009,
    "Alito": 2006,
    "Roberts": 2005,
    "Breyer": 1994,
    "Ginsburg": 1993,
    "Thomas": 1991,
    "Souter":  1990,
    "Kennedy":  1988,
    "Rehnquist" : 1986,
    "Scalia": 1986,
    "Connor": 1981,
    "Stevens": 1975
}

calcJustice = { "Jackson" : 0,
    "Barrett" :  0,
    "Kavanaugh" : 0,
    "Gorsuch":  0,
    "Kagan" :  0,
    "Sotomayor" :  0,
    "Alito": 0,
    "Roberts": 0,
    "Breyer": 0,
    "Ginsburg": 0,
    "Thomas": 0,
    "Souter":  0,
    "Kennedy":  0,
    "Rehnquist" : 0,
    "Scalia": 0,    
    "Connor": 0,
    "Stevens": 0
}

nameJustice = { "Jackson" : "Jackson, Ketanji Brown",
    "Barrett" : "Barrett, Amy Coney",
    "Kavanaugh" : "Kavanaugh, Brett M.",
    "Gorsuch": "Gorsuch, Neil M.",
    "Kagan" : "Kagan, Elena",
    "Sotomayor" : "Sotomayor, Sonia",
    "Alito": "Samuel A., Jr., Alito",
    "Roberts" : "Roberts, John",
    "Breyer": "Breyer, Stephen G.",
    "Ginsburg": "Ruth Bader Ginsburg",
    "Thomas": "Thomas, Clarence",
    "Souter": "Souter, David H.",
    "Kennedy": "Kennedy, Anthony M.",
    "Rehnquist": "Rehnquist, William",
    "Scalia": "Scalia, Antonin",
    "Connor": "O'Connor, Day Sandra",
    "Stevens": "Stevens, Paul John"
}
  
a = datetime.datetime.now()
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
    text.append(extract_text) #big summary
    text.append(hist_text) #historical text

    i = 0
    j = 0
    short_sum = []
    for line in text[1].splitlines():
        #print(line)
        if "Held:" in line:
            short_sum = (text[1].splitlines()[i+1:i+20])
        i = i+1
    
    i=0
    for line in extract_text.splitlines():
        #print(line)
        if 'a unanimous court' in line.lower():
            j = i
            break
        elif 'delivered the opinion of the court' in line.lower():
            j = i
            break
        i = i+1

    op = extract_text.splitlines()[j:j+11]
    op = ''.join(op)
    op = op.replace('-','')
    print(op)
    lines = tokenize.sent_tokenize(op)
    #print(lines)
    for line in lines:
        #print(line)
        if "unanimous" in line:
            for justice in calcJustice:
                calcJustice[justice] += 1
        else:
            if "delivered the opinion of the Court" in line:
                #print("hi!")
                for justice in calcJustice:
                    if justice.lower() in line.lower():
                        calcJustice[justice] += 1
            if "concurring" in line:
                for justice in calcJustice:
                    if justice.lower() in line.lower() and calcJustice[justice] != 1:
                        calcJustice[justice] += 1
            if "dissenting" in line:
                for justice in calcJustice:
                    if justice.lower() in line.lower() and calcJustice[justice] != 1:
                        calcJustice[justice] -= 1
    
    #print(calcJustice)
    short_sum = ''.join(short_sum)
    text.append(short_sum)
    return text

#text = []
#text = extract_pdf(downloaded_file)
 #short summary 
#print(short_sum)

#PIPELINE TO SUMMARIZE
def summarize(text):
    i = 0
    nlp = spacy.load('en_core_web_sm')
    results = []
    for item in text:
        doc = nlp(item)

        keyword = []
        stopwords = list(STOP_WORDS)
        stopwords.append("§")
        stopwords.append("U.")
        stopwords.append("S.")
        stopwords.append("C.")
        stopwords.append("Court")
        stopwords.append("_")
        stopwords.append("-")
        stopwords.append("Syllabus")
        stopwords.append("v.")

        pos_tag = ['PROPN','ADJ','NOUN','VERB']
        for token in doc:
            if(token.text in stopwords or token.text in punctuation or token.text.isnumeric()):
                continue
            if(token.pos_ in pos_tag):
                keyword.append(token.text)
        freq_word = Counter(keyword)

        lists = Counter(keyword).most_common(1)
        if(len(lists)!=0):
            max_freq = Counter(keyword).most_common(1)[0][1]
        else:
            max_freq = 1

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

        num_sentences = 1
        if i==0:
            num_sentences = 3
        elif i==1:
            num_sentences = 2

        sum_string = nlargest(num_sentences, sent_strength, key=sent_strength.get)

        fin_sentence = [w.text for w in sum_string]
        sum = ' '.join(fin_sentence)
        sum = re.sub(r"\s{10,}", "", sum)
        results.append(sum)
        i = i + 1
    
    return results



catText = pd.read_csv("categories.csv", encoding='cp1252')
catText['docket'] = catText['docket'].astype(pd.StringDtype())

categories = {
    1: "Criminal Procedure",
    2: "Civil Rights",
    3: "First Amendment",
    4: "Due Process",
    5: "Privacy",
    6: "Attorneys",
    7: "Unions",
    8: "Economic Activity",
    9: "Judicial Power",
    10: "Federalism",
    11: "Interstate Relations",
    12: "Federal Taxation",
    13: "Miscellaneous",
    14: "Private Action"
}


#updating the category
def update_category(docket):
    res_df = catText[catText['docket'] == docket]
    if (len(res_df) != 0 ):
        category = res_df['issueArea'].iloc[0]
        return categories[category]
    else:
        return "Uncategorized"

#Giving list of justics and what they voted for
def just_choice(date):
    findyear = pd.to_datetime(date).year
    #print(findyear)
    justices = []
    for justice in calcJustice:
        if dateEndJustice[justice] != 0 and dateEndJustice[justice] > findyear and dateStartJustice[justice] < findyear:
            add = {"name": nameJustice[justice], "opinion": calcJustice[justice]}
            justices.append(add)
        elif dateEndJustice[justice] == 0 and dateStartJustice[justice] < findyear:
            add = {"name": nameJustice[justice], "opinion": calcJustice[justice]}
            justices.append(add)
    print(justices)
    for justice in calcJustice:
        calcJustice[justice] = 0
    return(justices)

#a = download_pdf("https://www.supremecourt.gov/opinions/13pdf/11-965_1qm2.pdf")
#f = extract_pdf(a)
#just_choice("04/28/2014")
#s = summarize(f)
#print(s)

#update_category("13-483")
#find_result = opinions_col.find_one(
#    { "docket": "17-459"}
#)
#print(find_result)