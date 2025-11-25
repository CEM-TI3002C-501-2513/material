import asyncio
import dash
import dash_svg
import httpx
import pandas as pd
from dash import html, dcc, callback, Output, Input, State
from datetime import date, datetime

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def get_all_data(API_URLS):
    tasks = [fetch_data(url) for url in API_URLS.values()]
    results = await asyncio.gather(*tasks)
    return dict(zip(API_URLS.keys(), results))

dash.register_page(
    __name__,
    path="/prediccion",
    title="Predicción de Criminalidad",
    name="prediccion",
)

async def layout():
    API_URLS = {
        "wards": "http://localhost:8000/wards",
    }
    data = await get_all_data(API_URLS)
    return html.Div(
    children=[
        html.Section(
            className="bg-slate-800 py-16 text-white",
            children=[
                html.Div(
                    className="mx-auto px-6 container",
                    children=[
                        html.Div(
                            className="max-w-4xl",
                            children=[
                                html.H1(
                                    className="mb-4 font-bold text-4xl",
                                    children=["Predicción de Criminalidad"],
                                ),
                                html.P(
                                    className="text-slate-200 text-xl leading-relaxed",
                                    children=[
                                        "Utiliza nuestro modelo de inteligencia artificial para predecir la probabilidad de crímenes en una zona específica de Chicago según la fecha y hora seleccionadas."
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            ],
        ),
        html.Main(
            className="mx-auto px-6 py-12 container",
            children=[
                html.Div(
                    className="gap-8 grid lg:grid-cols-3",
                    children=[
                        html.Div(
                            className="lg:col-span-1",
                            children=[
                                html.Div(
                                    className="top-24 sticky bg-white p-8 border border-slate-200",
                                    children=[
                                        html.H2(
                                            className="mb-6 font-bold text-slate-900 text-2xl",
                                            children=["Parámetros de Predicción"],
                                        ),
                                        html.Div(
                                            className="space-y-6",
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="block mb-2 font-semibold text-slate-700 text-sm",
                                                            children=["Zona (Ward) *"],
                                                        ),
                                                        dcc.Dropdown(
                                                            id="ward_input",
                                                            options=[
                                                                {
                                                                    "label": f"Ward {ward}",
                                                                    "value": ward,
                                                                }
                                                                for ward in data["wards"] if ward is not None
                                                            ],
                                                            placeholder="Selecciona una zona (ward)...",
                                                            value=data["wards"][0],
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="block mb-2 font-semibold text-slate-700 text-sm",
                                                            children=["Fecha *"],
                                                        ),
                                                        dcc.DatePickerSingle(
                                                            id="date_input",
                                                            placeholder="Selecciona una fecha...",
                                                            date=date.today(),
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="block mb-2 font-semibold text-slate-700 text-sm",
                                                            children=["Hora del Día *"],
                                                        ),
                                                        dcc.Dropdown(
                                                            id="time_input",
                                                            options=[
                                                                {
                                                                    "label": f"{hour:02d}:00",
                                                                    "value": hour,
                                                                }
                                                                for hour in range(24)
                                                            ],
                                                            placeholder="Selecciona una hora...",
                                                            value=datetime.now().hour,
                                                        )
                                                    ]
                                                ),
                                                html.Button(
                                                    className="bg-slate-900 hover:bg-cyan-500 py-3 w-full font-semibold text-white transition-colors",
                                                    id="predict_button",
                                                    children=["Generar Predicción"],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="bg-cyan-50 mt-6 p-4 border-cyan-500 border-l-4",
                                            children=[
                                                html.P(
                                                    className="text-slate-700 text-sm",
                                                    children=[
                                                        html.Strong(children=["Nota:"]),
                                                        html.Span(
                                                            children=[
                                                                "Los resultados son predicciones basadas en datos históricos y modelos estadísticos. No deben usarse como única fuente para tomar decisiones de seguridad."
                                                            ]
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="lg:col-span-2",
                            children=[
                                dcc.Loading(
                                    overlay_style={"visibility": "visible", "filter": "blur(2px)"},
                                    type="circle",
                                    children=[        
                                        html.Div(
                                            className="bg-white p-8 border border-slate-200",
                                            children=[
                                                html.H2(
                                                    className="mb-6 font-bold text-slate-900 text-2xl",
                                                    children=["Resultados de la Predicción"],
                                                ),
                                                html.Div(
                                                    className="space-y-8",
                                                    id="resultsContainer",
                                                    children=[
                                                        html.Div(
                                                            className="bg-linear-to-r from-slate-900 to-slate-800 shadow-lg p-6 rounded text-white",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center mb-3",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="mr-2 w-6 h-6 text-cyan-400",
                                                                            fill="none",
                                                                            stroke="currentColor",
                                                                            viewBox="0 0 24 24",
                                                                            children=[
                                                                                dash_svg.Path(
                                                                                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z",
                                                                                    strokeLinecap="round",
                                                                                    strokeLinejoin="round",
                                                                                    strokeWidth="2",
                                                                                ),
                                                                                dash_svg.Path(
                                                                                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z",
                                                                                    strokeLinecap="round",
                                                                                    strokeLinejoin="round",
                                                                                    strokeWidth="2",
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.H3(
                                                                            className="font-bold text-xl",
                                                                            children=[
                                                                                "Predicción para:"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="gap-4 grid md:grid-cols-3 text-center",
                                                                    children=[
                                                                        html.Div(
                                                                            className="bg-white/10 backdrop-blur p-3 rounded",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-cyan-300 text-sm",
                                                                                    children=[
                                                                                        "Zona"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-white text-lg",
                                                                                    id="result_ward",
                                                                                    children=[
                                                                                        "Ward 32"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Div(
                                                                            className="bg-white/10 backdrop-blur p-3 rounded",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-cyan-300 text-sm",
                                                                                    children=[
                                                                                        "Fecha"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-white text-lg",
                                                                                    id="result_date",
                                                                                    children=[
                                                                                        "15 de Octubre, 2025"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Div(
                                                                            className="bg-white/10 backdrop-blur p-3 rounded",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-cyan-300 text-sm",
                                                                                    children=[
                                                                                        "Hora"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-white text-lg",
                                                                                    id="result_time",
                                                                                    children=[
                                                                                        "20:00"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center mb-4",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="mr-2 w-6 h-6 text-slate-900",
                                                                            fill="none",
                                                                            stroke="currentColor",
                                                                            viewBox="0 0 24 24",
                                                                            children=[
                                                                                dash_svg.Path(
                                                                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z",
                                                                                    strokeLinecap="round",
                                                                                    strokeLinejoin="round",
                                                                                    strokeWidth="2",
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.H3(
                                                                            className="font-bold text-slate-900 text-2xl",
                                                                            children=[
                                                                                "Probabilidad de Criminalidad por Impacto"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="bg-white shadow-lg border-2 border-slate-200 rounded-lg overflow-hidden",
                                                                    children=[
                                                                        html.Table(
                                                                            className="w-full",
                                                                            children=[
                                                                                html.Thead(
                                                                                    children=[
                                                                                        html.Tr(
                                                                                            className="bg-linear-to-r from-slate-900 to-slate-800 text-white",
                                                                                            children=[
                                                                                                html.Th(
                                                                                                    className="px-6 py-4 font-semibold text-left",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-5 h-5",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Nivel de Impacto"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-6 py-4 font-semibold text-center",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex justify-center items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-5 h-5",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Probabilidad"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-6 py-4 font-semibold text-left",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-5 h-5",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Indicador Visual"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                html.Tbody(
                                                                                    className="divide-y divide-slate-200",
                                                                                    children=[
                                                                                        html.Tr(
                                                                                            className="hover:bg-green-50 transition-colors",
                                                                                            children=[
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-center items-center bg-green-100 mr-4 rounded-lg w-12 h-12 shrink-0",
                                                                                                                    children=[
                                                                                                                        dash_svg.Svg(
                                                                                                                            className="w-7 h-7 text-green-600",
                                                                                                                            fill="none",
                                                                                                                            stroke="currentColor",
                                                                                                                            viewBox="0 0 24 24",
                                                                                                                            children=[
                                                                                                                                dash_svg.Path(
                                                                                                                                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                                    strokeLinecap="round",
                                                                                                                                    strokeLinejoin="round",
                                                                                                                                    strokeWidth="2",
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    children=[
                                                                                                                        html.P(
                                                                                                                            className="font-bold text-slate-900 text-lg",
                                                                                                                            children=[
                                                                                                                                "Bajo Impacto"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.P(
                                                                                                                            className="flex items-center mt-1 text-slate-600 text-sm",
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="mr-1 w-4 h-4 text-green-600",
                                                                                                                                    fill="none",
                                                                                                                                    stroke="currentColor",
                                                                                                                                    viewBox="0 0 24 24",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                                            strokeLinecap="round",
                                                                                                                                            strokeLinejoin="round",
                                                                                                                                            strokeWidth="2",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                                html.Span(
                                                                                                                                    children=[
                                                                                                                                        "Delitos menores, vandalismo, infracciones"
                                                                                                                                    ]
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5 text-center",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="inline-flex flex-col items-center",
                                                                                                            children=[
                                                                                                                html.Span(
                                                                                                                    className="font-bold text-green-600 text-4xl",
                                                                                                                    id="low_impact_probability_text",
                                                                                                                    children=[
                                                                                                                        "45.2%"
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    className="bg-green-100 mt-1 px-3 py-1 rounded-full font-semibold text-slate-500 text-xs",
                                                                                                                    children=[
                                                                                                                        "Riesgo Moderado"
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="w-full",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-between items-center mb-1",
                                                                                                                    children=[
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-slate-600 text-xs",
                                                                                                                            children=[
                                                                                                                                "Nivel de confianza"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-green-600 text-xs",
                                                                                                                            id="low_impact_probability_bar_text",
                                                                                                                            children=[
                                                                                                                                "45.2%"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    className="bg-slate-200 shadow-inner rounded-full w-full h-4",
                                                                                                                    children=[
                                                                                                                        html.Div(
                                                                                                                            className="flex justify-end items-center bg-linear-to-r from-green-500 to-green-600 shadow-md pr-2 rounded-full h-4 transition-all duration-500",
                                                                                                                            id="low_impact_probability_bar",
                                                                                                                            style={
                                                                                                                                "width": "45.2%"
                                                                                                                            },
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="w-3 h-3 text-white",
                                                                                                                                    fill="currentColor",
                                                                                                                                    viewBox="0 0 20 20",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            clipRule="evenodd",
                                                                                                                                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z",
                                                                                                                                            fillRule="evenodd",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                        html.Tr(
                                                                                            className="hover:bg-yellow-50 transition-colors",
                                                                                            children=[
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-center items-center bg-yellow-100 mr-4 rounded-lg w-12 h-12 shrink-0",
                                                                                                                    children=[
                                                                                                                        dash_svg.Svg(
                                                                                                                            className="w-7 h-7 text-yellow-600",
                                                                                                                            fill="none",
                                                                                                                            stroke="currentColor",
                                                                                                                            viewBox="0 0 24 24",
                                                                                                                            children=[
                                                                                                                                dash_svg.Path(
                                                                                                                                    d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z",
                                                                                                                                    strokeLinecap="round",
                                                                                                                                    strokeLinejoin="round",
                                                                                                                                    strokeWidth="2",
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    children=[
                                                                                                                        html.P(
                                                                                                                            className="font-bold text-slate-900 text-lg",
                                                                                                                            children=[
                                                                                                                                "Medio Impacto"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.P(
                                                                                                                            className="flex items-center mt-1 text-slate-600 text-sm",
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="mr-1 w-4 h-4 text-yellow-600",
                                                                                                                                    fill="none",
                                                                                                                                    stroke="currentColor",
                                                                                                                                    viewBox="0 0 24 24",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                                            strokeLinecap="round",
                                                                                                                                            strokeLinejoin="round",
                                                                                                                                            strokeWidth="2",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                                html.Span(
                                                                                                                                    children=[
                                                                                                                                        "Robos, hurtos, fraudes, daños a propiedad"
                                                                                                                                    ]
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5 text-center",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="inline-flex flex-col items-center",
                                                                                                            children=[
                                                                                                                html.Span(
                                                                                                                    className="font-bold text-yellow-600 text-4xl",
                                                                                                                    id="medium_impact_probability_text",
                                                                                                                    children=[
                                                                                                                        "38.7%"
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    className="bg-yellow-100 mt-1 px-3 py-1 rounded-full font-semibold text-slate-500 text-xs",
                                                                                                                    children=[
                                                                                                                        "Precaución"
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="w-full",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-between items-center mb-1",
                                                                                                                    children=[
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-slate-600 text-xs",
                                                                                                                            children=[
                                                                                                                                "Nivel de confianza"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-yellow-600 text-xs",
                                                                                                                            id="medium_impact_probability_bar_text",
                                                                                                                            children=[
                                                                                                                                "38.7%"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    className="bg-slate-200 shadow-inner rounded-full w-full h-4",
                                                                                                                    children=[
                                                                                                                        html.Div(
                                                                                                                            className="flex justify-end items-center bg-linear-to-r from-yellow-500 to-yellow-600 shadow-md pr-2 rounded-full h-4 transition-all duration-500",
                                                                                                                            id="medium_impact_probability_bar",
                                                                                                                            style={
                                                                                                                                "width": "38.7%"
                                                                                                                            },
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="w-3 h-3 text-white",
                                                                                                                                    fill="currentColor",
                                                                                                                                    viewBox="0 0 20 20",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            clipRule="evenodd",
                                                                                                                                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z",
                                                                                                                                            fillRule="evenodd",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                        html.Tr(
                                                                                            className="hover:bg-red-50 transition-colors",
                                                                                            children=[
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-center items-center bg-red-100 mr-4 rounded-lg w-12 h-12 shrink-0",
                                                                                                                    children=[
                                                                                                                        dash_svg.Svg(
                                                                                                                            className="w-7 h-7 text-red-600",
                                                                                                                            fill="none",
                                                                                                                            stroke="currentColor",
                                                                                                                            viewBox="0 0 24 24",
                                                                                                                            children=[
                                                                                                                                dash_svg.Path(
                                                                                                                                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                                    strokeLinecap="round",
                                                                                                                                    strokeLinejoin="round",
                                                                                                                                    strokeWidth="2",
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    children=[
                                                                                                                        html.P(
                                                                                                                            className="font-bold text-slate-900 text-lg",
                                                                                                                            children=[
                                                                                                                                "Alto Impacto"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.P(
                                                                                                                            className="flex items-center mt-1 text-slate-600 text-sm",
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="mr-1 w-4 h-4 text-red-600",
                                                                                                                                    fill="none",
                                                                                                                                    stroke="currentColor",
                                                                                                                                    viewBox="0 0 24 24",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                                            strokeLinecap="round",
                                                                                                                                            strokeLinejoin="round",
                                                                                                                                            strokeWidth="2",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                                html.Span(
                                                                                                                                    children=[
                                                                                                                                        "Agresiones, asaltos, crímenes violentos"
                                                                                                                                    ]
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5 text-center",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="inline-flex flex-col items-center",
                                                                                                            children=[
                                                                                                                html.Span(
                                                                                                                    className="font-bold text-red-600 text-4xl",
                                                                                                                    id="high_impact_probability_text",
                                                                                                                    children=[
                                                                                                                        "16.1%"
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    className="bg-red-100 mt-1 px-3 py-1 rounded-full font-semibold text-slate-500 text-xs",
                                                                                                                    children=[
                                                                                                                        "Alerta Alta"
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Td(
                                                                                                    className="px-6 py-5",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="w-full",
                                                                                                            children=[
                                                                                                                html.Div(
                                                                                                                    className="flex justify-between items-center mb-1",
                                                                                                                    children=[
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-slate-600 text-xs",
                                                                                                                            children=[
                                                                                                                                "Nivel de confianza"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                        html.Span(
                                                                                                                            className="font-semibold text-red-600 text-xs",
                                                                                                                            id="high_impact_probability_bar_text",
                                                                                                                            children=[
                                                                                                                                "16.1%"
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Div(
                                                                                                                    className="bg-slate-200 shadow-inner rounded-full w-full h-4",
                                                                                                                    children=[
                                                                                                                        html.Div(
                                                                                                                            className="flex justify-end items-center bg-linear-to-r from-red-500 to-red-600 shadow-md pr-2 rounded-full h-4 transition-all duration-500",
                                                                                                                            id="high_impact_probability_bar",
                                                                                                                            style={
                                                                                                                                "width": "16.1%"
                                                                                                                            },
                                                                                                                            children=[
                                                                                                                                dash_svg.Svg(
                                                                                                                                    className="w-3 h-3 text-white",
                                                                                                                                    fill="currentColor",
                                                                                                                                    viewBox="0 0 20 20",
                                                                                                                                    children=[
                                                                                                                                        dash_svg.Path(
                                                                                                                                            clipRule="evenodd",
                                                                                                                                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z",
                                                                                                                                            fillRule="evenodd",
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                )
                                                                                                                            ],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="gap-4 grid grid-cols-3 mt-4",
                                                                    children=[
                                                                        html.Div(
                                                                            className="bg-slate-50 p-4 border border-slate-200 rounded-lg text-center",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-slate-600 text-xs",
                                                                                    children=[
                                                                                        "Probabilidad Total"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-slate-900 text-2xl",
                                                                                    children=[
                                                                                        "100%"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Div(
                                                                            className="bg-cyan-50 p-4 border border-cyan-200 rounded-lg text-center",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-slate-600 text-xs",
                                                                                    children=[
                                                                                        "Nivel de Confianza"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-cyan-600 text-2xl",
                                                                                    children=[
                                                                                        "87.3%"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Div(
                                                                            className="bg-slate-50 p-4 border border-slate-200 rounded-lg text-center",
                                                                            children=[
                                                                                html.P(
                                                                                    className="mb-1 text-slate-600 text-xs",
                                                                                    children=[
                                                                                        "Datos Analizados"
                                                                                    ],
                                                                                ),
                                                                                html.P(
                                                                                    className="font-bold text-slate-900 text-2xl",
                                                                                    children=[
                                                                                        "45,892"
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="bg-linear-to-r from-slate-800 to-slate-700 shadow-xl p-8 rounded-lg text-white",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center mb-4",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="mr-3 w-8 h-8 text-cyan-400",
                                                                            fill="none",
                                                                            stroke="currentColor",
                                                                            viewBox="0 0 24 24",
                                                                            children=[
                                                                                dash_svg.Path(
                                                                                    d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z",
                                                                                    strokeLinecap="round",
                                                                                    strokeLinejoin="round",
                                                                                    strokeWidth="2",
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.H3(
                                                                            className="font-bold text-2xl",
                                                                            children=[
                                                                                "Delito Más Común en esta Zona"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="gap-6 grid md:grid-cols-3",
                                                                    children=[
                                                                        html.Div(
                                                                            className="md:col-span-2 bg-white/10 backdrop-blur p-6 rounded-lg",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="flex items-center mb-3",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="flex justify-center items-center bg-cyan-400 mr-4 rounded-lg w-16 h-16",
                                                                                            children=[
                                                                                                dash_svg.Svg(
                                                                                                    className="w-9 h-9 text-slate-900",
                                                                                                    fill="none",
                                                                                                    stroke="currentColor",
                                                                                                    viewBox="0 0 24 24",
                                                                                                    children=[
                                                                                                        dash_svg.Path(
                                                                                                            d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5m.75-9 3-3 2.148 2.148A12.061 12.061 0 0 1 16.5 7.605",
                                                                                                            strokeLinecap="round",
                                                                                                            strokeLinejoin="round",
                                                                                                            strokeWidth="2",
                                                                                                        )
                                                                                                    ],
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.Div(
                                                                                            children=[
                                                                                                html.P(
                                                                                                    className="font-bold text-cyan-300 text-4xl",
                                                                                                    id="most_common_crime_type",
                                                                                                    children=[
                                                                                                        "THEFT"
                                                                                                    ],
                                                                                                ),
                                                                                                html.P(
                                                                                                    className="mt-1 text-slate-300",
                                                                                                    id="most_common_crime_type_description",
                                                                                                    children=[
                                                                                                        "Robo / Hurto"
                                                                                                    ],
                                                                                                ),
                                                                                            ]
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                html.Div(
                                                                                    className="flex items-center text-slate-200",
                                                                                    children=[
                                                                                        dash_svg.Svg(
                                                                                            className="mr-2 w-5 h-5 text-cyan-400",
                                                                                            fill="none",
                                                                                            stroke="currentColor",
                                                                                            viewBox="0 0 24 24",
                                                                                            children=[
                                                                                                dash_svg.Path(
                                                                                                    d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6",
                                                                                                    strokeLinecap="round",
                                                                                                    strokeLinejoin="round",
                                                                                                    strokeWidth="2",
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.Span(
                                                                                            className="font-semibold text-cyan-300 text-2xl",
                                                                                            id="most_common_crime_type_percentage",
                                                                                            children=[
                                                                                                "34.5%"
                                                                                            ],
                                                                                        ),
                                                                                        html.Span(
                                                                                            className="ml-2",
                                                                                            children=[
                                                                                                "de todos los incidentes reportados"
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Div(
                                                                            className="flex flex-col justify-center bg-white/10 backdrop-blur p-6 rounded-lg",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="text-center",
                                                                                    children=[
                                                                                        dash_svg.Svg(
                                                                                            className="mx-auto mb-2 w-12 h-12 text-cyan-400",
                                                                                            fill="none",
                                                                                            stroke="currentColor",
                                                                                            viewBox="0 0 24 24",
                                                                                            children=[
                                                                                                dash_svg.Path(
                                                                                                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z",
                                                                                                    strokeLinecap="round",
                                                                                                    strokeLinejoin="round",
                                                                                                    strokeWidth="2",
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.P(
                                                                                            className="mb-1 text-slate-300 text-sm",
                                                                                            children=[
                                                                                                "Período de análisis"
                                                                                            ],
                                                                                        ),
                                                                                        html.P(
                                                                                            className="font-bold text-white text-xl",
                                                                                            children=[
                                                                                                "Últimos 12 meses"
                                                                                            ],
                                                                                        ),
                                                                                        html.P(
                                                                                            className="mt-2 text-slate-400 text-xs",
                                                                                            children=[
                                                                                                "3,247 incidentes analizados"
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center mb-4",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="mr-2 w-6 h-6 text-slate-900",
                                                                            fill="none",
                                                                            stroke="currentColor",
                                                                            viewBox="0 0 24 24",
                                                                            children=[
                                                                                dash_svg.Path(
                                                                                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01",
                                                                                    strokeLinecap="round",
                                                                                    strokeLinejoin="round",
                                                                                    strokeWidth="2",
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.H3(
                                                                            className="font-bold text-slate-900 text-2xl",
                                                                            children=[
                                                                                "Últimos 5 Delitos Reportados en la Zona"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="bg-white shadow-lg border-2 border-slate-200 rounded-lg overflow-hidden",
                                                                    children=[
                                                                        html.Table(
                                                                            className="w-full",
                                                                            children=[
                                                                                html.Thead(
                                                                                    children=[
                                                                                        html.Tr(
                                                                                            className="bg-linear-to-r from-slate-100 to-slate-50 border-slate-300 border-b-2",
                                                                                            children=[
                                                                                                html.Th(
                                                                                                    className="px-5 py-4 font-bold text-slate-700 text-sm text-left",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-4 h-4 text-slate-500",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Fecha"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-5 py-4 font-bold text-slate-700 text-sm text-left",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-4 h-4 text-slate-500",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Hora"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-5 py-4 font-bold text-slate-700 text-sm text-left",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-4 h-4 text-slate-500",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Tipo de Delito"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-5 py-4 font-bold text-slate-700 text-sm text-left",
                                                                                                    children=[
                                                                                                        "Descripción"
                                                                                                    ],
                                                                                                ),
                                                                                                html.Th(
                                                                                                    className="px-5 py-4 font-bold text-slate-700 text-sm text-center",
                                                                                                    children=[
                                                                                                        html.Div(
                                                                                                            className="flex justify-center items-center",
                                                                                                            children=[
                                                                                                                dash_svg.Svg(
                                                                                                                    className="mr-2 w-4 h-4 text-slate-500",
                                                                                                                    fill="none",
                                                                                                                    stroke="currentColor",
                                                                                                                    viewBox="0 0 24 24",
                                                                                                                    children=[
                                                                                                                        dash_svg.Path(
                                                                                                                            d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z",
                                                                                                                            strokeLinecap="round",
                                                                                                                            strokeLinejoin="round",
                                                                                                                            strokeWidth="2",
                                                                                                                        )
                                                                                                                    ],
                                                                                                                ),
                                                                                                                html.Span(
                                                                                                                    children=[
                                                                                                                        "Impacto"
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ],
                                                                                                        )
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                html.Tbody(
                                                                                    className="divide-y divide-slate-200",
                                                                                    id="recent_crimes_table_body",
                                                                                    children=[],
                                                                                ),
                                                                            ],
                                                                        )
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="p-6 border border-slate-200",
                                                            children=[
                                                                html.H3(
                                                                    className="mb-3 font-bold text-slate-900 text-lg",
                                                                    children=[
                                                                        "Contexto Adicional"
                                                                    ],
                                                                ),
                                                                html.Ul(
                                                                    className="space-y-2 text-slate-700",
                                                                    children=[
                                                                        html.Li(
                                                                            className="flex items-start",
                                                                            children=[
                                                                                dash_svg.Svg(
                                                                                    className="mt-0.5 mr-2 w-5 h-5 text-cyan-500 shrink-0",
                                                                                    fill="none",
                                                                                    stroke="currentColor",
                                                                                    viewBox="0 0 24 24",
                                                                                    children=[
                                                                                        dash_svg.Path(
                                                                                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                            strokeLinecap="round",
                                                                                            strokeLinejoin="round",
                                                                                            strokeWidth="2",
                                                                                        )
                                                                                    ],
                                                                                ),
                                                                                html.Span(
                                                                                    children=[
                                                                                        "La predicción se basa en más de 500,000 registros históricos de criminalidad"
                                                                                    ]
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Li(
                                                                            className="flex items-start",
                                                                            children=[
                                                                                dash_svg.Svg(
                                                                                    className="mt-0.5 mr-2 w-5 h-5 text-cyan-500 shrink-0",
                                                                                    fill="none",
                                                                                    stroke="currentColor",
                                                                                    viewBox="0 0 24 24",
                                                                                    children=[
                                                                                        dash_svg.Path(
                                                                                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                            strokeLinecap="round",
                                                                                            strokeLinejoin="round",
                                                                                            strokeWidth="2",
                                                                                        )
                                                                                    ],
                                                                                ),
                                                                                html.Span(
                                                                                    children=[
                                                                                        "El modelo considera factores como día de la semana, hora, zona geográfica y tendencias históricas"
                                                                                    ]
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        html.Li(
                                                                            className="flex items-start",
                                                                            children=[
                                                                                dash_svg.Svg(
                                                                                    className="mt-0.5 mr-2 w-5 h-5 text-cyan-500 shrink-0",
                                                                                    fill="none",
                                                                                    stroke="currentColor",
                                                                                    viewBox="0 0 24 24",
                                                                                    children=[
                                                                                        dash_svg.Path(
                                                                                            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                            strokeLinecap="round",
                                                                                            strokeLinejoin="round",
                                                                                            strokeWidth="2",
                                                                                        )
                                                                                    ],
                                                                                ),
                                                                                html.Span(
                                                                                    children=[
                                                                                        "Los resultados tienen un nivel de confianza del 85% basado en validaciones cruzadas"
                                                                                    ]
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        )
                                    ]
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white mt-12 p-8 border border-slate-200",
                    children=[
                        html.H2(
                            className="mb-6 font-bold text-slate-900 text-2xl",
                            children=["¿Cómo Funciona la Predicción?"],
                        ),
                        html.Div(
                            className="gap-6 grid md:grid-cols-4",
                            children=[
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mx-auto mb-4 rounded-full w-16 h-16",
                                            children=[
                                                html.Span(
                                                    className="font-bold text-cyan-600 text-2xl",
                                                    children=["1"],
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="mb-2 font-semibold text-slate-900",
                                            children=["Recopilación de Datos"],
                                        ),
                                        html.P(
                                            className="text-slate-600 text-sm",
                                            children=[
                                                "Se recopilan datos históricos de crímenes de Chicago"
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mx-auto mb-4 rounded-full w-16 h-16",
                                            children=[
                                                html.Span(
                                                    className="font-bold text-cyan-600 text-2xl",
                                                    children=["2"],
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="mb-2 font-semibold text-slate-900",
                                            children=["Análisis de Patrones"],
                                        ),
                                        html.P(
                                            className="text-slate-600 text-sm",
                                            children=[
                                                "Identificación de patrones temporales y espaciales"
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mx-auto mb-4 rounded-full w-16 h-16",
                                            children=[
                                                html.Span(
                                                    className="font-bold text-cyan-600 text-2xl",
                                                    children=["3"],
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="mb-2 font-semibold text-slate-900",
                                            children=["Modelo Predictivo"],
                                        ),
                                        html.P(
                                            className="text-slate-600 text-sm",
                                            children=[
                                                "Aplicación de algoritmos de machine learning"
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mx-auto mb-4 rounded-full w-16 h-16",
                                            children=[
                                                html.Span(
                                                    className="font-bold text-cyan-600 text-2xl",
                                                    children=["4"],
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="mb-2 font-semibold text-slate-900",
                                            children=["Resultados"],
                                        ),
                                        html.P(
                                            className="text-slate-600 text-sm",
                                            children=[
                                                "Generación de probabilidades y recomendaciones"
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ]
)
    
@callback(
    Output("result_ward", "children"),
    Output("result_date", "children"),
    Output("result_time", "children"),
    Output("low_impact_probability_text", "children"),
    Output("low_impact_probability_bar_text", "children"),
    Output("low_impact_probability_bar", "style"),
    Output("medium_impact_probability_text", "children"),
    Output("medium_impact_probability_bar_text", "children"),
    Output("medium_impact_probability_bar", "style"),
    Output("high_impact_probability_text", "children"),
    Output("high_impact_probability_bar_text", "children"),
    Output("high_impact_probability_bar", "style"),
    Output("most_common_crime_type", "children"),
    Output("most_common_crime_type_description", "children"),
    Output("most_common_crime_type_percentage", "children"),
    Output("recent_crimes_table_body", "children"),
    Input("predict_button", "n_clicks"),
    State("ward_input", "value"),
    State("date_input", "date"),
    State("time_input", "value"),
)
async def update_prediction(n_clicks, ward, date_value, time_value):
    if n_clicks:
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "ward": f"Ward_{ward}",
                    "month": pd.to_datetime(date_value).month_name(),
                    "day_of_week": pd.to_datetime(date_value).day_name(),
                    "hour": time_value,
                }
                response = await client.post(
                    "http://localhost:8000/predict_impact",
                    json=payload,
                )
                response.raise_for_status()
                prediction = response.json()
                
            
            API_URLS = {
                "highest_count_crime": f"http://localhost:8000/highest_count_crime/{ward}",
                "recent_crimes": f"http://localhost:8000/recent_crimes/{ward}",
            }
            
            data = await get_all_data(API_URLS)
            
            impact_visuals = {
                "low_impact": {
                    "circle": "bg-green-500 mr-2 rounded-full w-2 h-2",
                    "tag": html.Span(
                        className="inline-flex items-center bg-green-100 px-3 py-1.5 border border-green-300 rounded-full font-bold text-green-800 text-xs",
                        children=[
                            dash_svg.Svg(
                                className="mr-1 w-3 h-3",
                                fill="none",
                                stroke="currentColor",
                                viewBox="0 0 24 24",
                                children=[
                                    dash_svg.Path(
                                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
                                        strokeLinecap="round",
                                        strokeLinejoin="round",
                                        strokeWidth="2",
                                    )
                                ],
                            ),
                            html.Span(
                                children=[
                                    "Bajo"
                                ]
                            ),
                        ],
                    )
                },
                "medium_impact": {
                    "circle": "bg-yellow-500 mr-2 rounded-full w-2 h-2",
                    "tag": html.Span(
                        className="inline-flex items-center bg-yellow-100 px-3 py-1.5 border border-yellow-300 rounded-full font-bold text-yellow-800 text-xs",
                        children=[
                            dash_svg.Svg(
                                className="mr-1 w-3 h-3",
                                fill="none",
                                stroke="currentColor",
                                viewBox="0 0 24 24",
                                children=[
                                    dash_svg.Path(
                                        d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z",
                                        strokeLinecap="round",
                                        strokeLinejoin="round",
                                        strokeWidth="2",
                                    )
                                ],
                            ),
                            html.Span(
                                children=[
                                    "Medio"
                                ]
                            ),
                        ],
                    )
                },
                "high_impact": {
                    "circle": "bg-red-500 mr-2 rounded-full w-2 h-2",
                    "tag": html.Span(
                        className="inline-flex items-center bg-red-100 px-3 py-1.5 border border-red-300 rounded-full font-bold text-red-800 text-xs",
                        children=[
                            dash_svg.Svg(
                                className="mr-1 w-3 h-3",
                                fill="none",
                                stroke="currentColor",
                                viewBox="0 0 24 24",
                                children=[
                                    dash_svg.Path(
                                        d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                        strokeLinecap="round",
                                        strokeLinejoin="round",
                                        strokeWidth="2",
                                    )
                                ],
                            ),
                            html.Span(
                                children=[
                                    "Alto"
                                ]
                            ),
                        ],
                    )
                }
            }
            
            return (
                f"Ward {ward}", 
                datetime.fromisoformat(date_value).strftime("%d/%m/%Y"), 
                f"{time_value:02d}:00", 
                f"{prediction["low_impact_probability"]:.1%}",
                f"{prediction["low_impact_probability"]:.1%}",
                {"width": f"{prediction["low_impact_probability"]:.1%}"},
                f"{prediction["medium_impact_probability"]:.1%}",
                f"{prediction["medium_impact_probability"]:.1%}",
                {"width": f"{prediction["medium_impact_probability"]:.1%}"},
                f"{prediction["high_impact_probability"]:.1%}",
                f"{prediction["high_impact_probability"]:.1%}",
                {"width": f"{prediction["high_impact_probability"]:.1%}"},
                data["highest_count_crime"]["primary_type"],
                data["highest_count_crime"]["primary_type"],
                f"{data["highest_count_crime"]["ratio"]:.1%}",
                [
                    html.Tr(className="hover:bg-yellow-50 transition-colors",
                        children=[
                            html.Td(
                                className="px-5 py-4",
                                children=[
                                    html.Div(
                                        className="flex items-center font-medium text-slate-900 text-sm",
                                        children=[
                                            dash_svg.Svg(
                                                className="mr-2 w-4 h-4 text-slate-400",
                                                fill="currentColor",
                                                viewBox="0 0 20 20",
                                                children=[
                                                    dash_svg.Path(
                                                        clipRule="evenodd",
                                                        d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z",
                                                        fillRule="evenodd",
                                                    )
                                                ],
                                            ),
                                            html.Span(
                                                children=[
                                                    crime["date"].split("T")[0].replace("-", "/")
                                                ]
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            html.Td(
                                className="px-5 py-4",
                                children=[
                                    html.Div(
                                        className="flex items-center text-slate-900 text-sm",
                                        children=[
                                            dash_svg.Svg(
                                                className="mr-2 w-4 h-4 text-slate-400",
                                                fill="currentColor",
                                                viewBox="0 0 20 20",
                                                children=[
                                                    dash_svg.Path(
                                                        clipRule="evenodd",
                                                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z",
                                                        fillRule="evenodd",
                                                    )
                                                ],
                                            ),
                                            html.Span(
                                                children=[
                                                    crime["date"].split("T")[1]
                                                ]
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            html.Td(
                                className="px-5 py-4",
                                children=[
                                    html.Div(
                                        className="flex items-center",
                                        children=[
                                            html.Div(
                                                className=impact_visuals[crime["impact_level"].lower()]["circle"]
                                            ),
                                            html.Span(
                                                className="font-bold text-slate-900 text-sm",
                                                children=[
                                                    crime["primary_type"]
                                                ],
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            html.Td(
                                className="px-5 py-4 text-slate-600 text-sm",
                                children=[
                                    crime["description"]
                                ],
                            ),
                            html.Td(
                                className="px-5 py-4 text-center",
                                children=[
                                    impact_visuals[crime["impact_level"].lower()]["tag"]
                                ],
                            ),
                        ],
                    ) for crime in data["recent_crimes"]
                ]
            )
        except Exception as e:
            print(f"Error during prediction: {e}")
    return (
        "Ward -", 
        "-/--/----", 
        "--:--", 
        "---%",
        "---%",
        {"width": "0%"},
        "---%",
        "---%",
        {"width": "0%"},
        "---%",
        "---%",
        {"width": "0%"},
        "---",
        "---",
        "---%",
        []
    )