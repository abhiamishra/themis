import datetime
from typing import Dict, Any

from db import opinions_col
from utils.date import unix_time


class OpinionBuilder:
    dict: Dict[str, Any] = {}

    def __init__(self):
        self.dict["justices"] = []

    def set_date(self, date: datetime):
        self.dict["year"] = date.year
        self.dict["time"] = unix_time(date)
        self.dict["date"] = date.strftime("%m/%d/%Y")

    def add_justice(self, name: str, opinion: str):
        self.dict["justices"].append({"name": name, "opinion": opinion})

<<<<<<< HEAD
    def __str__(self) -> str:
        print("---------- START ---------------")
        print(self.dict["shortsum"])
        
        print("---------- his ---------------")

        print(self.dict["history"])

        print("---------- ENDER ---------------")

        print(self.dict["longsum"])

        print("--------------------------------")

        return ""



def insert_opinion(opinion: OpinionBuilder):
    opinions_col.insert_one(opinion.dict)
=======

def insert_opinion(opinion: OpinionBuilder):
    opinions_col.insert_one(opinion.dict)


'''
example usage

o = OpinionBuilder()
o.set_date(datetime.datetime(2022, 6, 30))
o.add_justice("Ruth Bader Ginsburg", "majority")
o.dict["title"] = "Someone v. Someone else"
o.dict["docket"] = "22-998"
o.dict["summary"] = "Summary test"
o.dict["history"] = "Summary test"
o.dict["link"] = "https://www.supremecourt.gov/opinions/21pdf/21-954_7l48.pdf"
o.dict["category"] = "jobs"

insert_opinion(o)
'''
>>>>>>> 78173879f233eff5cd04f7fd7eb474213f849481
