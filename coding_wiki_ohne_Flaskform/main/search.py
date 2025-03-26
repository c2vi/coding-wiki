

def simple_search(search_db,search_feld,search_begriff,return_feld):


	#MongoDB Connection
	from pymongo import MongoClient
	from main.main import Mongo_URL

	cluster = MongoClient(Mongo_URL)

	Coding_Wiki_DB = cluster["Coding_Wiki"]

	Python_Collection = Coding_Wiki_DB["Python"]
	Unix_Sehll_Collection = Coding_Wiki_DB["Unix Shell"]
	Swift_Collection = Coding_Wiki_DB["Swift"]
	Arduino_Collection = Coding_Wiki_DB["Arduino"]
	HTML_Collection = Coding_Wiki_DB["HTML"]
	CSS_Collection = Coding_Wiki_DB["CSS"]
	Java_Script_Collection = Coding_Wiki_DB["Java Script"]

	results = []

	if search_db == "python" or search_db == "py":
		for dokument in Python_Collection.find({search_feld:search_begriff}):
			results.append(dokument[return_feld])

	elif search_db == "swift" or search_db == "sw":
		for dokument in Swift_Collection.find({search_feld:search_begriff}):
			results.append(dokument[return_feld])


	elif search_db == "unixshell" or search_db == "unix" or search_db == "us":
		for dokument in Unix_Sehll_Collection.find({search_feld:search_begriff}):
			results.append(dokument[return_feld])


	else:
		return "Falsche Datenbank"
	
	return results