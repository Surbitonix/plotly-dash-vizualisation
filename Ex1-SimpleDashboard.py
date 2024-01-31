#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import pandas as pd
import dash
import dash_core_components as core
import dash_html_components as html
import plotly.graph_objs as gui


# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
oldFaithful=pd.read_csv('/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/OldFaithful.csv')
#print(oldFaithful.head())
# Create a Dash layout that contains a Graph component:
app.layout=html.Div([core.Graph(id='oldFaithful-eruptionPower',
                                figure={'data':[gui.Scatter(x=oldFaithful['Y'],
                                                           y=oldFaithful['X'],
                                                           mode='markers',
                                                            marker={
                                                                'size': 12,
                                                                'color': 'rgb(51,204,155)',
                                                                'symbol': 'pentagon',
                                                                'line': {'width': 2}
                                                            }
                                                            )],
                                        'layout':gui.Layout(title='OldFaithful geysers',xaxis={'title':'eruptionPower'})}
),
                    core.Graph(id='oldFaithful-waitingPeriod',
                                figure={'data':[gui.Scatter(x=oldFaithful['X'],
                                                           y=oldFaithful['Y'],
                                                           mode='markers',
                                                            marker={
                                                                'size': 12,
                                                                'color': 'rgb(210,57,155)',
                                                                'symbol': 'pentagon',
                                                                'line': {'width': 2}
                                                            }
                                                            )],
                                        'layout':gui.Layout(title='OldFaithful geysers',xaxis={'title':'waitingPeriod'})}
)
                     ])


if __name__ == '__main__':
    app.run_server()

















# Add the server clause:
