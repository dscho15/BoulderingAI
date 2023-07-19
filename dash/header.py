import dash
from dash import dcc, html

header = html.Div(
    className='header row',
    children=[
        html.Div(
            className='col',
        ),
        html.P(
            className='col',
            children=['BoulderingAI'],
            style={
                'font-size': '2rem',
                'width': 'auto',
                'justify-content': 'center',
                'align-items': 'center',
                'line-height': '4rem',
                },
        ),
        html.Div(
            className='col',
        ),
    ],
)