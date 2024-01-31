import dash
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div(['This is the outer most DIV!!!',
                        html.Div('this is inner div 001',
                                style={'color':'red','border':'2px red solid'}),
                       html.Div(['this inner Div - 002'],
                                style={'color':'blue','border':'2px blue solid'})],
                        style={'color':'green','border':'2px green solid'}
                      )


if __name__ == '__main__':
    app.run_server(port=1234)