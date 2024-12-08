import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class TextCapitalizationStandardization(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # Standardize text capitalization for all string columns
        text_cols = df.select_dtypes(include=['object', 'category']).columns
        for col in text_cols:
            if col == 'prenom':
                df[col] = df[col].str.capitalize()
            elif col == 'nom':
                df[col] = df[col].str.upper()
        return df