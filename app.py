from flask import Flask
import sys
from Bike.logger import logging
from Bike.exception import BikeException

app = Flask(__name__)

@app.route("/" ,methods=['GET','POST' ])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        Bike= BikeException(e,sys)
        logging.info(Bike.error_message)
        logging.info("we r testing logging module")

    return "CI CD  with entity pipeline has been established"

if __name__== "__main__":
  app.run(debug=True)
