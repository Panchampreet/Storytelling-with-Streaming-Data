# 'import' is a keyword in python used to call and include all necessary python
# library modules which are required to make use of pre-defined library functions
# as follows

import json
import time
import sys
import requests

while True:
       # The following function polls the TimesNewswire API for all news articles that have arrived in the past 24 hours.
       # The URL format for this API allows for fetching the articles archived since the past hour upto past 720 hours
       # i.e. the past whole month.
       
        r = requests.get("http://api.nytimes.com/svc/news/v3/content/nyt/all/24.json?api-key=2bf845abbb668b5d43da6f6387793f27:1:74611818")
    
       # The following snippet of code selects the 'results' element from the individual incoming stream components,
       # and displays them as json to standard output.
       
       # For the purposes of this assignment, this output instead of being displayed on standard output
       # is piped into another program named 'RateTracker.py', which calculates the rate of the inbound stream
       # and also executes alerts whenever suitable to a given set of conditions.

       for m in r.json()["results"]:
            print json.dumps(m, indent=1)
            sys.stdout.flush()
