
# The following program is used to decrement the value of the key before it is sent into the hash.

# Following are the statements which are used to include the in-built python modules on which the program depends.
import redis  # This imports the module that enables interaction of the application with the key-value database Redis.
import time   # This imports the module which is used to access various time-related functions.

# The following line is used to establish a connection with Redis database.
conn = redis.Redis()

# The following section of code runs forever until externally stopped.
while True:
    # This line saves all keys in the table into a variable named places.
    places = conn.keys()

# The following lines are used to get the count of tweets that have been posted from a single place.
    for place in places:
        d = conn.hgetall(place)

# The following lines check if thwere are more than one tweets being posted from a given place
# and if so, sets it equal to its corresponding value in the hash.
        for ref in d:
            if int(d[ref]) > 1:
                count = int(d[ref])
                count -= 1
                d[ref] = str(count)
        conn.hmset(place,d)
 
# the following line sets the duration of the time cycle of each operation.
    time.sleep(2)
