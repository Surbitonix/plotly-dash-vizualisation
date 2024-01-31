import dash
import  dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as gui
import pandas as pd


df = pd.read_csv('/home/surbitonix97/PycharmProjects/interactive-dashboards/dashboards/dash/mpg.csv')

#print(read_csv.head())

app = dash.Dash()
features=df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label':i,'value':i} for i in features],
                     value='displacement')
    ],style={'width':'50%','display':'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label':i,'value':i} for i in features],
                     value='mpg')
    ],style={'width':'50%','display':'inline-block'}),
    dcc.Graph(id='feature-graphic')
],style={'padding':'20'})

@app.callback(Output('feature-graphic','figure'),
              [Input('xaxis','value'),
              Input('yaxis','value')])
def updateGraph(x_axisName, y_axisName):
    return {'data':[gui.Scatter(x=df[x_axisName],
                                y=df[y_axisName],
                                text=df['name'],
                                mode='markers',
                                marker={'size':15,'opacity':0.5,'line':{'width':0.5,'color':'white'}})]
            ,'layout':gui.Layout(title='Car MPG range',
                                 xaxis={'title':x_axisName},
                                 yaxis={'title':y_axisName},
                                 hovermode='closest')}



if __name__ == '__main__':
    app.run_server()