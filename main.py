from Weather_Image_Classification import logger
from Weather_Image_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Weather_Image_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Weather_Image_Classification.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME_INGESTION = 'Data Ingestion Stage'
try:
   logger.info(f">>>>>> stage {STAGE_NAME_INGESTION} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME_INGESTION} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    


STAGE_NAME_PREPARE_BASE_MODEL = 'Prepare Base Model'
try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_PREPARE_BASE_MODEL}\n{"**"*50}\n')
    prepare_model = PrepareBaseModelTrainingPipeline()
    prepare_model.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_PREPARE_BASE_MODEL}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME_TRAINING= 'Training'
try:
    logger.info(f'\n\n{"**"*50}\nStarted {STAGE_NAME_TRAINING}\n{"**"*50}\n')
    trainer = ModelTrainingPipeline()
    trainer.main()
    logger.info(f'\n\n{"**"*50}\nCompleted {STAGE_NAME_TRAINING}\n{"**"*50}\n\n')
    
except Exception as e:
    logger.exception(e)
    raise e