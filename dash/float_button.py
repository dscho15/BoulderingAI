import dash
from dash import dcc, html

button = dcc.Upload(
        id='upload',
        className='upload_float',
        children=[
            html.Button(
                className='btn_float',
                children=['+'],
            )
        ]
    )
