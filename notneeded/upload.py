from flask import *

TEMPLATE_DIR = "C:/xampp/htdocs"
webServer = Flask(__name__ ,template_folder = TEMPLATE_DIR)
#Basic authentication HTML


@webServer.route("/upload.html" ,methods = ["GET" ,"POST"])
def uploadServer():
    if(request.method == "POST"):
        file = request.files["file"]
        file.save("C:/xampp/htdocs/" + file.filename)        
        return "test"

    else:
        return render_template("/upload.html")

@webServer.run(host = "127.0.0.1" ,port = 9090 ,debug = True)

def test():
    pass
