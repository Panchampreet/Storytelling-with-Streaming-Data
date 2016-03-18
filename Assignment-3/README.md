In this assignment, I have made use of the Twitter streaming API to analyze the following properties about the data stream:
(i) The entropy of the tweets received.
(ii) The distribution of the tweets being received with the help of a histogram.
(iii) The probability of the influx of a message from a particular place.
(iv) The rate of the stream.

The flow of control in the app goes as shown in the following pipeline:

python fetchTweetData.py | python populateRedis.py
& decrement.py
& computeStatistics.py

Much of the code in all programs is extended from the code in the corresponding modules provided in this repository by Mike Dewar:- https://github.com/mikedewar/RealTimeStorytelling/tree/master/3.
