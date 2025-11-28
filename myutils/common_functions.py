import os
import pandas as pd
from src.logger import get_logger
from src.custom_exceptions import customException
import yaml


logger = get_logger(__name__) #initialize logger

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise customException.FileNotFoundError(f"The file at path {file_path} does not exist.")
        
        with open(file_path, 'r') as yaml_file:
            config_content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file at {file_path} read successfully.")
            return config_content
    except Exception as e:
        logger.error(f"Error reading YAML file at {file_path}: {str(e)}")
        raise customException.YAMLFileReadError(f"Failed to read YAML file at {file_path}") from e


#load data function
def load_data(file_path):
    try:
        logger.info(f"Loading data from {file_path}")
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}, shape: {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {str(e)}")
        raise customException.DataLoadError(f"Failed to load data from {file_path}") from e