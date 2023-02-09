from flask import *

TEMPLATE_DIR = "C:/xampp/htdocs"

webServer = Flask(__name__ ,template_folder = TEMPLATE_DIR)

@webServer.route('/<path:path>',methods = ['GET','POST'])

def indexPage(path):
    return render_template(path)
    
webServer.run(host="127.0.0.1", port = 8000, debug = True)