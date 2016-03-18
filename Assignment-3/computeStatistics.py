# This program does the majority of the work for the assignment:
# (a) plotting the histogram of the distribution of the stream messages,
# (b) evaluating the entropy of the stream
# (c) calculating the probability of influx of a specific type of messages

# The following few statements featuring the word 'import' are special statements aimed at including
# the main in-built python modules into the program that are necessary for its execution

import flask               # This imports the flask framework that gets used in rendering the functioanlity of the program in the form a web application.
from flask import request  # This imports a special sub-module of flask named 'requests', which is used to handle http requests to the web-page of the app.
import redis               # This imports the module that enables interaction of the application with the key-value database Redis.
import collections         # This imports a module that facilitates the use of special container data types.
import json                # This imports a module used in deciphering and emission of the JSON data format.
import numpy as np         # This imports a mathematical module which is used in statistical computations, such as those carried  in this application.
from TwitterAPI import TwitterAPI  # This imports the module required for accessing the streaming API from twitter.
import math

# The following line is used to authenticate our access to the API on Twitter's website by filling in the correct consumer key and access key.
api = TwitterAPI(
		    'vkXJELmhvtBJwkbtt1rxe4cta',
                    '87HfgCeY2YRoxqMUniu3r5Kom0XDZZuo4MWnApt3SNh8HnScvI',
                    '2234996689-0livw7Tv5lQjwvmG0lbli8EKKm4VJVvU2BL4325',
                    '70sJwzSdtUjlcifSOptGLGrQ6QmETZZ2NmlNstPduwhKm'
		)			
		
# The following lines establish connection of the app with the Flask framework as well as Redis database.
app = flask.Flask(__name__)
conn = redis.Redis()

total=0
last=0

#The following function includes statements that create a histogram out of the distribution of tweets from the stream. 
def createHistogram():
    keys = conn.keys()
    values = conn.mget(keys)
    c = collections.Counter(values)
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}

# The following function calls the above function which created the histogram and displays it on standard output.
@app.route("/")
def histogram():
    #h = buildHistogram()
    #return json.dumps(h)

# The following function computes the entropy of the tweete being received.
def getEntropy():
    h = buildHistogram()
    return -sum([p*np.log(p) for p in h.values()]) 
    

# The following function evaluates the probability of receipt of tweets
# from a particular place where one or two of them were received from earlier.
@app.route("/probability")
def probability():
    place = request.args.get('PlaceOfTweet', '')
    count = request.args.get('total', '')
    # get the distribution for the language
    print place
    d = conn.hgetall(PlaceOfTweet)
    # get the count
    try:
      c = d[total]
    except KeyError:
      return json.dumps({
        "Place": place, 
        "prob": 0,
        "number": total
      })
    # get the normalising constant
    z = sum([float(v) for v in d.values()])
    return json.dumps({
      "Place": place, 
      "prob": float(c)/z,
      "number": total
      })
	  
# The following function makes a call to the function above which calculated the entropy of the stream
# and also judges any changes in the values of entropy. If it finds that a change has occured, it 
# immediately sends out an alert in the form a tweet indicating so.
@app.route("/")
def publishEntropyChange():
	#if sudden change in entropy post a tweet on twitter
    if (abs(getEntropy()-last) > 0):	
                               total+=1
    r = api.request('statuses/update', {'status': 'sudden change'+str(total)})
    last = getEntropy()  

# The following lines are simply used to start the execution of the program.
if __name__ == "__main__":
    app.debug = True
    app.run()
