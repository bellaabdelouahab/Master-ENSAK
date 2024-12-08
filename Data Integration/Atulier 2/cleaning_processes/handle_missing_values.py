import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class HandleMissingValues(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # Drop columns with 90% or more missing values
        threshold = 0.9
        df = df.loc[:, df.isnull().mean() < threshold]

        # # Fill remaining missing values with the median for numeric columns
        # numeric_cols = df.select_dtypes(include=['number']).columns
        # df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

        # # Fill remaining missing values with the mode for categorical columns
        # categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        # df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

        return df
