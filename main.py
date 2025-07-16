from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.exception.exception import CustomException
from src.logging.logger import LoggerConfig
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
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
    except Exception as e:
           raise CustomException(e,sys)