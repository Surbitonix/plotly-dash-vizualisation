import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

#slider = dcc.Slider(min=-20,max=20,step=1,value=5)
app.layout=html.Div([
    dcc.RangeSlider(
            min=-20,
            max=20,
            step=1,
            marks={i:str(i) for i in range(-20,20)},
            value=[-1, 2],
            id='range-slider'),
    html.H1(id='outputSlider')
    ])


@app.callback(
    Output('outputSlider','children'),
    [Input('range-slider','value')])
def rangeCalculator(x):
    return x[0] * x[1]


if __name__ == '__main__':
    app.run_server(debug=True)