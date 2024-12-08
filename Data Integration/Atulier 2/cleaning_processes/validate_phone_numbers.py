import pandas as pd
from cleaning_processes.data_cleaner import DataCleaner

class ValidatePhoneNumbers(DataCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Starting phone number validation process")
        if 'tel' not in df.columns:
            self.logger.error("DataFrame does not contain 'tel' column")
            raise ValueError("DataFrame must contain 'tel' column")
        df['tel'] = df['tel'].astype(str).apply(self.validate_phone_number)
        self.logger.info("Phone number validation process completed")
        return df

    def validate_phone_number(self, phone: str) -> str:
        phone = phone.strip()
        if len(phone) == 9 and phone[0] in {'5', '6', '7'} and phone.isdigit():
            return '+212' + phone
        elif len(phone) == 12 and phone.startswith('212') and phone[3:].isdigit():
            return '+' + phone
        else:
            self.logger.warning(f"Invalid phone number: {phone}")
            return None
