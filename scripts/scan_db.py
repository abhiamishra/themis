from db import opinions_col

cursor = opinions_col.find({}).sort("time", 1)
for document in cursor:
    print(document)
