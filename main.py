from Weather_Image_Classification import logger
from Weather_Image_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME_INGESTION = 'Data Ingestion Stage'


try:
   logger.info(f">>>>>> stage {STAGE_NAME_INGESTION} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME_INGESTION} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
