# Redis Bruter
Simple Redis bruteforce script

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
