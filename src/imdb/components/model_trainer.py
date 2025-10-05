from src.imdb import logger
from src.imdb.entity import ModelTrainerConfig
from src.imdb import constants as const
import evaluate
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer, AutoTokenizer
from src.imdb.utils.common import dataset_load_from_disk
import numpy as np
from datasets import load_from_disk
from transformers import DataCollatorWithPadding

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        logger.info("Initialized Model Trainer")
        self.accuracy = evaluate.load("accuracy")
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer)
        self.dataset = dataset_load_from_disk(config.transformed_data)
        self.model = AutoModelForSequenceClassification.from_pretrained(config.model_name, num_labels = 2, 
                                                                        id2label= const.ID2LABEL, label2id=const.LABEL2ID)
    
    def compute_metrics(self, eval_pred):
        try:
            logger.info("inside compute_metrics method")
            predictions, labels = eval_pred
            predictions = np.argmax(predictions, axis=1)
            return self.accuracy.compute(predictions=predictions, references=labels)
        except Exception as e:
            logger.error(f"Error occured inside compute_metrics:{e}")
            raise e
    
    def initiate_model_training(self):
        try:
            logger.info("inside initiate_model_training method")
            data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)

            training_args = TrainingArguments(
                output_dir= self.config.local_model,
                learning_rate=2e-5,
                per_device_train_batch_size=16,
                per_device_eval_batch_size=16,
                num_train_epochs=2,
                weight_decay=0.01,
                eval_strategy="epoch",
                save_strategy="epoch",
                load_best_model_at_end=True,
                push_to_hub=False,
                report_to="none" # Add this line to disable wandb logging
            )

            trainer = Trainer(
                model=self.model,
                args=training_args,
                train_dataset=self.dataset['train'],
                eval_dataset=self.dataset['test'],
                processing_class=self.tokenizer,
                data_collator=data_collator,
                compute_metrics=self.compute_metrics,
            )

            trainer.train()                     
        except Exception as e:
            logger.error(f"Error occured inside initiate_model_training method:{e}")
            raise e

    