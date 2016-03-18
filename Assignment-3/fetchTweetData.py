
# This program is used to fetch streaming data from the Twitter API and extract information
# most relevant for us from each JSON object being fetched.

# The following statements are used to include the in-built python modules on which the program depends.
from TwitterAPI import TwitterAPI   # This imports the module required for accessing the streaming API from twitter.
import time                         # This imports the module which is used to access various time-related functions.
import sys                          # This imports a module which is necessary to engage the python interpreter.
import json                         # This imports a module used in deciphering and enciphering of the JSON data format.


# The following line is used to authenticate our access to the API on Twitter's website by filling in the correct consumer key and access key.
api = TwitterAPI(
		    'vkXJELmhvtBJwkbtt1rxe4cta',
                    '87HfgCeY2YRoxqMUniu3r5Kom0XDZZuo4MWnApt3SNh8HnScvI',
                    '2234996689-0livw7Tv5lQjwvmG0lbli8EKKm4VJVvU2BL4325',
                    '70sJwzSdtUjlcifSOptGLGrQ6QmETZZ2NmlNstPduwhKm'
		)

# The following line asks teh API to stream the set of tweets which are being collected from within New York city.
r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})

# The following statements are used to extract the information that is the most relevant to us
# from the incoming JSON tweets and printing them out to standard output.
for item in r:
	print json.dumps({"text": item['text'], "ID": item['id'], "Place": item['place']['full_name']})
	sys.stdout.flush()
