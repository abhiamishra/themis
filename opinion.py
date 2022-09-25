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
