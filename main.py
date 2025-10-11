from src.imdb import logger
from src.imdb.pipeline.training_pipeline import TrainingPipeline
from src.imdb.pipeline.prediction_pipeline import PredictionPipeline


if __name__ == "__main__":
    logger.info("Inside main")
    text ="This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."
    result = PredictionPipeline().perform_classification(text=text)
    logger.info(result)