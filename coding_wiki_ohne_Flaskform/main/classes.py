



class Item():
	meta = {'allow_inheritance': True}



	def input_from_commandline():
		pass


	def edit():
		pass


	def insert(self):

		from datetime import datetime
		time = datetime.today()

		self.time_of_insertion = {
		"year": time.year,
		"month": time.month,
		"day": time.day,
		"hour": time.hour,
		"minute": time.minute,
		"seccond": time.second
		}

		#MongoDB connection
		from pymongo import MongoClient
		from main.main import Mongo_URL
		cluster = MongoClient(Mongo_URL)
		Coding_Wiki_DB = cluster["Coding_Wiki"]
		Collection = Coding_Wiki_DB["items"]


		Collection.insert(self.__dict__)


#---------------------------------------------------------------



class Garbige(Item):
	type = "Garbige"
	render = [{"title":"Some text for testing purposes","render":"one_line_text"}
			]
	insert_fields = ["type" , "one_line_text"]
	one_line_text = StringField(render[0]["title"])

	test = StringField('testing', validators=[DataRequired()])
	test2 = StringField('test2', validators=[DataRequired()])

class List(Item):
	type = "List"
	render = [
				{"title":"What this list is about","render":"one_line_text"},
				{"title":"" , "render":"list_of_text"}
			]

	test = StringField('testing', validators=[DataRequired()])
	test2 = StringField('test2', validators=[DataRequired()])

class Zitat(Item):
	type = "Zitat"
	render = [
				{"title":1},
				#{},
				#{}
			]


