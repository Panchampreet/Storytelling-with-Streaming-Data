# This script is a primary flask init script for the Flask setup

from flask import Flask

rateTracker = Flask(__name__)
from rateTracker import views
