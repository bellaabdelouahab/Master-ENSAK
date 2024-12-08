import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class HandleInvalidDates(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # Handle invalid dates in the specified columns
        df = self.handle_invalid_dates(df, ['date_naissance', 'created'])
        
        # costume handling for date_naissance out layer dates
        df = self.remove_outlayer_dates(df, ['date_naissance'])
        return df

    def handle_invalid_dates(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            # try to convert the column to datetime format with try and except
            try:
                df[column] = pd.to_datetime(df[column], errors='raise')
                self.logger.info(f"Successfully converted '{column}' column to datetime format.")
            except Exception as e:
                self.logger.error(f"Failed to convert '{column}' column to datetime format: {e}")
                # Handle invalid dates by setting them to NaT
                df[column] = pd.to_datetime(df[column], errors='coerce')
                self.logger.info(f"Handled invalid dates in '{column}' column by setting them to NaT.")
        return df
    def remove_outlayer_dates(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        for column in columns:
            # Calculate the mean and standard deviation of the dates
            mean_date = df[column].mean()
            std_date = df[column].std()
            
            # Define the range for outliers as mean ± 3*std
            lower_bound = mean_date - 3 * std_date
            upper_bound = mean_date + 3 * std_date
            
            # Filter rows where the specified column contains outlier dates
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        return df