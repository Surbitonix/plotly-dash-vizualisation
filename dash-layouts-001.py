import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
#set up the style
colors={'background':'#111111','text':'#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('hello oberrieden',style={'textAlign':'center',
                                      'color':colors['text']}),
    dcc.Graph(id='example',figure={'data':[
                                            {'x':[1,2,3],'y':[4,5,6],'type':'bar','name':'SanFran'},
                                            {'x':[1,2,3],'y':[7,15,26],'type':'bar','name':'NYC'}],
                                    'layout':{'title':'BarPlots',
                                              'plot_bgcolor':colors['background'],
                                              'paper_bgcolor':colors['background'],
                                              'font':{'color':colors['text']}}
    })],

    style={'background_color':colors['background']})

if __name__== '__main__':
    app.run_server()