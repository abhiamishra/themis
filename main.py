import uvicorn as uvicorn
from fastapi import FastAPI

from db import opinions_col
from utils.jsonify import jsonify

app = FastAPI()


@app.get("/year/{year}")
def get_by_year(year: int):
    cursor = opinions_col.find({"year": year}).sort("time", -1)
    opinions = []
    for element in cursor:
        opinions.append(element)
    return jsonify(opinions)


@app.get("/justice/{justice}/{opinion}")
def get_by_justice(justice: str, opinion: str):
    if opinion != "all":
        query = {"$and": [{"justices.name": justice}, {"justices.opinion": opinion}]}
    else:
        query = {"justices.name": justice}
    cursor = opinions_col.find(query).sort("time", -1)

    opinions = []
    for element in cursor:
        opinions.append(element)
    return jsonify(opinions)


@app.get("/category/{category}/{year}")
def get_by_justice(category: str, year: int):
    if year != 0:
        query = {"$and": [{"category": category}, {"year": year}]}
    else:
        query = {"category": category}
    cursor = opinions_col.find(query).sort("time", -1)

    opinions = []
    for element in cursor:
        opinions.append(element)
    return jsonify(opinions)


if __name__ == "__main__":
    print(__package__)
    uvicorn.run(app, host="localhost", port=8000)
