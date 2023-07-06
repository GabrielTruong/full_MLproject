## END TO END ML PROJECT - MY GETBACK PROJECT
### Installation
First create your python environment and activate it using the following command: 
```bash
conda create -p <venv name> python==3.8 -y
conda activate <project_path/venv name>
```

Then install all the pre-requisite packages:
```python
pip install - requirements.txt
```

Launch the application:
```python
python app.py
```

You can access the application at the following URL to do your prediction:
http://127.0.0.1:5000/prediction

TRY IT !

## Lessons from this project

### Setup
This ML project will be used as a package. So we created the *setup.py* file. This file is super useful because when you use the command `pip install -r requirements.txt` it will launch a series of command to setup the environment. Inside the file we used the very import setup function that enables all the packages to be recognized as such (would have soleved many problems in my poc_to_prod project).

### Exception
We created an *exception.py* file to custom our own exceptions. To do that we import the sys module to interact with the interpreter.
Then we created a function that returns an error message describing where the error occured (which file) alongside the error message. This function will be used to initialize our CustomException class that inherits the Exception class itself.

This message will then appear in all of our code whenever using a *try catch* statement. 

### Logger
Whenever we get an exception, we will take this exception, log in the logger file and put it in the logger file.

### Model Development (notebook)
In this step, we just quickly develop a model in jupyter notebook first. The process of model selection is standard but a bit rushed because that is not the purpose of this project. After building the model in the notebook, we will map it into production .py file.

### Data Ingestion
This file aims to split the data from a raw file into train and test split and store in csv files. We used a class with the `@dataclass` decorator. 
By using the @dataclass without using the constructor __init__(), the class (DataTransformationConfig ) accepted the value and assigned to the given variable, so that in this case automatically the 'preprocessor.pkl' file will be created in the 'artifacts' folder... 
Then we created the class that will do the splitting job. With always making sure using logging and exception to keep track of where errors could come from.

### Data Transformation
This file aims to perform the transformation needed on the data prior training the ML model. First we created the `DataTransformation` class. In this class, we have the first function `get_data_transformer_object` that will return an object that will do the preprocessing in chain. This object will then be used in the `initiate_data_transformation` to perform the transformation on the actual data. The preprocessor will also be saved in a pkl file.

### Model Trainer
- Import the data
- Train different models (cf.utils)
- Perform GridSearchCV to find best parameters
- Save the best model based on r2_score

### Predict Pipeline
- Create a class with all the data given by the user
- Import the model & preprocessor from saved pickle file (with a function from utils)
- Predict the math score from the data stored in the CustomData class

### Flask APP
- Gather data given in the html form by the user and instanciate the CustomData class with those data
- Call the predict pipeline and pass the data
- Return the prediction

=> Need to add a POST endpoint with data passed as json and curl request for the app able to be use as microservices 


