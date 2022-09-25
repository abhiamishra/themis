from datetime import datetime

from bs4 import BeautifulSoup
import requests

from opinion import OpinionBuilder, insert_opinion
from textsummary import download_pdf, extract_pdf, summarize, update_category, just_choice
from db import opinions_col
from utils.date import unix_time
import time

def crawl_year(year: int):
    r = requests.get(f"https://www.supremecourt.gov/opinions/slipopinion/{year}")
    soup = BeautifulSoup(r.text, 'html.parser')
    #cells = ["cell6", "cell5", "cell4", "cell3", "cell1", "cell12", "cell11", "cell10"]
    cells = ["cell6"]
    i=0
    for cell in cells:  
        table = soup.find(id=cell).div.table
        for tr in table.find_all("tr"):
            #print(i)

            tds = tr.find_all("td")

            if len(tds) == 0:
                continue

            # parse the info from the html page
            url = tds[3].a["href"]
            date = tds[1].string
            docket = tds[2].string
            title = tds[3].string
            url = f"https://www.supremecourt.gov/{url}"

            print(url)

            downloaded_file = download_pdf(url)
            text = extract_pdf(downloaded_file)
            results = summarize(text)

            #print(len(results))
            # 0 -> long summary
            # 1 -> historical summary
            # 2 -> short line summary
            # 3 -> category
            # 4 -> dictionary of what justices voted for who/what


            tokens = date.split("/")
            date = datetime(int(tokens[2]) + 2000, int(tokens[0]), int(tokens[1]))

            # insert the document into db
            o = {
                "year": date.year,
                "time": unix_time(date),
                "date": date.strftime("%m/%d/%Y"),
                "link": url, "title": title,
                "docket": docket,
                "longsum": text[0],
                "history": text[1],
                "shortsum": text[2],
                "category": update_category(docket),
                "justices": just_choice(date)
            }

            opinions_col.insert_one(o)

            print(i)
            i=i+1

            time.sleep(4)


def crawl():
    for i in range(13, 14):
        crawl_year(i)


crawl()
