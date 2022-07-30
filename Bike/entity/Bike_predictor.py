import os
import sys

from Bike.exception import BikeException
from Bike.util.util import load_object

import pandas as pd

##change from 25
class BikeData:

    def __init__(self,
                instant:int,
                season :int,
                yr :int,
                month:int,
                hr:int,
                holiday : int, 
                weekday :int, 
                workingday : int,
                weathersit : int,
                temp : float,
                atemp : float,
                hum : float,
                windspeed : float,
                cnt: int= None
                 ):
        try:
            
                self. instant = instant,
                self.season = season
                self.yr = yr
                self.month= month
                self.hr= hr
                self.holiday = holiday
                self.weekday = weekday 
                self.workingday = workingday
                self.weathersit = weathersit
                self.temp =temp
                self.atemp = atemp
                self.hum = hum
                self.windspeed =windspeed
                self.cnt = cnt
            
        except Exception as e:
            raise BikeException(e, sys) from e

    def get_Bike_input_data_frame(self):

        try:
            Bike_input_dict = self.get_Bike_data_as_dict()
            return pd.DataFrame(Bike_input_dict)
        except Exception as e:
            raise BikeException(e, sys) from e

    def get_Bike_data_as_dict(self):
        try:
            input_data = {
                
                "instant":[self. instant ],
               "season" :[self.season] ,
                "yr":[self.yr],
                "month":[self.month],
                "hr":[self.hr],
                "holiday":[self.holiday], 
                "weekday":[self.weekday],
                "workingday":[self.workingday], 
                "weathersit":[self.weathersit ],
                "temp":[self.temp],
                "atemp":[self.atemp ],
                "hum":[self.hum], 
                "windspeed":[self.windspeed] 
                }
            return input_data
        except Exception as e:
            raise BikeException(e, sys)


class BikePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise BikeException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise BikeException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_bike_rent_value = model.predict(X)
            return median_bike_rent_value
        except Exception as e:
            raise BikeException(e, sys) from e