import numpy as np
# import time
import requests
import sys
import json

rate = 5
last = 0

while True:
    # Polling TimesNewswire API for recent news in the past 24 hours
    r = requests.get("http://api.nytimes.com/svc/news/v3/content/nyt/all/1.json?api-key=2bf845abbb668b5d43da6f6387793f27:1:74611818")
    
    # Recording the timestamps of the API response received at an exponentially generated rate
    for m in r.json()["results"]:
        present = time.time()
        		
    time.sleep(np.random.exponential(rate))
	
    if last == 0 :
        last = present
        continue
    rate = present - last
    print "\n"
    print json.dumps({"Rate":rate})
	# Creating alerts associated to erratic behavior of the stream rate
	
	# Case 1 :- If the rate falls below 20% of the specified value
    if rate<1:
                print "\n"
                print "Woah, too fast!"
    
    # Case 2 :- If the rate grows 200% of the specified value	
    elif rate>10:
                print "\n"
                print "Too slow..."
    sys.stdout.flush()
    last = present		
