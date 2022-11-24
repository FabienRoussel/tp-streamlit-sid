from pathlib import Path

import pandas as pd
import streamlit as st

from src.utils import get_number_of_cylinders


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
        (used_car_deals_enriched['year'].notna())
    ]
    used_car_deals_enriched['ordometer'] = used_car_deals_enriched['odometer'].astype('int32')
    used_car_deals_enriched['year'] = used_car_deals_enriched['year'].astype('int16')
    used_car_deals_enriched = used_car_deals_enriched.rename(columns={'lat': 'latitude', 'long': 'longitude'})
    used_car_deals_enriched['nb cylinders'] = used_car_deals_enriched['cylinders'].apply(get_number_of_cylinders)
    return used_car_deals_enriched


@st.cache
def get_used_car_deals() -> pd.DataFrame:
    used_car_deals = _load_vehicles()
    used_car_deals = _update_columns_type_and_add_columns(used_car_deals)
    return used_car_deals
