import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class RemoveAnnomalies(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # remove row that are not supposed to contain numbers
        df = self.remove_rows_with_numbers(df, ['nom','prenom'])
        # show rows with number
        
        
        
        
        
        return df
    def remove_rows_with_numbers(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            # Filter rows where the specified column contains numbers
            rows_with_numbers = df[df[column].str.contains(r'\d', na=False)]
            if rows_with_numbers.empty:
                self.logger.info(f"No rows with numbers found in '{column}' column.")
            else:
                self.logger.info(f"Found rows with numbers in '{column}' column: {rows_with_numbers}")
                # Remove rows where the specified column contains numbers
                df = df[~df[column].str.contains(r'\d', na=False)]
        return df