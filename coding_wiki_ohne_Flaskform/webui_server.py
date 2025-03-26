from flask import Flask, request, render_template, redirect
from flask_mongoengine import MongoEngine
from main.classes import *
from main.main import *




app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "host":Mongo_URL,
    "db":"Coding_Wiki"
    }

import os
#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

#db = MongoEngine()
#db.init_app(app)


#structure = get_structure()
#types =get_types(structure)
types = list(structure.keys())
#testitem = Item()

#Garbige(render = "Testing2").save()

#test = User.objects(name="laura").first()



#App Routes
#-----------------------------------------------------

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/db/coding_wiki" , methods=["POST" , "GET"])
def coding_wiki_db():
    return render_db("coding_wiki")


@app.route('/db/personal', methods=('GET', 'POST'))
def personal_db():
    return render_db("personal")

@app.route("/db/coding_wiki/insert" , methods=("GET" , "POST"))
def insert_coding_wiki():
    return render_insert_db("coding_wiki")

@app.route("/db/personal/insert" , methods=("GET" , "POST"))
def insert_personal_db():


    return render_insert_db("personal",request.method)




#---------------------------------------------------
    
def render_db(db_type):
   
    return render_template("database.html" ,
     include="none",
     types=structure.keys(),
     db_type=db_type
     )

def render_insert_db(db_type,method):
    type = "Garbige"

    if method == "POST":
        form.insert()
        return redirect("/db/personal")


    elif method == "GET":

        return render_template("database.html",
            include="{}_database_insert.html".format(db_type),
            types=structure.keys(),
            db_type=db_type,
            form=form
            )
    else:
        pass

#--------------------------------------------

if __name__ == "__main__":
    app.run(debug='True')


