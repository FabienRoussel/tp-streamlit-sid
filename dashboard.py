import streamlit as st

import src.data_loading
from src.filters import filter_car_deals_by_car_type
from src.charts import display_charts
from src.utils import get_car_type

st.set_page_config(layout="wide")

st.title('TP streamlit')

# Data loading
df_used_car_deals = src.data_loading.get_used_car_deals()
car_types = get_car_type(df_used_car_deals)

st.sidebar.success('TEST')
# Filters
filter_by_car_types = st.sidebar.multiselect(
    'Selectionnez le type de véhicules',
    car_types,
    default=['sedan'])

df_used_car_deals_for_type = src.filters.filter_car_deals_by_car_type(df_used_car_deals, filter_by_car_types)

# Figures and charts
if not filter_by_car_types:
    st.subheader("Aucune catégorie de voitures selectionnée, sélectionnez une catégorie minumum.")
else:
    display_charts(df_used_car_deals_for_type, filter_by_car_types)
    assert 1 == 1
