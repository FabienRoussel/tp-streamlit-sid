import pandas as pd
import plotly.express as px
import streamlit as st


def display_charts(df_used_car_deals: pd.DataFrame, filter_by_car_types: list[str]) -> None:
    expander_col_1, expander_col_2 = st.columns((5, 1))
    with expander_col_1:
        with st.expander('Voir les données du dataset'):
            # filtered_dataframe = df_used_car_deals[df_used_car_deals['Turnover'] > 0]
            filtered_dataframe = df_used_car_deals[
                ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel',
                 'odometer', 'transmission', 'drive', 'type', 'size', 'paint_color', 'description',
                 'county', 'region', 'state', 'latitude', 'longitude', 'posting_date']
            ]
            st.dataframe(filtered_dataframe.head(1000))
    with expander_col_2:
        st.download_button(label="Télécharger", data=df_used_car_deals.to_csv().encode('utf-8'),
                           file_name=f"{str(filter_by_car_types)}.csv", mime='text/csv')

    with st.container():
        st.subheader('CA par mois')
        # _bar_chart_turnover_by_month(df_cutting_training_only, filter_by_fy)
