from src.imdb import logger
from src.imdb.entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from src.imdb.utils.common import read_yaml, create_directories
from src.imdb import constants as const

class ConfigurationManager:
    def __init__(self):
        logger.info("Initialized ConfigurationManager class")
        self.config = read_yaml(const.CONFIG_FILE)
        self.schema = read_yaml(const.SCHEMA_FILE)
        self.params = read_yaml(const.PARAMS_FILE)
      
        create_directories([self.config.root_dir])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info("Inside get_data_ingestion_config method")
        try:
            config = self.config.data_ingestion
            logger.info(f"creating directory for Data Ingestion")
            create_directories([config.root_dir])
            return DataIngestionConfig(
                root_dir=config.root_dir,
                dataset=config.dataset
            )
        except Exception as e:
            logger.error(f"error occured inside get_data_ingestion_config: {e}")
            raise e
    
