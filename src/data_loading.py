from pathlib import Path

import pandas as pd
import streamlit as st

from src.utils import get_number_of_cylinders, drop_vehicules_with_more_than_300_000_kilometers


@st.cache
def _load_vehicles() -> pd.DataFrame:
    data_path = Path() / 'data/vehicles.csv'
    data = pd.read_csv(data_path, sep=',', encoding="ISO-8859-1")
    return data


@st.cache
def _update_columns_type_and_add_columns(used_car_deals: pd.DataFrame) -> pd.DataFrame:
    used_car_deals_enriched = used_car_deals.copy()
    used_car_deals_enriched = used_car_deals_enriched[
        (used_car_deals_enriched['odometer'].notna()) &
        (used_car_deals_enriched['year'].notna()) &
        (used_car_deals_enriched['manufacturer'].notna()) &
        (used_car_deals_enriched['lat'].notna()) &
        (used_car_deals_enriched['long'].notna()) &
        (used_car_deals_enriched['posting_date'].notna()) &
        (used_car_deals_enriched['price'] > 0)
    ]
    used_car_deals_enriched['ordometer'] = used_car_deals_enriched['odometer'].astype('int32')
    used_car_deals_enriched['year'] = used_car_deals_enriched['year'].astype('int16')
    used_car_deals_enriched.drop(columns=['county'])
    used_car_deals_enriched = used_car_deals_enriched.rename(columns={'lat': 'latitude', 'long': 'longitude'})

    # TODO implémenter les filter en dessous, les fonctions sont dans utils.py
    used_car_deals_enriched['nb_cylinders'] = used_car_deals_enriched['cylinders'].apply(get_number_of_cylinders)
    used_car_deals_enriched = drop_vehicules_with_more_than_300_000_kilometers(used_car_deals_enriched)

    return used_car_deals_enriched


@st.cache
def get_used_car_deals() -> pd.DataFrame:
    used_car_deals = _load_vehicles()
    used_car_deals = _update_columns_type_and_add_columns(used_car_deals)
    return used_car_deals
