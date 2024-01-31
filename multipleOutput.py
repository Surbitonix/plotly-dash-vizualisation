import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import base64


df = pd.read_csv('/home/surbitonix97/PycharmProjects/interactive-dashboards/dashboards/dash/wheels.csv')
#print(df.head())

def bold_text(text):
    start_bold = '\033[0m'
    end_bold = '\033[0m'
    return start_bold + text + end_bold

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label':i,'value':i} for i in df['wheels'].unique()],
                   value=1
                   ),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                   options=[{'label':x,'value':x} for x in df['color'].unique()],
                   value='blue'
                   ),
    html.Div(id='colors-output'),
    html.Img(id='display-image',src='children',height=300)
], style={'font-family':'helvetica','fontSize':18})


@app.callback(Output('wheels-output','children'),
              [Input('wheels','value')])
def callback_a(wheels_chosen):
    return "you chose ---> {}".format(wheels_chosen)

@app.callback(Output('colors-output','children'),
              [Input('colors','value')])
def callback_b(color_chosen):
    return 'you chose ---> {}'.format(color_chosen)

@app.callback(Output('display-image','children'),
              [Input('wheels','value'),Input('colors','value')])
def callback_img(wheel,color):
    path = '/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/Images/'
    return encode_image((path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0]))



if __name__ == '__main__':
    app.run_server()