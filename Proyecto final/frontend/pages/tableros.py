import dash
import dash_svg
from dash import html

dash.register_page(
    __name__,
    path="/tableros",
    title="Tableros de Análisis Interactivos - Criminalidad en Chicago",
    name="tableros",
)

async def layout():
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
                                    children=["Tableros de Análisis Interactivos"],
                                ),
                                html.P(
                                    className="text-slate-200 text-xl leading-relaxed",
                                    children=[
                                        "Explora visualizaciones interactivas de datos de criminalidad en Chicago. Analiza tendencias, patrones y estadísticas clave para comprender mejor la distribución del crimen en la ciudad."
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
                    className="bg-white shadow-sm mb-12 p-8 border border-slate-200",
                    children=[
                        html.Div(
                            className="mb-6",
                            children=[
                                html.H2(
                                    className="mb-3 font-bold text-slate-900 text-3xl",
                                    children=["Dashboard Principal"],
                                ),
                                html.P(
                                    className="text-slate-600 text-lg",
                                    children=[
                                        "Este tablero interactivo presenta un análisis completo de los datos de criminalidad en Chicago, incluyendo tendencias temporales, distribución geográfica y tipos de delitos."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-slate-50 border border-slate-300 w-full",
                            style={"height": "800px"},
                            children=[
                                html.Iframe(
                                    className="w-full h-full",
                                    height="100%",
                                    src="https://public.tableau.com/views/DASHBOARDINDIVIDUAL2/Dashboard1?:embed=true&:showVizHome=no",
                                    width="100%",
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="gap-8 grid md:grid-cols-3 mb-12",
                    children=[
                        html.Div(
                            className="bg-white hover:shadow-lg p-6 border border-slate-200 transition-shadow",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-100 mb-4 rounded-full w-12 h-12",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-6 h-6 text-cyan-600",
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
                                        )
                                    ],
                                ),
                                html.H3(
                                    className="mb-2 font-bold text-slate-900 text-xl",
                                    children=["Análisis Temporal"],
                                ),
                                html.P(
                                    className="text-slate-600",
                                    children=[
                                        "Visualiza la evolución del crimen a lo largo del tiempo con gráficos de tendencias y series temporales."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white hover:shadow-lg p-6 border border-slate-200 transition-shadow",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-100 mb-4 rounded-full w-12 h-12",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-6 h-6 text-cyan-600",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        )
                                    ],
                                ),
                                html.H3(
                                    className="mb-2 font-bold text-slate-900 text-xl",
                                    children=["Distribución Geográfica"],
                                ),
                                html.P(
                                    className="text-slate-600",
                                    children=[
                                        "Identifica zonas de alta criminalidad y patrones espaciales mediante mapas de calor y visualizaciones geográficas."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white hover:shadow-lg p-6 border border-slate-200 transition-shadow",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-100 mb-4 rounded-full w-12 h-12",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-6 h-6 text-cyan-600",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        )
                                    ],
                                ),
                                html.H3(
                                    className="mb-2 font-bold text-slate-900 text-xl",
                                    children=["Categorías de Delitos"],
                                ),
                                html.P(
                                    className="text-slate-600",
                                    children=[
                                        "Analiza la distribución de diferentes tipos de crímenes y sus proporciones mediante gráficos circulares y de barras."
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-linear-to-r from-slate-800 to-slate-700 mb-12 p-10 text-white",
                    children=[
                        html.H2(
                            className="mb-6 font-bold text-3xl",
                            children=["Insights Clave del Análisis"],
                        ),
                        html.Div(
                            className="gap-8 grid md:grid-cols-2",
                            children=[
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="mb-3 font-semibold text-cyan-300 text-xl",
                                            children=["Tendencias Identificadas"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Variación estacional en la incidencia de ciertos tipos de delitos"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Concentración de criminalidad en zonas específicas de la ciudad"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Horarios de mayor incidencia delictiva"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="mb-3 font-semibold text-cyan-300 text-xl",
                                            children=["Datos Destacados"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Análisis basado en miles de registros históricos de Chicago"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Actualización periódica de la información"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Span(
                                                            className="mr-2 text-cyan-400",
                                                            children=["•"],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Múltiples dimensiones de análisis disponibles"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white p-8 border border-slate-200",
                    children=[
                        html.H2(
                            className="mb-6 font-bold text-slate-900 text-2xl",
                            children=["Cómo Utilizar el Tablero"],
                        ),
                        html.Div(
                            className="gap-6 grid md:grid-cols-2",
                            children=[
                                html.Div(
                                    className="flex items-start space-x-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 font-bold text-white shrink-0",
                                            children=["1"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-semibold text-slate-900",
                                                    children=[
                                                        "Interactúa con las Visualizaciones"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Haz clic en los elementos del tablero para filtrar y explorar los datos en profundidad."
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 font-bold text-white shrink-0",
                                            children=["2"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-semibold text-slate-900",
                                                    children=["Utiliza los Filtros"],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Aplica filtros por fecha, tipo de delito o zona para personalizar tu análisis."
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 font-bold text-white shrink-0",
                                            children=["3"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-semibold text-slate-900",
                                                    children=["Explora Detalles"],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Pasa el cursor sobre los gráficos para ver información detallada de cada punto de datos."
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 font-bold text-white shrink-0",
                                            children=["4"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-semibold text-slate-900",
                                                    children=["Descarga Reportes"],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Exporta visualizaciones y datos para tus propios análisis o presentaciones."
                                                    ],
                                                ),
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
    ]
)
