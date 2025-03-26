#Coding-Wiki - main - Sebastian Moser

Mongo_URL = "mongodb://Test:Test@coding-wiki-shard-00-00-c4i9i.gcp.mongodb.net:27017,coding-wiki-shard-00-01-c4i9i.gcp.mongodb.net:27017,coding-wiki-shard-00-02-c4i9i.gcp.mongodb.net:27017/Coding_Wiki?ssl=true&replicaSet=Coding-Wiki-shard-0&authSource=admin&retryWrites=true&w=majority"

structure = {

	"Garbige":[{"title":"Some text for testing purposes","render":"one_line_text"}],
	"List":[{"title":"What this list is about","render":"one_line_text"},{"render":"list_of_text"}]


}

def get_structure():

	#Mongo Connection
	from pymongo import MongoClient
	cluster = MongoClient(Mongo_URL)
	Coding_Wiki_DB = cluster["Coding_Wiki"]
	config_collection = Coding_Wiki_DB["config"]
	return config_collection.find_one({"myid":"structure"})["types"]

def get_types(structure):
	types =[]
	for category in structure:
		for type in list(structure[category].keys()):
			types.append(type)
	return types

def get_categories(structure):
	categories = list(structure.keys())
	return categories()



def main():
	pass



if __name__ == "__main__":
	main()



