import pandas as pd


def get_car_type(df_used_car_deals: pd.DataFrame) -> list[str]:
    return df_used_car_deals['type'].unique()


def get_number_of_cylinders(cylinders: str) -> int:
    # TODO récupérer le nombre de cylindres, attention aux valeurs nulles !
    return 0
