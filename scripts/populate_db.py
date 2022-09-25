import datetime
import sys
sys.path.append('C:/UTD/Senior Year/Fall Semester 2022/themis')  
from utils.date import unix_time
from db import opinions_col


# types of scotus opinions: majority, dissenting, concurring, unanimous


def get_opinion():
    x = datetime.datetime(2022, 6, 30)
    opinion = {
        "year": x.year,
        "time": unix_time(x),
        "date": x.strftime("%m/%d/%Y"),
        "title": "Biden v. Texas",
        "docket": "21-954",
        "summary": "This one is about biden vs texas.",
        "history": "This happened because of politics in texas",
        "link": "https://www.supremecourt.gov/opinions/21pdf/21-954_7l48.pdf",
        "category": "healthcare",
        "justices": [
            {
                "name": "Amy Coney Barrett",
                "opinion": "majority"
            },
            {
                "name": "Ketanji Brown Jackson",
                "opinion": "dissenting"
            }
        ]
    }
    return opinion


def get_opinion1():
    x = datetime.datetime(2022, 5, 30)
    opinion = {
        "year": x.year,
        "time": unix_time(x),
        "date": x.strftime("%m/%d/%Y"),
        "title": "West Virginia v. EPA",
        "docket": "20-1530",
        "summary": "This one is about west virginia vs epa.",
        "history": "This happened because of the epa",
        "link": "https://www.supremecourt.gov/opinions/21pdf/20-1530_new_l537.pdf",
        "category": "industry",
        "justices": [
            {
                "name": "Amy Coney Barrett",
                "opinion": "majority"
            },
            {
                "name": "Ketanji Brown Jackson",
                "opinion": "concurring"
            },
            {
                "name": "John G. Roberts",
                "opinion": "concurring"
            }
        ]
    }
    return opinion


opinions_col.insert_one(get_opinion())
opinions_col.insert_one(get_opinion1())
