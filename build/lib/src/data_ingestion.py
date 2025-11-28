import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exceptions import customException
from config.paths_config import *
from sklearn.model_selection import train_test_split
from myutils.common_functions import read_yaml

#initialize logger magic method
logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        try:
            self.config = config["data_ingestion"]
            self.bucket_name = self.config['bucket_name']
            self.file_name = self.config['file_name']
            self.train_ratio = self.config['train_ratio']
        except Exception as e:
            logger.error(f"Error initializing DataIngestion: {str(e)}")
            raise customException.DataIngestionInitError("Failed to initialize DataIngestion class") from e
        
        logger.info(f"DataIngestion initialized with bucket: {self.bucket_name}, file: {self.file_name}")


    def download_data_from_gcs(self):
        """Downloads data from Google Cloud Storage bucket."""
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            os.makedirs(RAW_DIR, exist_ok=True)
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Data downloaded from GCS bucket {self.bucket_name} to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error(f"Error downloading data from GCS: {str(e)}")
            raise customException.DataDownloadError("Failed to download data from GCS") from e

    def split_data(self):
        """Splits the raw data into training and testing datasets."""
        try:
            df = pd.read_csv(RAW_FILE_PATH)
            train_df, test_df = train_test_split(df, train_size=self.train_ratio, random_state=42)
            train_df.to_csv(TRAIN_FILE_PATH, index=False)
            test_df.to_csv(TEST_FILE_PATH, index=False)
            logger.info(f"Data split into train and test sets at {TRAIN_FILE_PATH} and {TEST_FILE_PATH}")
        except Exception as e:
            logger.error(f"Error splitting data: {str(e)}")
            raise customException.DataSplitError("Failed to split data into train and test sets") from e

    def run(self):
        """Executes the data ingestion process."""
        try:
            self.download_data_from_gcs()
            self.split_data()
            logger.info("Data ingestion process completed successfully.")
        except customException as ce:
            logger.error(f"Error in data ingestion process: {str(ce)}")
            raise ce

        finally:
            logger.info("DataIngestion run method execution finished.")       

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()