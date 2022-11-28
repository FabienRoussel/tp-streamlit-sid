import pandas as pd
import plotly.express as px
import streamlit as st


def _histogram_odometer(df_used_car_deals: pd.DataFrame) -> None:
    # TODO afficher un histogram du kilométrage des annonces
    fig = px.histogram(df_used_car_deals, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    pass


def _bar_chart_turnover_by_month(df_used_car_deals: pd.DataFrame, fiscal_year: int) -> None:
    #df_turnover_by_month_and_leagues = get_turnover_by_month_and_league(df_cutting_training)
    #fig1 = px.bar(df_turnover_by_month_and_leagues, x='Month', y='Turnover', color='League')
    #fig1.layout.xaxis.tickvals = pd.date_range(f'{fiscal_year - 1}-09-1', f'{fiscal_year}-08-01', freq='MS')
    #fig1.layout.xaxis.tickformat = '%b %Y'
    #st.plotly_chart(fig1, use_container_width=True)
    pass


def display_charts(df_used_car_deals: pd.DataFrame, filter_by_car_types: list[str]) -> None:
    expander_col_1, expander_col_2 = st.columns((5, 1))
    with expander_col_1:
        with st.expander('Voir les données du dataset'):
            filtered_dataframe = df_used_car_deals[
                ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'nb_cylinders',
                 'fuel', 'odometer', 'transmission', 'drive', 'type', 'size', 'paint_color',
                 'description', 'region', 'state', 'latitude', 'longitude', 'posting_date']
            ]
            st.dataframe(filtered_dataframe.head(1000))
    with expander_col_2:
        st.download_button(label="Télécharger", data=df_used_car_deals.to_csv().encode('utf-8'),
                           file_name=f"{str(filter_by_car_types)}.csv", mime='text/csv')

    with st.container():
        # TODO
        st.subheader('Histogramme du kilométrage des annonces')
        _histogram_odometer(df_used_car_deals)

    with st.container():
        # TODO
        st.subheader('Histogramme du kilométrage des annonces')
        #_histogram_odometer(df_used_car_deals)

    with st.container():
        # TODO
        st.subheader('Histogramme du kilométrage des annonces')
        #_histogram_odometer(df_used_car_deals)

    with st.container():
        # TODO
        st.subheader('Histogramme du kilométrage des annonces')
        #_histogram_odometer(df_used_car_deals)
