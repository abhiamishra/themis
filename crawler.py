from datetime import datetime

from bs4 import BeautifulSoup
import requests

from db import opinions_col
from utils.date import unix_time


def crawl_year(year: int):
    r = requests.get(f"https://www.supremecourt.gov/opinions/slipopinion/{year}")
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find(id="cell6").div.table
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")

        if len(tds) == 0:
            continue

        # parse the info from the html page
        url = tds[3].a["href"]
        date = tds[1].string
        docket = tds[2].string
        title = tds[3].string
        url = f"https://www.supremecourt.gov/{url}"

        tokens = date.split("/")
        date = datetime(int(tokens[2]) + 2000, int(tokens[0]), int(tokens[1]))

        # insert the document into db
        o = {
            "year": date.year,
            "time": unix_time(date),
            "date": date.strftime("%m/%d/%Y"),
            "link": url, "title": title,
            "docket": docket,
            "summary": "Summary",
            "history": "History",
            "category": "Category",
            "justices": []
        }
        o["justices"].append({"name": "Ruth Bader Ginsburg", "opinion": "no"})

        opinions_col.insert_one(o)


def crawl():
    for i in range(13, 22):
        crawl_year(i)


crawl()
