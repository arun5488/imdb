from src.imdb import logger
from src.imdb.components.model_trainer import ModelTrainer
from src.imdb.config.configuration import ConfigurationManager

class ModelTrainerPipeline:
    def __init__(self):
        logger.info("Initialized ModelTrainerPipeline")
        self.config = ConfigurationManager().get_model_trainer_config()
    
    def initiate_model_trainer_pipeline(self):
        try:
            logger.info("Inside initiate_model_trainer_pipeline method")
            ModelTrainer(self.config).initiate_model_training()
        except Exception as e:
            logger.error(f"Error occured inside initiate_model_trainer_pipeline:{e}")
            raise e
