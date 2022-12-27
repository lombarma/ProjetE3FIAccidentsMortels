# TODO : affichage des accidents sur la carte
# TODO : bar chart des accidents par mois sur 2021 -- Fait
# TODO : pie chart des accidents en fonction du sexe des victimes (1 = homme, 2 = femme) -- Fait
# TODO : bar chart des accidents en fonction de la gravité de l'accident -- Fait
# TODO : barchart nombre d'accidents par jour de la semaine
# TODO : graphique des accidents en fonction de la catégorie de véhicule impliquée -- Fait
# TODO : il faut un histogramme

import dash
from dash import dcc
from dash import html
import plotly.express as px

from script import camembert_accident_par_sexe as cas
from script import bar_chart_accident_par_gravite as bcag
from script import bar_chart_accidents_par_mois as bcapm
from script import categorie_vehicule_impliquee as cvi


def dash_project():
    # Figures
    fig_camembert_cas = cas.pie_chart_accident_by_sex()
    fig_bar_chart_bcag = bcag.bar_chart_accident_by_gravity()
    fig_bar_chart_bcapm = bcapm.bar_char_accidents_by_month()
    fig_graph_cvi = cvi.chart_vehicle_categories()

    # Update
    fig_camembert_cas.update_layout(paper_bgcolor="#132742", plot_bgcolor="#132742", font_color="#FFFFFF")
    fig_bar_chart_bcag.update_layout(paper_bgcolor="#132742", plot_bgcolor="#132742", font_color="#FFFFFF")
    fig_bar_chart_bcapm.update_layout(paper_bgcolor="#132742", plot_bgcolor="#132742", font_color="#FFFFFF")
    fig_graph_cvi.update_layout(paper_bgcolor="#132742", plot_bgcolor="#132742", font_color="#FFFFFF")

    # Dashboard
    app = dash.Dash()
    app.layout = html.Div(style={"backgroundColor": '#132742', "color": "#FFFFFF"}, children=[
        html.H1(children=f'Les accidents de la route en France en 2021',
                style={'textAlign': 'center', 'color': '#FFFFF'}),

        html.Div(style={"display": "inline-block", "width": "45%", "border": "2px solid white", "margin": "20px"},
                 children=[
                     dcc.Graph(
                         id='camembert accident par sexe',
                         figure=fig_camembert_cas
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "45%", "border": "2px solid white", "margin": "20px"},
                 children=[
                     dcc.Graph(
                         id='bar chart accident par gravite',
                         figure=fig_bar_chart_bcag
                     )
                 ]
                 ),
        html.Div(children=[
                     dcc.Graph(
                         id='graph categorie vehicule impliquee',
                         figure=fig_graph_cvi
                     )
                 ]
                 ),
        html.Div(children=[
            dcc.Graph(
                id='bar chart accidents par mois',
                figure=fig_bar_chart_bcapm
            )
        ]
        )
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    dash_project()
