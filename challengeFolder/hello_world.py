from executer import *
import random

def start_challenge(target_file):
    p = process(target_file)
    ret = readline(p)
    if ret == "Hello World":
        return 1
    else:
        return 0