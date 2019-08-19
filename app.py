import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "National League Team Win Totals"
mytitle = "Win totals"
x_values = ['1990', '1991', '1992', '1993', '1994', '1995']
y1_values = [65, 94, 98, 104, 68, 90]
y2_values = [77, 77, 78, 84, 49, 73]
y3_values = [91, 74, 90, 73, 66, 85]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'ATL'
name2 = 'CHC'
name3 = 'CIN'
tabtitle = 'baseball'
sourceurl = 'https://www.baseball-reference.com'
githublink = 'https://github.com/szilviaaltorjai/dash-linechart-example'
notes = 'ATL: Atlanta Braves, Milwaukee Braves, Boston Bees, Boston Braves, Boston Rustlers, Boston Doves, Boston Beaneaters, Boston Red Stockings; CHC: Chicago Cubs, Chicago Orphans, Chicago Colts, Chicago White Stockings; CIN: Cincinnati Redlegs, Cincinnati Reds,Cincinnati Red Stockings'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
