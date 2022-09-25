from pydoc import doc
import sys
sys.path.append('C:/UTD/Senior Year/Fall Semester 2022/themis')  

from db import opinions_col

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

documents = opinions_col.find({})
for document in documents:
    print(document["docket"])
    print(document["category"])
    print(document["date"])
    print(document["justices"])
