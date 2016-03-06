from rateTracker import rateTracker

@rateTracker.route('/')
@rateTracker('/index')
def index():
    return "Hello, World!"
