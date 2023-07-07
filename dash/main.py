import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import float_button

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
    className='container',
    children=[
        float_button.button,
        html.Img(id='image', width="100%")
    ]
)
app.clientside_callback(
    """
    function(contents) {
        // document.write(contents)
        if (contents === undefined) {
            return "";
        } else {
            return contents;
        }
    }
    """,
    Output('image', 'src'),
    Input('upload', 'contents')
)


if __name__ == "__main__":
    app.run_server(debug=True, host="192.168.0.113")