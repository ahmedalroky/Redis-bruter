from colorama import init
from colorama import Fore, Back, Style
import socket
init()
open_port=[]
host = "192.168.1.18"
ports = range(64290,64300)
def scan(host,port):
    p_=[]
    p_.append(port)
    try :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        try : 
            con=s.connect((host,port))
            data=s.recv(1024)
            #print(data.decode("utf-8"))
            if data.strip() ==b"":
                print(Fore.YELLOW +f"[-] T-Pot Detected On Port {port} [-]")
            else :
                print(Fore.GREEN +f"[+] Open Port : {port} [+]"+Style.RESET_ALL)
                p_.append(data.decode("utf-8"))
                open_port.append(p_)
        except Exception as e:
            if  "WinError 10061" in str(e):
                print(Fore.RED +f"[-] Closed Port {port} [-]"+Style.RESET_ALL)
            else :
                print(Fore.GREEN +f"[+] Open Port {port} [+]"+Style.RESET_ALL)
                open_port.append(p_)
            #print(str(e))
    except Exception as e:
        if  "WinError 10061" in str(e):
            print(Fore.RED +f"[-] Closed Port {port} [-]"+Style.RESET_ALL)
        open_port.append(p_)
for port in ports:
    scan(host,port)
print(Fore.CYAN + "[*] Scan Finished [*]"+Style.RESET_ALL)
for res in open_port:
    if len(res)==2:
        print(Fore.BLUE +f"[+] Port: {str(res[0]).strip()}|Banner : {res[1].strip()} [+]"+Style.RESET_ALL)
    else :
        print(Fore.BLUE +f"[+] Port: {res[0]} [+]"+Style.RESET_ALL)
