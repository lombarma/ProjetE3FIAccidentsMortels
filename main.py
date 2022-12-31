import dash
from dash import dcc
from dash import html

from script import pie_chart_accident_by_sex as cas
from script import bar_chart_accidents_per_gravity as bcag
from script import bar_chart_accidents_per_month as bcapm
from script import category_vehicle_involved as cvi
from script import map_accident_distribution as mra
from script import hist_accidents_per_hours as haph
from script import pie_chart_accident_by_ages as pca


def dash_project():
    # Figures
    pie_chart_by_sex = cas.pie_chart_accident_by_sex()
    bar_chart_per_gravity = bcag.bar_chart_accident_by_gravity()
    bar_chart_by_month = bcapm.bar_char_accidents_by_month()
    graph_category = cvi.scatter_vehicle_categories()
    map_mra = mra.accident_distribution_map()
    hist_per_hours = haph.histogram_accidents_per_hours()
    pie_chart_by_ages = pca.pie_chart_accident_by_ages()

    # Update
    pie_chart_by_sex.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    bar_chart_per_gravity.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    graph_category.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    bar_chart_by_month.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    hist_per_hours.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")
    pie_chart_by_ages.update_layout(paper_bgcolor="#172F50", plot_bgcolor="#172F50", font_color="#FFFFFF")

    # Dashboard
    app = dash.Dash(__name__)
    app.layout = html.Div(style={"backgroundColor": '#132742', "color": "#FFFFFF", "textAlign": "center"}, children=[
        html.H1(children='Les accidents de la route en France en 2021',
                style={'textAlign': 'center', 'color': '#FFFFF', "padding": "20px"}),

        html.Div(style={"display": "inline-block", "width": "30%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='pie chart accidents per sexe',
                         figure=pie_chart_by_sex
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "30%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='bar chart accidents per gravity',
                         figure=bar_chart_per_gravity
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "30%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='pie chart accidents per ages',
                         figure=pie_chart_by_ages
                     )
                 ]
                 ),
        html.Div(style={"margin": "20px", "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='graph category vehicle involved',
                         figure=graph_category
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "45%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='bar chart accidents per month',
                         figure=bar_chart_by_month
                     )
                 ]
                 ),
        html.Div(style={"display": "inline-block", "width": "45%", "margin": "20px",
                        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.4)"},
                 children=[
                     dcc.Graph(
                         id='histogram accidents per hours',
                         figure=hist_per_hours
                     )
                 ]
                 ),
        html.H2(children='Carte des accidents de la route en France en 2021',
                style={'textAlign': 'center', 'color': '#FFFFF'}),
        html.Div(
            children=[
                html.Iframe(
                    id='map',
                    srcDoc=map_mra.get_root().render(),
                    style={'width': '80%', 'height': '800px', 'margin': 'auto', 'display': 'block'}
                )
            ]
        )
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    dash_project()
