from flask import *
from challenge import chall_list
import time, random, os
from challengeFolder import add

app = Flask(__name__)

tmp_path = "/tmp/"

@app.route("/")
def index():
    return render_template("/index.html")

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
        if lang == "Python":
            codeFilename = codeFilename + ".py"
            f = open(codeFilename,"w+")
            f.write(code)
            print(f"[+] create : {codeFilename}")
            try:
                command = chall_list[chall_num]["chall_name"]+".start_challenge" + f"([\"python3\",{codeFilename}])"
                print(f"[+] TRY {command}")
                ret = eval(command)
                if ret:
                    print("성공")
                else:
                    print("실패")
            except:
                print("[+] ERROR")            

            os.system("rm " + codeFilename)
            print(f"[+] delete : {codeFilename}")
        else:
            return "프로그래밍 언어를 선택해주세요."
            
        return render_template("/send.html")

if __name__=="__main__":
    app.run(debug=True)