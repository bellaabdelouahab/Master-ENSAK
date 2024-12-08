import pandas as pd
import unicodedata
from cleaning_processes.data_cleaner import DataCleaner

class FixSpecialCharacters(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Starting special characters fixing process")
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = df[column].apply(self.fix_special_characters)
        self.logger.info("Special characters fixing process completed")
        return df

    def fix_special_characters(self, text: str) -> str:
        if not isinstance(text, str):
            return text
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
        return text
