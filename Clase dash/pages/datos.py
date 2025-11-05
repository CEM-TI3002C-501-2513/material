import asyncio
import dash
import httpx
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dash import html, dash_table, dcc

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def get_all_data():
    API_URLS = {
        "primary_types1": "http://localhost:8000/top_primary_types",
        "primary_types2": "http://localhost:8000/top_primary_types",
    }
    tasks = [fetch_data(url) for url in API_URLS.values()]
    results = await asyncio.gather(*tasks)
    return dict(zip(API_URLS.keys(), results))

dash.register_page(
    __name__,
    path="/datos",
    title="Datos",
    name="datos"
)

async def layout():
    data = await get_all_data()
    df1 = pd.DataFrame(data["primary_types1"])
    df2 = pd.DataFrame(data["primary_types2"])
    return html.Div(
        children=[
            html.H1(
                children="Página de Datos",
                className="text-3xl font-bold mb-4"
            ),
            html.H2(
                children="Ejemplo de tabla con dash_table",
                className="text-2xl font-semibold mb-2"
            ),
            dash_table.DataTable(data=df1.to_dict("records"), page_size=10),
            html.H2(
                children="Ejemplo de tabla con dash_ag_grid",
                className="text-2xl font-semibold my-2"
            ),
            dag.AgGrid(
                rowData=df2.to_dict("records"),
                columnDefs=[{"field": col, "sortable": True, "filter": True} for col in df2.columns],
                columnSize="responsiveSizeToFit",
                dashGridOptions={"pagination": True, "paginationPageSize": 10}
            ),
            html.H2(
                children="Ejemplo de gráfico con Plotly",
                className="text-2xl font-semibold my-2"
            ),
            dcc.Graph(figure=px.bar(df1, 
                                    x="primary_type", 
                                    y="count", 
                                    title="Conteo por Tipo Primario"))
        ]
    )