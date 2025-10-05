from src.imdb import logger
from src.imdb.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.imdb.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.imdb.cloud.s3Syncer import S3Sync
from src.imdb.utils.common import read_yaml
from src.imdb import constants as const
from src.imdb.pipeline.model_trainer_pipeline import ModelTrainerPipeline

class TrainingPipeline:
    def __init__(self):
        logger.info("Initialized TrainingPipeline")
        self.s3_syncer = S3Sync()
        self.config = read_yaml(const.CONFIG_FILE)
    
    def sync_artifacts_to_s3(self):
        try:
            logger.info("Inside sync_artifacts_to_s3")
            artifacts_dir = self.config.root_dir
            aws_bucket_path = f"s3://{const.AWS_S3_BUCKET}/artifact/{self.config.root_dir}"
            self.s3_syncer.sync_local_to_s3(aws_bucket_url=aws_bucket_path, local_dir_path=artifacts_dir)
            logger.info("Data sync between s3 bucket and artifacts folder")
        except Exception as e:
            logger.error(f"Error occured inside sync_artifacts_to_s3:{e}")
            raise e
    
    def initiate_training_pipeline(self):
        try:
            logger.info("Inside initiate_training_pipeline method")
            # logger.info("Initiating DataIngestion Stage")
            # DataIngestionPipeline().initiate_data_ingestion_pipeline()
            # logger.info("Data Ingestion Stage completed")
            # logger.info("Initiating Data Transformation stage ")
            # DataTransformationPipeline().initiate_data_transformation_pipeline()
            # logger.info("Data Transformation stage completed")
            logger.info("Initiating Model Trainer stage")
            ModelTrainerPipeline().initiate_model_trainer_pipeline()
            logger.info("Model Trainer stage completed")

            logger.info("Initiating syncing between artifacts folder and s3")
            self.sync_artifacts_to_s3()
        except Exception as e:
            logger.error(f"Error occured inside initiate_training_pipeline: {e}")
            raise e