import asyncio
import dash
import httpx
import pandas as pd
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def get_all_data():
    API_URLS = {
        "wards": "http://localhost:8000/wards",
    }
    tasks = [fetch_data(url) for url in API_URLS.values()]
    results = await asyncio.gather(*tasks)
    return dict(zip(API_URLS.keys(), results))

dash.register_page(
    __name__,
    path="/prediccion",
    title="Predicción de impacto de crímenes",
    name="prediccion"
)

async def layout():
    data = await get_all_data()
    return html.Div(
        children=[
            html.H1(
                children="Predicción de impacto de crímenes",
                className="text-3xl font-bold mb-4"
            ),
            html.Div(
                className="bg-sky-50 p-4 rounded-lg",
                children=[
                    html.Label(
                        className="block text-lg font-medium mb-2",
                        children="Seleccione el ward"
                    ),
                    dcc.Dropdown(
                        id="ward-dropdown",
                        options=[{"label": f"Ward {i}", "value": f"Ward_{i}"} for i in data["wards"]]
                    ),
                    html.Label(
                        className="block text-lg font-medium mb-2",
                        children="Seleccione la fecha"
                    ),
                    dcc.DatePickerSingle(
                        id="date-picker"
                    ),
                    html.Label(
                        className="block text-lg font-medium mb-2",
                        children="Seleccione la hora"
                    ),
                    dcc.Dropdown(
                        id="hour-dropdown",
                        options=[{"label": f"{i}:00", "value": i} for i in range(24)]
                    ),
                    html.Button(
                        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded",
                        children="Hacer predicción",
                        id="submit-prediction-button"
                    )
                ]
            ),
            html.Div(id="prediction-results-output")
        ]
    )
    
@callback(
    Output("prediction-results-output", "children"),
    Input("submit-prediction-button", "n_clicks"),
    State("ward-dropdown", "value"),
    State("date-picker", "date"),
    State("hour-dropdown", "value"),
    prevent_initial_call=True
)
async def make_prediction(n_clicks, ward, date, hour):
    if n_clicks:
        if not ward or not date or hour is None:
            return html.Div(
                className="text-red-500 mt-4",
                children="Debes llenar todos los campos para hacer tu predicción."
            )
        try:
            fecha = pd.to_datetime(date)
            payload = {
                "ward": ward,
                "month": fecha.month_name(),
                "day_of_week": fecha.day_name(),
                "hour": hour,
            }
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:8000/predict_impact", json=payload)
                probabilities = response.json()
                
                return html.Div(
                    className="mt-4",
                    children=[
                        html.H2(
                            className="text-2xl font-semibold mb-2",
                            children="Resultados de la predicción de impacto"
                        ),
                        html.Ul(
                            children=[
                                html.Li(
                                    className="mb-1 text-lg bg-green-100 p-2 rounded",
                                    children=f"Bajo impacto: {probabilities['low_impact_probability']*100:.2f}%"
                                ),
                                html.Li(
                                    className="mb-1 text-lg bg-yellow-100 p-2 rounded",
                                    children=f"Medio impacto: {probabilities['medium_impact_probability']*100:.2f}%"
                                ),
                                html.Li(
                                    className="mb-1 text-lg bg-red-100 p-2 rounded",
                                    children=f"Alto impacto: {probabilities['high_impact_probability']*100:.2f}%"
                                ),
                            ]
                        )
                    ]
                )
        except Exception as e:
            return html.Div(
                className="text-red-500 mt-4",
                children=f"Ocurrió un error al hacer la predicción: {str(e)}"
            )                