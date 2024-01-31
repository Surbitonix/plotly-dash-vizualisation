import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd


app = dash.Dash()

nasdaq500 = pd.read_csv('/home/surbitonix97/PycharmProjects/dashboards/codeGoldenSource/Plotly-Dashboards-with-Dash-master/Data/NASDAQcompanylist.csv')
nasdaq500.set_index('Symbol',inplace=True)

options = []

for tick in nasdaq500.index:
    dict001 = {}
    dict001['label'] = str(nasdaq500.loc[tick]['Name'] + ' ' + tick)
    dict001['value'] = tick
    options.append(dict001)

app.layout = html.Div([
                html.H1('Stock Ticker Dashboard'),
            html.Div([
                html.H3('Enter a Ticker', style={'paddingRight':'30px'}),
                dcc.Dropdown(id='my_stock_ticker',
                          options = options,
                          value=[],
                          multi=True
                          )],style={'display':'inline-block','verticalAlign':'top','width':'30%'}),
            html.Div([
                html.H3('StartDate / EndDate'),
                dcc.DatePickerRange(id='datePicker',
                                    min_date_allowed=datetime(2017,1,1),
                                    max_date_allowed=datetime.today(),
                                    start_date=datetime(2020,1,1),
                                    end_date = datetime.today())
            ],style={'display':'inline-block'}),
            html.Div([
                html.Button(id='submit-button',
                            n_clicks=0,
                            children='Submit',
                            style={'fontSize':24,'marginLeft':'30px'})
            ],style={'display':'inline-block'}),
                dcc.Graph(id='stockGraph',
                          figure={'data':[{'x':[1,2],'y':[3,1]}],
                                  'layout':{'title':'Default Title'},
                                  })
])

#state is used to support the SUBMIT button
@app.callback(
    Output('stockGraph','figure'),
    [Input('submit-button','n_clicks')],
    [State('my_stock_ticker','value'),
        State('datePicker','start_date'),
        State('datePicker','end_date')]
    )

def updateGraph(n_clicks,stockTicker,start_date,end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10],'%Y-%m-%d')

    traces = []
    for tick in stockTicker:
        df = web.get_data_tiingo(tick,start,end,api_key='3654d3e03f88fcc35e009b313ebe8053ddc88876')
        traces.append({'x':df.index.get_level_values(1),'y':df['close'],'name': tick})

    fig = {'data':traces,
        'layout': {'title':stockTicker}
    }


    return fig

if __name__ == '__main__':
    app.run_server()