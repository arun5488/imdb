import os
from src.imdb import logger

class S3Sync:
    def __init__(self):
        logger.info("Initialized S3Sync")
    
    def sync_local_to_s3(self, local_dir_path, aws_bucket_url):
        try:
            logger.info("Inside sync_local_to_s3 folder")
            logger.info(f"local dir path: {local_dir_path}")
            logger.info(f"aws bucket url:{aws_bucket_url}")
            command = f"aws s3 sync {local_dir_path} {aws_bucket_url}"
            os.system(command)
        except Exception as e:
            logger.error(f"Error occured inside sync_local_to_s3:{e}")
            raise e
    
    def sync_s3_to_local(self, aws_bucket_url, local_dir_path):
        try:
            logger.info("Inside sync_s3_to_local method")
            logger.info(f"local dir path: {local_dir_path}")
            logger.info(f"aws bucket URL: {aws_bucket_url}")
            command = f"aws s3 sync {aws_bucket_url} {local_dir_path}"
            os.system(command=command)
        except Exception as e:
            logger.error(f"Error occured inside sync_s3_to_local method: {e}")
            raise e