from src.imdb import logger
from src.imdb.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    logger.info("Inside main")
    TrainingPipeline().initiate_training_pipeline()