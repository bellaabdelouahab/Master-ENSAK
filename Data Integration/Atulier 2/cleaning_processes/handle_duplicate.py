import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class HandleDuplicate(DataCleaner):

    def log_and_remove_duplicates(self, df: pd.DataFrame, subset: list, description: str) -> pd.DataFrame:
        duplicates = df[df.duplicated(subset=subset, keep=False)]
        self.logger.info(f"{description} duplicates:\n{duplicates}")
        df = df.drop_duplicates(subset=subset)
        return df

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Starting duplicate removal process")
        initial_row_count = len(df)
        
        df = self.log_and_remove_duplicates(df, df.columns.tolist(), "Full (100%)")
        df = self.log_and_remove_duplicates(df, df.columns[:-1].tolist(), "Partial (90%)")
        df = self.log_and_remove_duplicates(df, df.columns[:-2].tolist(), "Partial (80%)")
        df = self.log_and_remove_duplicates(df, df.columns[:-3].tolist(), "Partial (70%)")
        df = self.log_and_remove_duplicates(df, df.columns[:-4].tolist(), "Partial (60%)")

        final_row_count = len(df)
        self.logger.info(f"Removed {initial_row_count - final_row_count} duplicate rows")
        self.logger.info("Duplicate removal process completed")
        return df
