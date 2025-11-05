import dash
from dash import html

dash.register_page(
    __name__,
    path="/",
    title="Inicio",
    name="index"
)

async def layout():
    return html.Div(
        children=[
            html.H1(
                children="Página de Inicio",
                className="text-3xl font-bold mb-4"
            ),
            html.P(
                children="Página de inicio del sitio de prueba de Dash",
                className="text-lg"
            ),
            html.Img(
                src=dash.get_asset_url("images/pexels-brandon-retratos-768594541-34563097.jpg"),
                className="w-1/2 mx-auto"
            )
        ]
    )