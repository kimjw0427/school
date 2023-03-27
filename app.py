from flask import *
import time, random

app = Flask(__name__)

tmp_path = "/tmp/"

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/send", methods=['GET','POST'])
def send():
    if request.method == 'GET':
        return render_template("/send.html")
    else:
        lang = request.form.get("lang")
        code = request.form.get("code")
        codeFilename = tmp_path + str(time.time()) + str(random.randint(10**10,10**11))
        if lang == "Python":
            codeFilename = codeFilename + ".py"
            f = open(codeFilename,"w+")
            f.write(code)
            
        return render_template("/send.html")

if __name__=="__main__":
    app.run(debug=True)