import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import opinions_col
from utils.jsonify import jsonify

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/filter")
def get_filter(category: str, year: int, justice: str):
    cond = []

    if year > 0:
        cond.append({"year": year})

    if category != "All":
        cond.append({"category": category})

    if justice != "All":
        cond.append({"justices.name": justice})

    if len(cond) > 0:
        query = {"$and": cond}
    else:
        query = {}

    cursor = opinions_col.find(query).sort("time", -1)

    opinions = []
    for element in cursor:
        opinions.append(element)
    return jsonify(opinions)


@app.get("/plot")
def get_plot(justice: str, category: str):
    cond = []

    if justice != "All":
        cond.append({"justices.name": justice})

    if category != "All":
        cond.append({"category": category})

    if len(cond) > 0:
        query = {"$and": cond}
    else:
        query = {}

    cursor = opinions_col.find(query).sort("time", 1)

    # types of scotus opinions: majority, dissenting, concurring, unanimous
    data = {}
    for element in cursor:
        # search for the justices opinion
        opinions = []
        for j in element["justices"]:
            if j["name"] == justice or justice == "All":
                opinions.append(j["opinion"])
        year = element["year"]
        if year not in data:
            data[year] = {}
        for opinion in opinions:
            if opinion not in data[year]:
                data[year][opinion] = 1
            else:
                data[year][opinion] += 1

    plot = []
    for d in data:
        print(d, data[d])
        plot.append({"year": d, **data[d]})
    return plot


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
