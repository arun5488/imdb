import yaml
from datasets import load_from_disk
from src.imdb import logger
from box import ConfigBox
import os

def read_yaml(file_path):
    try:
        with open(file_path) as file:
            content = yaml.safe_load(file)
            if content is None:
                raise ValueError(f" file {file_path} is empty")         
            else:
                return ConfigBox(content)
    except Exception as e:
        logger.error(f"error occured inside read_yaml method:{e}")
        raise e

def create_directories(file_paths: list):
    try:
        for path in file_paths:
            os.makedirs(path, exist_ok= True)
            logger.info(f"folder created in path:{path}")
    except Exception as e:
        logger.error(f"Error occured inside create_directories method:{e}")
        raise e



