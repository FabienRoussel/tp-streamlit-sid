import pandas as pd


def filter_car_deals_by_car_type(df_used_car_deals: pd.DataFrame, filter_by_car_type: int) -> pd.DataFrame:
    return df_used_car_deals[df_used_car_deals['type'].isin(filter_by_car_type)]
