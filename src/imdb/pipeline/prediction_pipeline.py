from src.imdb import logger
from src.imdb import constants as const
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from src.imdb.cloud.s3Syncer import S3Sync
from src.imdb.utils.common import read_yaml

class PredictionPipeline:
    def __init__(self):
        logger.info("Initialized Prediction Pipeline")
        self.s3sync = S3Sync()
        self.config = read_yaml(const.CONFIG_FILE)
    
    def sync_s3_to_artifacts(self):
        try:
            logger.info("inside sync_s3_to_artifacts method")
            artifacts_dir = self.config.root_dir
            logger.info(f"artifacts dir: {artifacts_dir}")
            aws_bucket_url=f"s3://{const.AWS_S3_BUCKET}/artifact/{artifacts_dir}"
            logger.info(f"aws bucket url:{aws_bucket_url}")
            self.s3sync.sync_s3_to_local(aws_bucket_url=aws_bucket_url, local_dir_path=artifacts_dir)
            logger.info(f"S3 bucket and local artifacts folder are in sync")
        except Exception as e:
            logger.error(f"Error occured inside sync_s3_to_artifacts method:{e}")
            raise e
    
    def perform_classification(self, text):
        try:
            logger.info("Inside perform_classification method")
            logger.info("Initiating s3-Artifacts folder sync")
            self.sync_s3_to_artifacts()
            logger.info("Sync complete")
            logger.info(f"loading tokenizer from {const.TOKENIZER}")
            tokenizer = AutoTokenizer.from_pretrained(const.TOKENIZER)
            logger.info("tokenizer loaded from local")
            logger.info(f"loading model from {const.FINAL_MODEL}")
            model = AutoModelForSequenceClassification.from_pretrained(const.FINAL_MODEL)
            logger.info("model loaded from local")
            classifier = pipeline(const.PIPELINE_TASK, model = model, tokenizer = tokenizer)
            result = classifier(text)
            logger.info(f"result: {result}")
        except Exception as e:
            logger.error(f"error occured inside perform_classification:{e}")
            raise e
