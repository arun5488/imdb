from src.imdb import logger
from src.imdb.config.configuration import ConfigurationManager
from src.imdb.components.data_transformation import DataTransformation
from datasets import load_from_disk

class DataTransformationPipeline:
    def __init__(self):
        logger.info("Initialized DataTransformationPipeline")
        self.config = ConfigurationManager().get_data_transformation_config()
    
    def initiate_data_transformation_pipeline(self):
        try:
            logger.info("Inside initiate_data_transformation_pipeline method")
            DataTransformation(self.config).initiate_data_tranformation()
        except Exception as e:
            logger.error(f"Error occured inside initiate_data_transformation_pipeline method: {e}")
            raise e