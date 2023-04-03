import subprocess

def process(target_file):
    p = subprocess.Popen(target_file, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    return p

def sendline(p, string_bytes):
    p.stdin.write(string_bytes + b"\n")
    p.stdin.flush()

def readline(p):
    rs = p.stdout.readline().decode("utf-8").strip()
    return rs