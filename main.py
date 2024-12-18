from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)