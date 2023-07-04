import os 
import sys
from src.exception import CustomException 
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        #Read data from a DB with the client
        logging.info("Entered the data ingestion method of component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the datasets as a DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) 
            #exsit_ok -> if it is already there no need to delete and recreate the folder      

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) 

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size = 0.2, random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
            #Will be required for data transformation later in the pipeline

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformer = DataTransformation()
    data_transformer.initiate_data_transformation(train_data,test_data)