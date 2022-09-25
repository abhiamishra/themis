from pydoc import doc
import sys
sys.path.append('C:/UTD/Senior Year/Fall Semester 2022/themis')  

from db import opinions_col

documents = opinions_col.find({})
for document in documents:
    #print(document["docket"])
    #print(document["category"])
    #print(document["date"])
    print(document["justices"])
