from src.imdb.pipeline.prediction_pipeline import PredictionPipeline
from src.imdb import logger
from src.imdb import constants as const
from flask import Flask, render_template, url_for, request
import os 
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    try:
        logger.info('Inside index method, launching index.html')
        if request.method == 'POST':
            logger.info("Inside POST method")
            sentence = request.form.get('sentence')
            logger.info(f"recieved review: {sentence}")
            predictedvalue = PredictionPipeline().perform_classification(sentence)
            logger.info(f'Predicted value: {predictedvalue}')
            return render_template('index.html', sentence = sentence, predictedvalue = predictedvalue)
        else:
            logger.info(f"inside {request.method} method")
            return render_template('index.html')

    except Exception as e:
        logger.error("Error occured inside index method: {e}")
        raise e
    
if __name__ == '__main__':
    logger.info("Inside app.py")
    load_dotenv(dotenv_path= const.FLASK_ENV)
    host = os.getenv('FLASK_RUN_HOST')
    logger.info(f"host: {host}")
    port = os.getenv('FLASK_RUN_PORT')
    logger.info(f"port: {port}")

    app.run(host=host, port=port, debug=True)
    