# TODO : pie chart accidents by age (ou tranche d'age)
# TODO : mise en page
# TODO : README

import dash
from dash import dcc
from dash import html

from script import pie_chart_accident_by_sex as cas
from script import bar_chart_accidents_per_gravity as bcag
from script import bar_chart_accidents_per_month as bcapm
from script import category_vehicule_involved as cvi
from script import map_accident_distribution as mra
from script import hist_accidents_per_hours as haph


def dash_project():
    # Figures
    fig_camembert_cas = cas.pie_chart_accident_by_sex()
    fig_bar_chart_bcag = bcag.bar_chart_accident_by_gravity()
    fig_bar_chart_bcapm = bcapm.bar_char_accidents_by_month()
    fig_graph_cvi = cvi.chart_vehicle_categories()
    map_mra = mra.accident_distribution_map()
    fig_hist_haph = haph.histogram_accidents_per_hours()

    # Update
    fig_camembert_cas.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    fig_bar_chart_bcag.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    fig_graph_cvi.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    fig_bar_chart_bcapm.update_layout(paper_bgcolor="#132742", plot_bgcolor="#132742", font_color="#FFFFFF")
    fig_hist_haph.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")

    # Dashboard
    app = dash.Dash(__name__)
    app.layout = html.Div(style={"backgroundColor": '#132742', "color": "#FFFFFF"}, children=[
        html.H1(children=f'Les accidents de la route en France en 2021',
                style={'textAlign': 'center', 'color': '#FFFFF'}),

        html.Div(style={"display": "inline-block", "width": "45%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='camembert accident par sexe',
                         figure=fig_camembert_cas
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "45%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='bar chart accident par gravite',
                         figure=fig_bar_chart_bcag
                     )
                 ]
                 ),
        html.Div(style={"margin": "20px", "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='graph categorie vehicule impliquee',
                         figure=fig_graph_cvi
                     )
                 ]
                 ),
        html.Div(
            children=[
                dcc.Graph(
                    id='bar chart accidents par mois',
                    figure=fig_bar_chart_bcapm
                )
            ]
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id='histogram accidents per hours',
                    figure=fig_hist_haph
                )
            ]
        ),
        html.Div(
            children=[
                html.Iframe(
                    id='map',
                    srcDoc=map_mra.get_root().render(),
                    style={'width': '90%', 'height': '800px', 'margin': 'auto', 'display': 'block'}
                )
            ]
        )
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    dash_project()
