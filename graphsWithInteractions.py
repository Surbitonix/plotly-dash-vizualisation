import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
import plotly.graph_objs as gui
import pandas as pd
from numpy import random

app = dash.Dash()
df = pd.read_csv('/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')
df['year'] = random.randint(-4,5,len(df))*0.1 + df['model_year']

app.layout = html.Div([
                html.Div([dcc.Graph(id='mpg-scatter',
                    figure={
                        'data':[gui.Scatter(
                                x=df['year']+1900,
                                y=df['mpg'],
                                text=df['name'],
                                hoverinfo='text'+'y'+'x',
                                mode='markers'
                    )],
                        'layout': gui.Layout(title='MPG Data',
                                       xaxis={'title':'Model Year'},
                                       yaxis={'title':'MPG'},
                                       hovermode='closest')
                            }
                        )],style={'width':'50%','display':'inline-block'}),
                html.Div([
                    dcc.Graph(id='mpg_line',
                              figure={'data':[gui.Scatter(x=[0,1],y=[0,1],mode='lines')],
                                      'layout':gui.Layout(title='accelaration',margin={'l':0})})
                ],style={'width':'20%','height':'50%','display':'inline-block'}),
            html.Div([
                dcc.Markdown(id='mpg-stats')
            ],style={'width':'20%','height':'50%','display':'inline-block'})

])

@app.callback(Output('mpg_line','figure'),
              [Input('mpg-scatter','hoverData')])
def callback_graph(hoverData):
    #find index of vehicle
    car_index = hoverData['points'][0]['pointIndex']
    figure = {'data':[gui.Scatter(x=[0,1],
                                  y=[0,60 / df.iloc[car_index]['acceleration']],
                                  mode='lines',
                                  line={'width':df.iloc[car_index]['cylinders']*2}
                                  )
                      ],
              'layout':gui.Layout(title=df.iloc[car_index]['name'],
                                  xaxis={'visible':False},
                                  yaxis={'visible':False,'range':[0,60/df['acceleration'].min()]},
                                  margin={'l':0},
                                  height=300
                                  )}
    return  figure

@app.callback(Output('mpg-stats','children'),
              [Input('mpg-scatter','hoverData')])
def callback_stats(hoverData):
    car_index = hoverData['points'][0]['pointIndex']
    stats = """
        {} cylinders
        {}cc displacement
        0 to 60mph in {} seconds
    """ .format(df.iloc[car_index]['cylinders'],
                df.iloc[car_index]['displacement'],
                df.iloc[car_index]['acceleration']
                )

    return stats


if __name__ == '__main__':
    app.run_server()