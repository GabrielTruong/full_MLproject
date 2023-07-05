import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig: 
    preprocessor_object_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        Function responsible for tranforming the data
        '''
        try:
            numerical_features = ["writing_score","reading_score"]
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical columns standard scaling completed")

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("scaler",OneHotEncoder()),
                    ("standard scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical columns encoding completed")

            logging.info(f"Categorical features: {categorical_features}")
            logging.info(f"Numerical features: {numerical_features}")

            preprocessor = ColumnTransformer([
                ("numerical_pipeline",numerical_pipeline,numerical_features),
                ("categorical_pipeline",categorical_pipeline,categorical_features)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            preprocessor_object = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_features = ["writing_score","reading_score"]

            input_feature_train_df = train_df.drop(target_column_name,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(target_column_name,axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on train df and test df")

            input_feature_train_arr = preprocessor_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_object_path,
                obj = preprocessor_object
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_object_path
            )

        except Exception as e:
            raise CustomException(e,sys)