import os

#######################Data Ingestion related paths #######################'
RAW_DIR = "artifacts/raw_data"
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"

#######################Data Processing #######################
PROCESSED_DIR = "artifacts/processed_data"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "train_processed.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "test_processed.csv")

####################### MODEL TRAINING #################
MODEL_OUTPUT_PATH = "artifacts/models/lgbm_model.pkl"