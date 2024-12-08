import logging
import os
from dotenv import load_dotenv
import pandas as pd
from cleaning_processes.handle_invalid_dates import HandleInvalidDates
from cleaning_processes.remove_special_characters import FixSpecialCharacters
from cleaning_processes.handle_missing_values import HandleMissingValues
from cleaning_processes.remove_unnamed_columns import RemoveUnnamedColumns
from cleaning_processes.text_capitalization_standardization import TextCapitalizationStandardization
from cleaning_processes.remove_annomalies import RemoveAnnomalies
from cleaning_processes.validate_email_addresses import ValidateEmailAddresses
from cleaning_processes.validate_phone_numbers import ValidatePhoneNumbers
from cleaning_processes.handle_cin import HandleCin
from cleaning_processes.handle_duplicate import HandleDuplicate

def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    return logger

def load_environment():
    load_dotenv()
    env_vars = {
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'API_KEY': os.getenv('API_KEY')
    }
    return env_vars

def main():
    logger = setup_logger()
    logger.info("Starting the application")

    env_vars = load_environment()
    logger.info(f"Loaded environment variables: {env_vars}")

    # Load the dataset
    df = pd.read_csv('c:/GitHub/Master-ENSAK/Data Integration/Atulier 2/datasets/excel-2015.csv')
    # df = pd.read_csv('c:/GitHub/Master-ENSAK/Data Integration/Atulier 2/datasets/cleaned_excel-2015.csv')

    # Perform cleaning processes
    df = RemoveUnnamedColumns(logger).clean(df)
    df = HandleMissingValues(logger).clean(df)
    df = TextCapitalizationStandardization(logger).clean(df)
    df = RemoveAnnomalies(logger).clean(df)
    df = HandleInvalidDates(logger).clean(df)
    df = ValidateEmailAddresses(logger).clean(df)
    df = ValidatePhoneNumbers(logger).clean(df)
    df = HandleCin(logger).clean(df)
    df = FixSpecialCharacters(logger).clean(df)
    df = HandleDuplicate(logger).clean(df)

    logger.info(f"Cleaned DataFrame: {df}")

    # Save cleaned dataset
    df.to_csv('c:/GitHub/Master-ENSAK/Data Integration/Atulier 2/datasets/cleaned_excel-2015.csv', index=False)

if __name__ == "__main__":
    main()