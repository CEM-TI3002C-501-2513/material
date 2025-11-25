import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path="/",
    title="Chicago Crime Prediction - Proyecto Thales",
    name="Inicio",
)

async def layout():
    return html.Div(
    children=[
        html.Section(
            className="relative bg-slate-800 py-32 overflow-hidden text-white",
            children=[
                html.Div(
                    className="absolute inset-0 bg-linear-to-r from-slate-900/90 to-slate-800/90"
                ),
                html.Div(
                    className="z-10 relative mx-auto px-6 container",
                    children=[
                        html.Div(
                            className="max-w-3xl",
                            children=[
                                html.H1(
                                    className="mb-6 font-bold text-5xl leading-tight",
                                    children=["Predicción de Crimen en Chicago"],
                                ),
                                html.P(
                                    className="mb-8 text-slate-200 text-xl leading-relaxed",
                                    children=[
                                        "Análisis avanzado y predicción de patrones delictivos utilizando datos históricos e inteligencia artificial"
                                    ],
                                ),
                                html.Div(
                                    className="flex gap-4",
                                    children=[
                                        dcc.Link(
                                            className="bg-cyan-500 hover:bg-cyan-600 px-8 py-3 font-semibold text-white transition-colors",
                                            href="/prediccion",
                                            children=["Hacer una Predicción →"],
                                        ),
                                        dcc.Link(
                                            className="hover:bg-white/10 px-8 py-3 border-2 border-white font-semibold text-white transition-colors",
                                            href="/tableros",
                                            children=["Ver Tableros"],
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
        html.Main(
            className="mx-auto px-6 py-20 container",
            children=[
                html.H2(
                    className="mb-4 font-bold text-slate-900 text-4xl",
                    children=["Explora Nuestras Herramientas"],
                ),
                html.P(
                    className="mb-16 max-w-2xl text-slate-600 text-lg",
                    children=[
                        "Descubre las funcionalidades de nuestra plataforma de análisis predictivo de criminalidad"
                    ],
                ),
                html.Div(
                    className="space-y-8",
                    children=[
                        html.Div(
                            className="bg-white shadow-sm hover:shadow-xl border border-slate-200 overflow-hidden transition-shadow duration-300",
                            children=[
                                html.Div(
                                    className="gap-0 grid md:grid-cols-2",
                                    children=[
                                        html.Div(
                                            className="h-80 md:h-auto overflow-hidden",
                                            children=[
                                                html.Img(
                                                    alt="Tableros de análisis",
                                                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500",
                                                    src=dash.get_asset_url("images/tableros.jpg"),
                                                )
                                            ],
                                        ),
                                        html.Div(
                                            className="flex flex-col justify-center p-10",
                                            children=[
                                                html.H3(
                                                    className="mb-4 font-bold text-slate-900 text-3xl",
                                                    children=["Tableros de Análisis"],
                                                ),
                                                html.P(
                                                    className="mb-6 text-slate-600 text-lg leading-relaxed",
                                                    children=[
                                                        "Visualiza estadísticas detalladas y tendencias de criminalidad en Chicago mediante gráficos interactivos y dashboards dinámicos que facilitan la comprensión de patrones complejos."
                                                    ],
                                                ),
                                                html.Div(
                                                    children=[
                                                        dcc.Link(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="/tableros",
                                                            children=["Ver Tableros →"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="bg-white shadow-sm hover:shadow-xl border border-slate-200 overflow-hidden transition-shadow duration-300",
                            children=[
                                html.Div(
                                    className="gap-0 grid md:grid-cols-2",
                                    children=[
                                        html.Div(
                                            className="md:order-2 h-80 md:h-auto overflow-hidden",
                                            children=[
                                                html.Img(
                                                    alt="Predicción con IA",
                                                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500",
                                                    src=dash.get_asset_url("images/prediccion.jpg"),
                                                )
                                            ],
                                        ),
                                        html.Div(
                                            className="flex flex-col justify-center md:order-1 p-10",
                                            children=[
                                                html.H3(
                                                    className="mb-4 font-bold text-slate-900 text-3xl",
                                                    children=["Modelo Predictivo"],
                                                ),
                                                html.P(
                                                    className="mb-6 text-slate-600 text-lg leading-relaxed",
                                                    children=[
                                                        "Utiliza nuestro avanzado modelo de inteligencia artificial para predecir la probabilidad de ocurrencia de crímenes en áreas específicas de la ciudad con alta precisión."
                                                    ],
                                                ),
                                                html.Div(
                                                    children=[
                                                        dcc.Link(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="/prediccion",
                                                            children=[
                                                                "Hacer Predicción →"
                                                            ],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="bg-white shadow-sm hover:shadow-xl border border-slate-200 overflow-hidden transition-shadow duration-300",
                            children=[
                                html.Div(
                                    className="gap-0 grid md:grid-cols-2",
                                    children=[
                                        html.Div(
                                            className="h-80 md:h-auto overflow-hidden",
                                            children=[
                                                html.Img(
                                                    alt="Mapa interactivo de delitos",
                                                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500",
                                                    src=dash.get_asset_url("images/mapa.jpg"),
                                                )
                                            ],
                                        ),
                                        html.Div(
                                            className="flex flex-col justify-center p-10",
                                            children=[
                                                html.H3(
                                                    className="mb-4 font-bold text-slate-900 text-3xl",
                                                    children=[
                                                        "Mapa Interactivo de Delitos"
                                                    ],
                                                ),
                                                html.P(
                                                    className="mb-6 text-slate-600 text-lg leading-relaxed",
                                                    children=[
                                                        "Explora un mapa geoespacial interactivo que muestra la ubicación, distribución y concentración de incidentes criminales en diferentes zonas de Chicago."
                                                    ],
                                                ),
                                                html.Div(
                                                    children=[
                                                        dcc.Link(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="/mapa",
                                                            children=["Ver Mapa →"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="bg-white shadow-sm hover:shadow-xl border border-slate-200 overflow-hidden transition-shadow duration-300",
                            children=[
                                html.Div(
                                    className="gap-0 grid md:grid-cols-2",
                                    children=[
                                        html.Div(
                                            className="md:order-2 h-80 md:h-auto overflow-hidden",
                                            children=[
                                                html.Img(
                                                    alt="Equipo de trabajo",
                                                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-500",
                                                    src=dash.get_asset_url("images/acerca.jpg"),
                                                )
                                            ],
                                        ),
                                        html.Div(
                                            className="flex flex-col justify-center md:order-1 p-10",
                                            children=[
                                                html.H3(
                                                    className="mb-4 font-bold text-slate-900 text-3xl",
                                                    children=["Acerca del Proyecto"],
                                                ),
                                                html.P(
                                                    className="mb-6 text-slate-600 text-lg leading-relaxed",
                                                    children=[
                                                        "Conoce más sobre el proyecto, la metodología aplicada, las fuentes de datos utilizadas y el equipo multidisciplinario detrás de esta innovadora herramienta."
                                                    ],
                                                ),
                                                html.Div(
                                                    children=[
                                                        dcc.Link(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="/acerca",
                                                            children=[
                                                                "Más Información →"
                                                            ],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-slate-50 mt-20 p-10 border-cyan-500 border-l-4",
                    children=[
                        html.H2(
                            className="mb-6 font-bold text-slate-900 text-3xl",
                            children=["¿Qué es Chicago Crime Prediction?"],
                        ),
                        html.P(
                            className="mb-4 text-slate-700 text-lg leading-relaxed",
                            children=[
                                "Este proyecto utiliza técnicas avanzadas de análisis de datos e inteligencia artificial para predecir patrones de criminalidad en la ciudad de Chicago. Nuestro objetivo es proporcionar herramientas útiles para la prevención del crimen y la toma de decisiones informadas basadas en evidencia."
                            ],
                        ),
                        html.P(
                            className="text-slate-700 text-lg leading-relaxed",
                            children=[
                                "Exploramos datos históricos de crímenes, identificamos tendencias y patrones complejos, y utilizamos modelos predictivos de última generación para ayudar a anticipar dónde y cuándo podrían ocurrir eventos delictivos en el futuro."
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ]
)
