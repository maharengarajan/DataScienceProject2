from src.components.data_ingestion import DataIngestion
from src.exception.exception import CustomException
from src.logging.logger import LoggerConfig
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
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
    except Exception as e:
           raise CustomException(e,sys)