import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output,State

app = dash.Dash()
app.layout = html.Div([
    dcc.Input(id='inputNumber',value=1,style={'fontSize':24}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='submit request...',
                style={'fontSize':20}),
    html.H1(id='outputNumber')
])

@app.callback(Output('outputNumber','children'),
              [Input('submit-button','n_clicks')],
              [State('inputNumber','value')])
def outputNumber(clikx,inputText):
    return " input value is -> \"{}\" || button was clicked  -> {} times".format(inputText,clikx)

if __name__ == '__main__':
    app.run_server()