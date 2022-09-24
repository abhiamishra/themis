from db import opinions_col

documents = opinions_col.find({})
for document in documents:
    print(document)
