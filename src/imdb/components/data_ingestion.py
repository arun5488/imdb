from src.imdb import logger
from src.imdb.entity import DataIngestionConfig
from datasets import load_dataset
from src.imdb import constants as const
from datasets import DatasetDict

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        logger.info("Initiatizing DataIngestion class")
        self.config = config

    
    def initiate_data_ingestion(self):
        try:
            raw_imdb = load_dataset(const.DATASET_NAME)
            imdb = DatasetDict()
            for split in raw_imdb:
                subset = raw_imdb[split].train_test_split(test_size=const.DATASET_SPLIT, shuffle=True, seed=42)['test']
                imdb[split]=subset

            logger.info(f"{const.DATASET_SPLIT} is saved locally from the main dataset")
            imdb.save_to_disk(self.config.dataset)
            logger.info(f"dataset saved to {self.config.dataset}")

        except Exception as e:
            logger.error(f"error occured inside initiate_data_ingestion:{e}")
            raise e
