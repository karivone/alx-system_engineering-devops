#!/usr/bin/python

'''
This module enables us to run our code in production
'''
from flask import Flask
import os

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """This function returns a string when called upon"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # use command line arguments to determine the environment
    import sys
    if sys.argv[0] == "python3":
        # Run the app in development mode
        app.run(host='0.0.0.0', port=5000, debug=True)

    elif sys.argv[0] == "gunicorn":
        # Run the app in production mode
        from wsgi import app
        app.run(host='0.0.0.0', port=5000)

    app.run(host='0.0.0.0', port=5000)
