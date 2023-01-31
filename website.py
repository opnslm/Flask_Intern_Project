from flask import *
import json
import copy

TEMPLATE_DIR = "C:/xampp/htdocs"

webServer = Flask(__name__ ,template_folder = TEMPLATE_DIR)

@webServer.route("/<path:path>",methods = ["GET","POST"])

def renderPage(path):
    return render_template(path)



#Create User
@webServer.route("/user/create.html" ,methods = ["GET" ,"POST"])
def userPage():
    if (request.method == "POST"):
        userFile = open("users.json" ,"a")

        User = dict(copy.copy(request.form))
        userPassword = User["password"]
        #hashPassword(userPassword)
        userFile.write(json.dumps(User))
        userFile.close

        return "Succeeded"


    else:
        return render_template("/user/create.html")



#List Users
@webServer.route("/user/list.html" ,methods = ["GET"])
def userList():
    userFileTemp = open("users.json" ,"r")
    userFile = userFileTemp.read()
    userFileTemp.close()

    return render_template("/user/list.html" ,userFile = userFile)


#Delete User
@webServer.route("/user/delete.html" ,methods = ["GET" ,"POST"])

def deleteUser():
    if(request.method == "POST"):
        username =  request.form["username"]
        userFileTemp = open("users.json" ,"r")
        userFile = userFileTemp.read()
        userFileTemp.close()


        isFound = False
        for i in range(0 ,len(userFile)):
            if (userFile[i:i + len(username)] == username):
                print("bulundu")
                isFound = True
                whereIs = i
                whereIsCopy = i
                break
        
        isTrue = False
        isTrueSecond = False
        if(isFound == True):
            while(True):
                if(isTrue == False):
                    whereIs = whereIs - 1

                if(isTrueSecond == False):
                    whereIsCopy = whereIsCopy + 1

                if((userFile[whereIs]) == "{"):
                    first = whereIs
                    isTrue = True

                if((userFile[whereIsCopy]) == "}"):
                    second = whereIsCopy
                    isTrueSecond = True

                if(isTrue and isTrueSecond):
                    break

            temp = whereIsCopy - whereIs
            tempString = ""
            tempWhereIs = copy.copy(whereIs)
            for i in range(0 ,temp + 1):
                tempString = tempString + userFile[whereIs]
                whereIs = whereIs + 1
            whereIs = copy.copy(tempWhereIs)



            userfile = userFile.replace(tempString ,"")
            userFileTemp = open("users.json" ,"w")
            userFileTemp.write(userfile)
            userFileTemp.close()



            return str(userfile)
            #Silinecek


        else:
            return "User not found"
    else:
        return render_template("/user/delete.html")







@webServer.run(host = "127.0.0.1" ,port = 80 ,debug = True)

def hashPassword(password):
    pass

