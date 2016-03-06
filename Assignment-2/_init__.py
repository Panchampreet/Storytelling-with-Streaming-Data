from flask import Flask

rateTracker = Flask(__name__)
from rateTracker import views
