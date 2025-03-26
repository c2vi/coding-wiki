#Coding-Wiki - insert - Sebastian Moser

version = {
	"python":		1.2,
	"unixshell":	1.2
}

import time


from pymongo import MongoClient

Mongo_URL = "mongodb://Test:Test@coding-wiki-shard-00-00-c4i9i.gcp.mongodb.net:27017,coding-wiki-shard-00-01-c4i9i.gcp.mongodb.net:27017,coding-wiki-shard-00-02-c4i9i.gcp.mongodb.net:27017/Things?ssl=true&replicaSet=Coding-Wiki-shard-0&authSource=admin&retryWrites=true&w=majority"

cluster = MongoClient(Mongo_URL)

Coding_Wiki_DB = cluster["Coding_Wiki"]


Python_Collection = Coding_Wiki_DB["Python"]
Unix_Sehll_Collection = Coding_Wiki_DB["Unix Shell"]
Swift_Collection = Coding_Wiki_DB["Swift"]
Arduino_Collection = Coding_Wiki_DB["Arduino"]
HTML_Collection = Coding_Wiki_DB["HTML"]
CSS_Collection = Coding_Wiki_DB["CSS"]
Java_Script_Collection = Coding_Wiki_DB["Java Script"]


def add_array(array_name):
	array_name += ": "
	array = ["nothing"]
	counter_add_array = 0
	while array[counter_add_array] != "":
		array.append(input(array_name))
		counter_add_array += 1
	array.pop(0)
	array.pop(-1)
	return array;


def insert_python():
	name = input("name:")
	code = input("code:")
	code_advanced = input("code_advanced:")
	kurz_beschreibung = input("Beschreibung:")
	modul = input("modul:")
	art = input("art:")
	arten = ["keyword","funktion","operator","zeichen","tags"]
	while art not in arten:
			art = input("invalid art:")

	def add_links():
		dokument_links = {
			"videolink":add_array("videolink"),
			"artikellink":add_array("artikellink")
		}
		return dokument_links;
	
	
	dokument = {
		"name":	name	,
		"code":	code	,
		"code_advanced":code_advanced,
		"art":	art	,
		"ort":	["python",modul,name],
		"beschreibung":kurz_beschreibung,
		"tags":add_array("tags"),
		"links":add_links(),
		"erstelldatum":time_of_insertion,
		"suchtags":add_array("suchtags"),
		"version":version["python"]
	}

	edit = "nothing"
	counter_edit = 0
	while edit != "":
		edit = input("edit:")
		for python_property in dokument:
			if python_property == edit :
				if type(dokument[python_property]) is list:
					dokument[python_property] = add_array(python_property)
				elif python_property == "links":
					dokument[python_property] = add_links()
				else:
					dokument[python_property] = input("ersetzen mit:")

		counter_edit += 1


	Python_Collection.insert_one(dokument)


def insert_unixshell():
	programm_name = input("name: ")
	code = input("code: ")
	kurz_beschreibung = input("Beschreibung: ")
	art = input("art:")
	arten = ["argument","programm","sonderzeichen","beispiel"]
	while art not in arten:
			art = input("invalid   art:")
	argumente = add_array("argumente")

	def add_links():
		dokument_links = {
			"videolink":add_array("videolink"),
			"artikellink":add_array("artikellink")
		}
		return dokument_links;
	
	
	dokument = {
		"name":	programm_name	,
		"code":	programm_name+ str(argumente)	,
		"art":	art	,
		"ort":	["shell",programm_name],
		"beschreibung":kurz_beschreibung,
		"tags":add_array("tags"),
		"links":add_links(),
		"erstelldatum":time_of_insertion,
		"suchtags":add_array("suchtags"),
		"version":version["unixshell"]
	}

	edit = "nothing"
	counter_edit = 0
	while edit != "":
		edit = input("edit:")
		for python_property in dokument:
			if python_property == edit :
				if type(dokument[python_property]) is list:
					dokument[python_property] = add_array(python_property)
				elif python_property == "links":
					dokument[python_property] = add_links()
				else:
					dokument[python_property] = input("ersetzen mit:")

		counter_edit += 1


	Unix_Sehll_Collection.insert_one(dokument)


def insert_swift():
	name = input("name:")
	code = input("code:")
	code_advanced = input("code_advanced:")
	kurz_beschreibung = input("Beschreibung:")
	# modul = input("modul:")
	art = input("art:")
	arten = ["keyword","funktion","operator","zeichen","tags"]
	while art not in arten:
			art = input("invalid art:")

	def add_links():
		dokument_links = {
			"videolink":add_array("videolink"),
			"artikellink":add_array("artikellink")
		}
		return dokument_links;
	
	
	dokument = {
		"name":	name	,
		"code":	code	,
		"code_advanced":code_advanced,
		"art":	art	,
		"ort":	["Swift",name],
		"beschreibung":kurz_beschreibung,
		"tags":add_array("tags"),
		"links":add_links(),
		"erstelldatum":time_of_insertion,
		"suchtags":add_array("suchtags"),
		"version":version["swift"]
	}

	edit = "nothing"
	counter_edit = 0
	while edit != "":
		edit = input("edit:")
		for python_property in dokument:
			if python_property == edit :
				if type(dokument[python_property]) is list:
					dokument[python_property] = add_array(python_property)
				elif python_property == "links":
					dokument[python_property] = add_links()
				else:
					dokument[python_property] = input("ersetzen mit:")

		counter_edit += 1


	Swift_Collection.insert_one(dokument)





time = time.gmtime(time.time()+7200)

time_of_insertion = {
	"year":		time.tm_year,
	"month":	time.tm_mon,
	"day":		time.tm_mday,
	"hour":		time.tm_hour,
	"minute":	time.tm_min,
	}


