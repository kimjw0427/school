from executer import *
import random

def start_challenge(target_file):
    comp = 0
    for i in range(0,10):
        p = process(target_file)

        v1 = random.randint(0,10**10); v2 = random.randint(0,10**10)
        sendline(p,f"{v1} {v2}".encode())
        ret = readline(p)

        if int(ret) == (v1+v2):
            comp = comp + 1
        p.kill()
    
    if comp==10:
        return 1
    else:
        return 0
