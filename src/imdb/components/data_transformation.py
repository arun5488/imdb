from src.imdb import logger
from src.imdb.entity import DataTransformationConfig
from src.imdb.utils.common import dataset_load_from_disk
from transformers import AutoTokenizer

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        logger.info("Initialized DataTransformation Component")
        self.config = config
        logger.info(f"Instantiating {self.config.tokenizer_name} tokenizer")
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    
    def preprocess_function(self, examples):
        try:
            logger.info("Inside preprocess_function method")
            return self.tokenizer(examples["text"], truncation = True)
        except Exception as e:
            logger.error(f"Error occured inside preprocess_function:{e}")
            raise e

    def initiate_data_tranformation(self):
        try:
            logger.info("Inside initiate_data_transformation method")
            logger.info("Loading dataset from local folders")
            imdb_data_set = dataset_load_from_disk(self.config.dataset)
            logger.info(f"dataset loaded from local folder")
            logger.info("tokenizing the dataset")
            tokenized_imdb = imdb_data_set.map(self.preprocess_function, batched = True)
            logger.info(f"saving the transformed data to {self.config.transformed_data}")
            tokenized_imdb.save_to_disk(self.config.transformed_data)
            logger.info(f"saving the tokenizer to {self.config.local_tokenizer}")
            self.tokenizer.save_pretrained(self.config.local_tokenizer)

        except Exception as e:
            logger.error(f"Error occured inside initiate_data_transformation method:{e}")
            raise e