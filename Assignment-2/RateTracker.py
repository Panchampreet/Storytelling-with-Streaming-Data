# This program does the bulk of the work for the assignment. It fetches the output from the
# 'poll_API.py' program as 

from flask import Flask
import numpy as np
import time
import requests
import sys
import json
rateTracker = Flask(__name__)

@poll_API.route("/")
def main():
	return render_template('index.html')

        lastInstance = 0

        while True:
      	        line = sys.stdin.readline()
                save = json.loads(line)
	     
        if lastInstance == 0 :
                lastInstance = present
                continue
         
        rate = present - lastInstance
        print "\n"

        # Creating alerts associated to erratic behavior of the stream rate
	
        # Case 1 :- If the rate falls below 20% of the specified value
        if rate<1:
                message = "This rate of influx of articles is too fast!"
                d = {rate: message}    
	
        # Case 2 :- If the rate grows 200% of the specified value	
        elif rate>10:
                message = "This rate of influx of articles is very slow."
                d = {rate:message}
			
        else:
                message = "This is a favorable rate."
                d = {rate:message}		
				
        print json.dumps(d, indent = 1, separators=(': '))			
        sys.stdout.flush()
        lastInstance = present
