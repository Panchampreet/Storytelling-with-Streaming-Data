import json
import time
import sys
import requests

while True:
        # Fetching the response from NY Times through the API
        r = requests.get("http://api.nytimes.com/svc/news/v3/content/nyt/all/24.json?api-key=2bf845abbb668b5d43da6f6387793f27:1:74611818")
    
        # Polling for recently saved articles on the site and displaying on standard output
        for m in r.json()["results"]:
            print json.dumps(m, indent=1)
            sys.stdout.flush()
        
        time.sleep(5)
