import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as gui
import numpy as np

app = dash.Dash()

#create data
np.random.seed(47)
rand_x=np.random.randint(1,101,100)
rand_y=np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                       figure={'data':[gui.Scatter(
                                                x=rand_x,
                                                y=rand_y,
                                                mode='markers',
                                                marker={
                                                    'size':12,
                                                    'color': 'rgb(51,204,155)',
                                                    'symbol':'pentagon',
                                                    'line':{'width': 2}
                                                        }
                                                )],
                                'layout':gui.Layout(title='test scatterplot',xaxis={'title':'dataX'})})
                       ,
                      dcc.Graph(id='scatterplot2',
                                figure={'data': [gui.Scatter(
                                    x=rand_x,
                                    y=rand_y,
                                    mode='markers',
                                    marker={
                                        'size': 12,
                                        'color': 'rgb(200,55,155)',
                                        'symbol': 'pentagon',
                                        'line': {'width': 2}
                                    }
                                )],
                                    'layout': gui.Layout(title='2nd plot', xaxis={'title': 'dataX'})})

                      ])


if __name__ == '__main__':
    app.run_server()