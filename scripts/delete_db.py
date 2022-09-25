import sys
sys.path.append('C:/UTD/Senior Year/Fall Semester 2022/themis')

from db import opinions_col


documents = opinions_col.delete_many({})

