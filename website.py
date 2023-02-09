from flask import *
import json
from passlib.hash import pbkdf2_sha256
import copy

TEMPLATE_DIR = "C:/xampp/htdocs"

webServer = Flask(__name__ ,template_folder = TEMPLATE_DIR)

@webServer.route("/<path:path>",methods = ["GET"])

def renderPage(path):
    return render_template(path)

i = 0
#Create User
@webServer.route("/user/create.html" ,methods = ["GET" ,"POST"])
def userPage():
    if (request.method == "POST"):
        global i
        i = i + 1
        userPassword = request.form["password"]
        form = copy.copy(request.form)
        form = form.to_dict()

        hashedPass= hashPass(userPassword ,16)
        form["password"] = hashedPass

        file = json.loads(readJson())
        file[int(i)] = form
        writeJson(file ,"w")
        return redirect("/success.html")

    else:
        return render_template("/user/create.html")

#List Users
@webServer.route("/user/list.html" ,methods = ["GET"])
def userList():
    file = json.loads(readJson())
    return render_template("/user/list.html" ,file = file)


#Delete User
@webServer.route("/user/delete.html" ,methods = ["GET" ,"POST"])
def deleteUser():
    if(request.method == "POST"):
        username =  request.form["username"]
        #Changes to dict
        userFile = json.loads(readJson())

        #This loop finds if user exists if exists deletes
        for x in userFile:
            if(userFile[x]["username"] == username):
                userFile.pop(x)
                writeJson(userFile ,"w")
                return redirect("/success.html")

        #If user has beed founded i doesn't enters this return
        return "User not found"

    else:
        return render_template("/user/delete.html")



#Updates user
@webServer.route("/user/update.html" ,methods = ["GET" ,"POST"])
def updateUser():
    if(request.method == "POST"):
        username =  request.form["username"]
        #Changes to dict
        userFile = json.loads(readJson())

        #Finds and changes user from the form
        for x in userFile:
            if(userFile[x]["username"] == username):
                userPassword = request.form["password"]
                form = copy.copy(request.form)
                form = form.to_dict()
                hashedPass= hashPass(userPassword ,16)
                form["password"] = hashedPass
                userFile[x] = form
                writeJson(userFile ,"w")
                return redirect("/success.html")

        return "User not found"

    else:
        return render_template("/user/update.html")


@webServer.route("/login.html" ,methods = ["GET" ,"POST"])
def loginUser():
    if (request.method == "POST"):
        username =  request.form["username"]
        userFile = json.loads(readJson())
        form = copy.copy(request.form)
         
        for x in userFile:
            if(userFile[x]["username"] == username):
                if(validatePass(form["password"] ,userFile[x]["password"])):
                    return render_template("/logout.html" ,username = username)
                else:
                    return "You wrote password wrong"

        #If user has beed founded i doesn't enters this return
        return "User not found"

    else:
        return render_template("/login.html")



#Writes to json
def writeJson(text ,mode):
    file = open("users.json" ,mode)
    file.write(json.dumps(text))
    file.close()

#Reads the json data
def readJson():
    file = open("users.json" ,"r")
    data = file.read()
    file.close()
    return data

#This hashes the passsword
def hashPass(password ,saltSize):
    hashedPass = pbkdf2_sha256.using(salt_size=saltSize).hash(password)
    return hashedPass

#This validates the password with hash
def validatePass(password ,hashedPass):
    return pbkdf2_sha256.verify(password, hashedPass)

@webServer.run(host = "127.0.0.1" ,port = 80 ,debug = True)

def test():
    pass
