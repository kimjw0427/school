from flask import *
from challenge import chall_list
import time, random, os
from challengeFolder import add, hello_world

app = Flask(__name__)

tmp_path = "/tmp/"

def fileDelete(codeFilename):
    for fileList in codeFilename:
        os.system("rm " + fileList)
    print(f"[+] delete : {codeFilename}")

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/test")
def test():
    a = 'add.start_challenge(["python3","/tmp/1681101509.687060841954444524.py"])'
    return str(eval(a))

@app.route("/challenge", methods=['GET'])
def challenge():
    chall_num = request.args.get("n")
    if chall_num in chall_list:
        return render_template("/challenge.html",chall=chall_list[chall_num])
    else:
        return "404"

@app.route("/send", methods=['GET','POST'])
def send():
    if request.method == 'GET':
        chall_num = request.args.get("n")
        return render_template("/send.html",chall_num=chall_num)
    else:
        lang = request.form.get("lang")
        code = request.form.get("code")
        chall_num = request.form.get("n")
        if not chall_num in chall_list:
            return "404"
        
        codeFilename = tmp_path + str(time.time()) + str(random.randint(10**10,10**11))
        result = 0
        if lang == "Python":
            codeFilename = codeFilename + ".py"
            f = open(codeFilename,"w+")
            f.write(code)
            f.close()
            print(f"[+] create : {codeFilename}")
            command = chall_list[chall_num]["chall_file"]+".start_challenge" + f"([\"python3\",\"{codeFilename}\"])"
            codeFilename = [codeFilename]
        if lang == "C":
            codeFilename_c = codeFilename + ".c"
            codeFilename_o = codeFilename + ".o"
            codeFilename = [codeFilename_c,codeFilename_o]
            f = open(codeFilename[0],"w+")
            f.write(code)
            f.close()
            print(f"[+] create : {codeFilename}")
            os.system("gcc " + codeFilename_c + " -o " + codeFilename_o)
            if not os.path.isfile(codeFilename_o):
                fileDelete(codeFilename)
                return render_template("/result_2.html", error="Compile Error")
            command = chall_list[chall_num]["chall_file"]+".start_challenge" + f"(\"{codeFilename[1]}\")"
        else:
            return "프로그래밍 언어를 선택해주세요."
        
        try:
            print(f"[+] TRY {command}")
            ret = eval(command)
            if ret:
                result = 1
            else:
                result = 0
        except Exception as e:
            fileDelete(codeFilename)
            print("[+] ERROR : " + str(e))
            return render_template("/result_2.html",error=str(e))
        
        fileDelete(codeFilename)
        if result:
            return render_template("/result_1.html")
        else:
            return render_template("/result_2.html", error="정답이 아닙니다.")

if __name__=="__main__":
    app.run(debug=True)