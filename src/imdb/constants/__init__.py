CONFIG_FILE = "config/config.yaml"
SCHEMA_FILE = "schema.yaml"
PARAMS_FILE = "params.yaml"

#data_ingestion
DATASET_NAME="imdb"
DATASET_SPLIT = 0.2

#model_trainer
ID2LABEL = {0: "NEGATIVE", 1: "POSITIVE"}
LABEL2ID = {"NEGATIVE": 0, "POSITIVE": 1}

#AWS 
AWS_S3_BUCKET= "bsaarun54.imdb"

#prediction pipeline
PIPELINE_TASK = "sentiment-analysis"
FINAL_MODEL = "artifacts/model_trainer/model/final_model"
TOKENIZER = "artifacts/data_transformation/tokenizer"

FLASK_ENV = '.flaskenv'