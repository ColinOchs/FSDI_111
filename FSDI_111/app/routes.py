from flask import Flask               #from flask module import Flask class


app = Flask(__name__)                  #create an instance of "Flask" in app 
                                        #the "app" variable is also considered an "object"

@app.get("/")                          #Flask decorator that allows us to map "/" to "index"         
def index():                           #Python function - in Flask this is a "view function"
    me = {                                #Python dictionary containing key-value pairs.                  
        "first_name": "Colin",
        "last_name": "Ochs",
        "hobbies": "Crushin' it like a BOSS",
        "active": True
    }

    return me                                               # return statement. Flask converts dict to JSON.