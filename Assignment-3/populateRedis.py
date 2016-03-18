# This program is used to process the data extraced from the Twitter stream
# in 'fetchweetData.py' program, and store it in Redis database as required
# to make it available for statistical analysis.

# Following are the statements which are used to include the in-built python modules on which the program depends.
import json
import sys
import redis
import time

# The following line is used to establish a connection with Redis database.
conn = redis.Redis()

while True:
    # This line is used to fetch the data being printed at standard output.
    line = sys.stdin.readline()
    # The following lines store the inout data in a variable called 'd' in an error-proof method.
    try:
        d = json.loads(line)
    except ValueError:
        # sometimes we get an empty line, so just skip it
        continue

	# These lines capture the ID element of the fetched JSON.
    try:
        TweetID = d["ID"]
    except KeyError: 
        # if there is no ID attribute in the tweet
        # then skip it
        continue
	
	# These lines capture the Place element of the fetched JSON.
	try:
        PlaceOfTweet = d["Place"]
    except KeyError: 
        # if there is no Place attribute in the tweet
        # then skip it
        continue	

    # The following lines increment the value of the count of tweets against each location recorded for the tweets so far.
	conn.hincrby(PlaceOfTweet, 1)
    
	# These lines print out the new data on the standard output.
	print json.dumps({"Tweet ID": TweetID, "Place where tweeted": PlaceOfTweet})
    sys.stdout.flush()
