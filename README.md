## Classification if IMDB reviews using huggingface transformers

This project implements the task of classifying the imdb reviews into Positive/Negative review.

# Dataset
The project uses imdb dataset present in hugging face, using various inbuilt dataset library methods the data is prepared and saved locally in the artifacts folder and synced to aws s3 bucket for storage

# Data transformation 
Checkpoint - distilbert/distilbert-base-uncased
https://huggingface.co/distilbert/distilbert-base-uncased

Data is then loaded from the local and tokenized using the tokenizers. Only 20% of the dataset is used for this project as the resources available in local is not sufficient to handle this much of data

tokenized data is also pushed to s3 bucket

# model trainer
The model is trained using the free gpus in google colab and the model weights are stored in the s3 bucket. The models weights are then synced to local artifacts in the to run the prediction pipeline from the local. 

Prediction pipeline is implemented and served on Flask on UI.

The entire artifacts folder size comes up to 2 GB, so it was not deployed to aws due to space constraints.

