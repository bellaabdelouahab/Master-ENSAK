import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class HandleCin(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Starting CIN cleaning process")
        if 'cin' not in df.columns:
            self.logger.error("DataFrame does not contain 'cin' column")
            raise ValueError("DataFrame must contain 'cin' column")
        df['cin'] = df['cin'].astype(str).apply(self.clean_cin)
        self.logger.info("CIN cleaning process completed")
        return df

    def clean_cin(self, cin: str) -> str:
        cin = cin.replace(" ", "").upper()
        if len(cin) >= 3 and any(char.isalpha() for char in cin):
            return cin
        else:
            self.logger.warning(f"Invalid CIN: {cin}")
            return None
