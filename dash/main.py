import sys
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import float_button
import header
import base64
from PIL import Image
from flask import request
import datetime



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

pil_image = Image.open('images/placeholder.jpg')
# Rotate the image by 90 degrees
#pil_image = pil_image.rotate(270, expand=True)

app.layout = html.Div(
    className='container',
    children=[
        header.header,
        html.Div(
            style={
                'height': '80vh',
            },
            children=[
                html.Img(
                    src=pil_image, id='image',
                    style={
                        'width': '100vw',
                        }
                    ),
            ],
        ), 
        float_button.button,
        html.Div(id='dummy'),
    ],
)

def save_uploaded_file(contents, filename):
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    with open('images/'+filename, 'wb') as f:
        f.write(decoded)

@app.callback(
    Output('image', 'src'),
    Input('upload', 'contents'),
    State('upload', 'filename'),
    prevent_initial_call=True,
)
def update_output(contents, filename):
    if contents is not None:
        # Save the file to the server
        save_uploaded_file(contents, filename)
        return contents  # Return the contents of the uploaded image
    else:
        return ''
    
@app.callback(
        Output('dummy', 'children'),
        Input('dummy', 'children')
)
def get_ip(value):
    # Write to log.txt request.remote_addr and timestamp
    with open('log.txt', 'a') as f:
        f.write(request.remote_addr + ', ' + str(datetime.datetime.now()) + '\n')
    dash.no_update


if __name__ == "__main__":
    argv = sys.argv
    app.run_server(debug=False, host=argv[1], port=8050)