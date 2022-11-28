import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils import get_mean_price_by_age_of_car


def _histogram_odometer(df_used_car_deals: pd.DataFrame) -> None:
    # TODO afficher un histogram du kilométrage des annonces
    fig = px.histogram(df_used_car_deals, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    pass


def _example_bar_chart_mean_price_of_sold_car_by_age_of_car(df_used_car_deals: pd.DataFrame) -> None:
    # Voici un exemple de graphes affichant le prix moyen des voitures selon leur age.

    df_mean_price_by_age_of_car = get_mean_price_by_age_of_car(df_used_car_deals)
    fig = px.bar(df_mean_price_by_age_of_car, x='age', y='price')
    st.plotly_chart(fig, use_container_width=True)
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
        # TODO question 3
        st.subheader('Prix moyen des véhicules selon leur age')
        _example_bar_chart_mean_price_of_sold_car_by_age_of_car(df_used_car_deals)

    with st.container():
        # TODO question 3
        st.subheader('Histogramme du kilométrage des annonces')
        _histogram_odometer(df_used_car_deals)

    with st.container():
        # TODO question 4
        st.subheader('Histogramme des années des annonces')

    with st.container():
        # TODO question 5.1
        st.subheader('Couleurs les plus populaires')

    with st.container():
        # TODO question 5.2
        st.subheader('Marques les plus populaires')

    with st.container():
        # TODO question 6
        st.subheader('Proportion des carburants par catégorie de véhicule')

    with st.container():
        # TODO question 7
        st.subheader('Annonces de voitures d\'occasion aux des Etats Unis')

    with st.container():
        # TODO question 8
        st.subheader('Évolution du prix des annonces de véhicules d\'occasion aux des Etats Unis au cours du temps')
