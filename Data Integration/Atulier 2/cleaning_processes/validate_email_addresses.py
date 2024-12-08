import pandas as pd
import logging
from cleaning_processes.data_cleaner import DataCleaner
from validate_email import validate_email

class ValidateEmailAddresses(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Starting email validation process")
        if 'email' not in df.columns:
            self.logger.error("DataFrame does not contain 'email' column")
            raise ValueError("DataFrame must contain 'email' column")

        df['email'] = df['email'].astype(str).apply(lambda email: email if validate_email(email) else None)
        self.logger.info("Email validation process completed")
        return df
