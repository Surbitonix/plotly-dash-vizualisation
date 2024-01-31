import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as gui
import  pandas as pd
import json
import base64

app = dash.Dash()

dataframe = pd.read_csv('/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/wheels.csv')
#print(dataframe.head())

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
            html.Div(dcc.Graph(id='wheels-plot',
                               figure={'data':[gui.Scatter(
                                            x=dataframe['color'],
                                            y=dataframe['wheels'],
                                            dy= 1,
                                            mode='markers',
                                            marker={'size':15}
                               )],
            'layout':gui.Layout(title='madness',hovermode='closest')
            }
        ),style={'witdth':'30%','float':'left'}),
    html.Div(html.Pre(id='hover-data',style={'paddingTop':35}))
             #Img(id='hover-data',src='children',height=300,style={'paddingTop':35}))
             #,style={'width':'30%'})
])

@app.callback(Output('hover-data','children'),
              [Input('wheels-plot','clickData')])
def callback_image(hoverdata):
    return json.dumps(hoverdata,indent=2)
    wheel = hoverdata['points'][0]['y']
    color = hoverdata['points'][0]['x']
    path = '/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/Images/'
    #return encode_image((path + dataframe[(dataframe['wheels'] == wheel) & (dataframe['color'] == color)]['image'].values[0]))

if __name__ == '__main__':
    app.run_server(debug=True)