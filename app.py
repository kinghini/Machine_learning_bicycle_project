from flask import Flask
from Bike.logger import logging

app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def  index():
    logging.info("we are testing logging")
   
    return "Bike_rental CI/CD pipeline has established"


if __name__== "__main__" :
       app.run(debug=True)

