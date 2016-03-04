In this assignment, I have made use of the Times Newswire API from the New York Times. I capture a stream of the articles emitted from the API according to a random rate generated using the "numpy" module of python with its random function, which results in the stream representing a Poisson process.
Following it, I analyze the rate of the stream and display it on the output.
Moreover, I have also setup an alerting system which sends out alerts in print when the rate of the stream goes very high or low, in relation to hard-coded time periods.
