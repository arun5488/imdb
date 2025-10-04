from src.imdb import logger
from src.imdb.components.data_ingestion import DataIngestion
from src.imdb.config.configuration import ConfigurationManager

class DataIngestionPipeline:
    def __init__(self):
        logger.info("Initialized DataIngestionPipeline")
        self.config = ConfigurationManager().get_data_ingestion_config()
    
    def initiate_data_ingestion_pipeline(self):
        try:
            logger.info("Inside initiate_data_ingestion_pipeline method")
            DataIngestion(self.config).initiate_data_ingestion()
        except Exception as e:
            logger.error(f"Error occured inside initiate_data_ingestion_pipeline: {e}")
            raise e