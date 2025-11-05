import dash
from dash import Dash, html, dcc

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}
]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    title="Ejemplo de sitio en Dash",
    update_title="Cargando...",
    use_async=True,
    use_pages=True
)

header = html.Header(
    children=[
        dcc.Link(
            children="Inicio",
            href="/",
            className="font-bold text-xl"
        ),
        dcc.Link(
            children="Datos",
            href="/datos",
            className="font-bold text-xl ml-4"
        ),
        ],
    className="p-4 bg-blue-500 text-white text-center"
)

footer = html.Footer(
    children="© 2024 Mi Sitio Dash",
    className="p-4 bg-gray-200 text-center"
)

app.layout = html.Div(
    children = [
        header,
        dash.page_container,
        footer
    ]
)

if __name__ == "__main__":
    app.run(debug=True)