
from pymongo import MongoClient

from main.main import Mongo_URL
cluster = MongoClient(Mongo_URL)
Coding_Wiki_DB = cluster["Coding_Wiki"]
Collection = Coding_Wiki_DB["Python"]

for item in Collection.find({"art":"Keyword"}):
	print(item["name"])


	