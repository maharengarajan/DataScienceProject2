from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.exception.exception import CustomException
from src.logging.logger import LoggerConfig
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
import sys

logger = LoggerConfig().get_logger()


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logger.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logger.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logger.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logger.info("data Validation Completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logger.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logger.info("data Transformation completed")

        logger.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logger.info("Model Training artifact created")
    except Exception as e:
           raise CustomException(e,sys)