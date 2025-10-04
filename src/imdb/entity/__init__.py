from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    dataset: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    dataset: Path
    tokenizer_name: Path
    local_tokenier: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    model_name: Path
    tokenizer: Path
    