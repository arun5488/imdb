from src.imdb import logger
from src.imdb.pipeline.data_ingestion_pipeline import DataIngestionPipeline

class TrainingPipeline:
    def __init__(self):
        logger.info("Initialized TrainingPipeline")
    
    def initiate_training_pipeline(self):
        try:
            logger.info("Inside initiate_training_pipeline method")
            logger.info("Initiating DataIngestion Stage")
            DataIngestionPipeline().initiate_data_ingestion_pipeline()
            logger.info("Data Ingestion Stage completed")
        except Exception as e:
            logger.error(f"Error occured inside initiate_training_pipeline: {e}")
            raise e