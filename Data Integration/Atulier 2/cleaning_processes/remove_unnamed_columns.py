import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class RemoveUnnamedColumns(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        return df
