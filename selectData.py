import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import plotly.graph_objs as gui
import numpy as np
import pandas as pd

app = dash.Dash()

#create data
np.random.seed(10)
x1 = np.linspace(0.1,5,50)
x2 = np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)


#datafradmes
df1 = pd.DataFrame({'x':x1,'y':y})
df2 = pd.DataFrame({'x':x1,'y':y})
df3 = pd.DataFrame({'x':x2,'y':y})

df = pd.concat([df1,df2,df3])

#layoyut
app.layout = html.Div([
    html.Div([    dcc.Graph(id='plot',
              figure={'data':[gui.Scatter(
                  x=df['x'],
                  y=df['y'],
                  mode='markers')],
                  'layout':gui.Layout(title='scatterplot',hovermode='closest')})]
             ,style={'witdth':'30%','display':'inline-block'}),
    html.Div([
        html.H1(id='density',style={'paddingTop':35})],style={'width':'30%','display':'inline-block','verticalAlign':'top'})
])

@app.callback(
    Output('density','children'),
    [Input('plot','selectedData')]
)
def densityCalc(selectedData):
    points = len(selectedData['points'])
    #print(points)
    range_or_lasso_pts = list(selectedData.keys())
    range_or_lasso_pts.remove('points')
    max_x = max(selectedData[range_or_lasso_pts[0]]['x'])
    min_x = min(selectedData[range_or_lasso_pts[0]]['x'])
    max_y = max(selectedData[range_or_lasso_pts[0]]['y'])
    min_y = min(selectedData[range_or_lasso_pts[0]]['y'])
    area = (max_x-min_x)*(max_y-min_y)
    dnsty = points / area
    return 'Density is -> {:.2f}'.format(dnsty)#something....of couurse lol

if __name__ == '__main__':
    app.run_server(host="127.0.0.1",port=1234,debug=True)