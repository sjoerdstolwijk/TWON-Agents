import dataclasses
import typing


@dataclasses.dataclass
class TrainerConfig:
    num_epochs: int = 5
    batch_size: int = 32
    learning_rate: float = 1e-3


@dataclasses.dataclass
class ClassifierConfig:
    hid_size: int = 512
    dropout: float = 0.2


@dataclasses.dataclass
class Config:
    dataset_path: str = f'../dataset.full.parquet'

    encoder: str = 'Twitter/twhin-bert-base'

    data_out_dir: str = f'./data'
    result_dir: str = f'./results'
    test_size: float = 0.2

    text_column: str = 'text'
    label_columns: typing.List[str] = dataclasses.field(default_factory=lambda: ['model', 'persona', 'topic', 'language'])

    trainer_config: TrainerConfig = dataclasses.field(default_factory=TrainerConfig)
    classifier_config: ClassifierConfig = dataclasses.field(default_factory=ClassifierConfig)
