
from flask import Flask
from flask_mongoengine import MongoEngine

from webui_server import db

#Flaskforms imports
#from flask_wtf import FlaskForm
#from wtforms import StringField as wtf_StringField
#from wtforms.validators import DataRequired


class Item(db.Document):
	meta = {'allow_inheritance': True}
	
	one_line_text = db.StringField(max_length=500)
	email = db.EmailField(required=True, unique=True)
	first_name = db.StringField(max_length=50)
	last_name = db.StringField(max_length=50)






class Garbige(Item):
	type = "Garbige"
	


class List(Item):
	type = "List"
	


class Zitat(Item):
	type = "Zitat"
	



#---------------------------------------------------------------

type_switch = {
	"Garbige":Garbige,
	"List":List
}

