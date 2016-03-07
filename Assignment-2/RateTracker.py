# This program does the bulk of the work for the assignment. It fetches the output from the
# 'poll_API.py' script as json, analyzes the rate with which it is streaming, and sends out
# alerts when the rate exceeds a threshold time value or falls below another threshold.

# Following are the 'import' statements necessary to include library modules

from flask import Flask
import time
import requests
import sys
import json

# The following statement is used to create a rateTracker object of class Flask
# in effect setting up the flow between this script and the front-end with the
# help of Flask web framework for python.

rateTracker = Flask(__name__)

# The route function is used to create the mapping from URL /index to this function
@poll_API.route("/")

# The following statement is used to make another file 'index.html' load whenever
# this script gets called in the flask directory structure.

def main():
	return render_template('index.html')
	
	# The following section of code is what is responsible for rate analysis part of the assignment.
	# News article stream in JSON format being sent out by the 'poll_API.py' script is piped into
	# this script from the bash shell/powershell.
	
	# An initial value of instance of time equal to 0 is given to this 'lastInstance' variable here.
        lastInstance = 0

        # The following snippet regularly fetches the JSON article stream from the 'poll_API.py' script
        while True:
      	        line = sys.stdin.readline()
                save = json.loads(line)
                present = time.time()
	
	# The following lines do some error-handling related to the lastInstance variable value   
        if lastInstance == 0 :
                lastInstance = present
                continue
        
        # The following line calculates the rate of stream as difference between the
        # present time value and the lastInstance value.
        rate = present - lastInstance
        print "\n"

        # The following section creates alerts associated with different cases of
        # the erratic behavior of the article stream rate.
	
        # Case 1 :- If the rate falls below 20% of the base value of 5 seconds,
        #           the rate is considered to be too fast for processing,
        #           and a relevant message is displayed to the output.
        if rate<1:
                message = "This rate of influx of articles is too fast!"
                d = {rate: message}    
	
        # Case 2 :- If the rate grows 200% of the base value,
        #           the rate is deemed too slow for being captured reliably,
        #           and a relevant corresponding message is output.
        elif rate>10:
                message = "This rate of influx of articles is very slow."
                d = {rate:message}
			
        # Case3:- If the rate of incoming stream stays within a suitable hard-coded
        #         range from 1 to 10 seconds, a message indicating the same is displayed
        #         on the output.
        else:
                message = "This is a favorable rate."
                d = {rate:message}		

	# The following snippet only functions to make the above
	# information get displayed in a pretty-print in the JSON format.
	
        print json.dumps(d, indent = 1, separators=(': '))			
        sys.stdout.flush()
        lastInstance = present
