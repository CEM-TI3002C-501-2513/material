import dash
import dash_svg
from dash import html

dash.register_page(
    __name__,
    path="/acerca",
    title="Acerca del Proyecto Thales",
    name="acerca"
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
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-4 w-12 h-12 text-cyan-400",
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
                                        html.H1(
                                            className="font-bold text-4xl",
                                            children=["Acerca del Proyecto"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-200 text-xl leading-relaxed",
                                    children=[
                                        "Conoce más sobre el Proyecto Thales y cómo la tecnología está transformando el análisis de seguridad urbana"
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
                    className="bg-white shadow-sm mb-12 p-10 border border-slate-200 rounded-lg",
                    children=[
                        html.Div(
                            className="flex items-center mb-6",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-linear-to-brrom-cyan-500 to-blue-600 mr-4 rounded-lg w-16 h-16",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-9 h-9 text-white",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        )
                                    ],
                                ),
                                html.H2(
                                    className="font-bold text-slate-900 text-3xl",
                                    children=["Proyecto Thales"],
                                ),
                            ],
                        ),
                        html.Div(
                            className="max-w-none prose",
                            children=[
                                html.P(
                                    className="mb-4 text-slate-700 text-lg leading-relaxed",
                                    children=[
                                        "El",
                                        html.Strong(children=["Proyecto Thales"]),
                                        html.Span(
                                            children=[
                                                "es una iniciativa innovadora desarrollada en colaboración con"
                                            ]
                                        ),
                                        html.Strong(children=["Thales Group"]),
                                        html.Span(
                                            children=[
                                                ", empresa líder mundial en tecnología para los sectores aeroespacial, de defensa, seguridad y transporte. Este proyecto combina análisis de datos, inteligencia artificial y visualización geoespacial para proporcionar herramientas avanzadas de predicción y análisis de criminalidad en la ciudad de Chicago."
                                            ]
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="mb-4 text-slate-700 text-lg leading-relaxed",
                                    children=[
                                        "En alianza con Thales, reconocida por su experiencia en sistemas de seguridad y análisis predictivo a nivel global, hemos desarrollado una plataforma que aplica tecnologías de vanguardia al campo de la seguridad pública urbana, aprovechando el conocimiento y las mejores prácticas de la industria tecnológica."
                                    ],
                                ),
                                html.P(
                                    className="text-slate-700 text-lg leading-relaxed",
                                    children=[
                                        "A través de este sitio web, democratizamos el acceso a información crítica sobre patrones delictivos, permitiendo a autoridades, investigadores y ciudadanos tomar decisiones más informadas sobre seguridad urbana, respaldados por la excelencia técnica que caracteriza a Thales."
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="gap-8 grid md:grid-cols-2 mb-12",
                    children=[
                        html.Div(
                            className="bg-linear-to-br from-cyan-500 to-cyan-600 shadow-lg p-8 rounded-lg text-white",
                            children=[
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-3 w-10 h-10",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M13 10V3L4 14h7v7l9-11h-7z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-2xl",
                                            children=["Nuestra Misión"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-cyan-50 leading-relaxed",
                                    children=[
                                        "Desarrollar y proporcionar herramientas de análisis predictivo de criminalidad accesibles y precisas, que contribuyan a la prevención del crimen y mejoren la seguridad de las comunidades urbanas mediante el uso inteligente de datos históricos y tecnologías emergentes."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-linear-to-br from-slate-700 to-slate-800 shadow-lg p-8 rounded-lg text-white",
                            children=[
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-3 w-10 h-10",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                ),
                                                dash_svg.Path(
                                                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                ),
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-2xl",
                                            children=["Nuestra Visión"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-200 leading-relaxed",
                                    children=[
                                        "Convertirnos en un referente en el análisis predictivo de criminalidad urbana, expandiendo nuestras soluciones a múltiples ciudades y contribuyendo significativamente a la creación de comunidades más seguras a través de la ciencia de datos y la inteligencia artificial."
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white shadow-sm mb-12 p-10 border border-slate-200 rounded-lg",
                    children=[
                        html.H2(
                            className="flex items-center mb-8 font-bold text-slate-900 text-3xl",
                            children=[
                                dash_svg.Svg(
                                    className="mr-3 w-8 h-8 text-cyan-600",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                ),
                                html.Span(children=["Funcionalidades del Sitio"]),
                            ],
                        ),
                        html.Div(
                            className="gap-6 grid md:grid-cols-2",
                            children=[
                                html.Div(
                                    className="flex items-start space-x-4 bg-slate-50 p-4 rounded-lg",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-purple-100 rounded-lg w-12 h-12 shrink-0",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-6 h-6 text-purple-600",
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
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-bold text-slate-900",
                                                    children=["Tableros Interactivos"],
                                                ),
                                                html.P(
                                                    className="text-slate-600 text-sm",
                                                    children=[
                                                        "Visualizaciones dinámicas con Tableau Public que permiten explorar tendencias y estadísticas de criminalidad"
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4 bg-slate-50 p-4 rounded-lg",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-green-100 rounded-lg w-12 h-12 shrink-0",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-6 h-6 text-green-600",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
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
                                                html.H3(
                                                    className="mb-1 font-bold text-slate-900",
                                                    children=["Modelo Predictivo"],
                                                ),
                                                html.P(
                                                    className="text-slate-600 text-sm",
                                                    children=[
                                                        "Algoritmos de machine learning que predicen probabilidades de crímenes según zona, fecha y hora"
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4 bg-slate-50 p-4 rounded-lg",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-red-100 rounded-lg w-12 h-12 shrink-0",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-6 h-6 text-red-600",
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
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-1 font-bold text-slate-900",
                                                    children=["Mapas Geoespaciales"],
                                                ),
                                                html.P(
                                                    className="text-slate-600 text-sm",
                                                    children=[
                                                        "Visualización geográfica con línea de tiempo que muestra la distribución espacial y temporal de delitos"
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-start space-x-4 bg-slate-50 p-4 rounded-lg",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-blue-100 rounded-lg w-12 h-12 shrink-0",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-6 h-6 text-blue-600",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
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
                                                html.H3(
                                                    className="mb-1 font-bold text-slate-900",
                                                    children=["Datos Históricos"],
                                                ),
                                                html.P(
                                                    className="text-slate-600 text-sm",
                                                    children=[
                                                        "Acceso a análisis detallados basados en años de registros del Chicago Police Department"
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
                html.Div(
                    className="bg-linear-to-r from-slate-800 to-slate-700 shadow-xl mb-12 p-10 rounded-lg text-white",
                    children=[
                        html.H2(
                            className="flex items-center mb-8 font-bold text-3xl",
                            children=[
                                dash_svg.Svg(
                                    className="mr-3 w-8 h-8 text-cyan-400",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                ),
                                html.Span(children=["Tecnologías Utilizadas"]),
                            ],
                        ),
                        html.Div(
                            className="gap-6 grid md:grid-cols-2 lg:grid-cols-4",
                            children=[
                                html.Div(
                                    className="bg-white/10 backdrop-blur p-6 rounded-lg",
                                    children=[
                                        html.H3(
                                            className="mb-3 font-bold text-cyan-300 text-xl",
                                            children=["Frontend"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(children=["HTML5"]),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["Tailwind CSS v4"]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Diseño Responsive"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["Dash (Plotly)"]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="bg-white/10 backdrop-blur p-6 rounded-lg",
                                    children=[
                                        html.H3(
                                            className="mb-3 font-bold text-cyan-300 text-xl",
                                            children=["Backend"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(children=["Python"]),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(children=["FastAPI"]),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["REST APIs"]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="bg-white/10 backdrop-blur p-6 rounded-lg",
                                    children=[
                                        html.H3(
                                            className="mb-3 font-bold text-cyan-300 text-xl",
                                            children=["Ciencia de Datos"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(children=["Pandas"]),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["Scikit-learn"]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Machine Learning"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=[
                                                                "Análisis Predictivo"
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="bg-white/10 backdrop-blur p-6 rounded-lg",
                                    children=[
                                        html.H3(
                                            className="mb-3 font-bold text-cyan-300 text-xl",
                                            children=["Base de Datos"],
                                        ),
                                        html.Ul(
                                            className="space-y-2 text-slate-200",
                                            children=[
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["PostgreSQL"]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["Tableau Public"]
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-center",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mr-2 w-4 h-4 text-cyan-400",
                                                            fill="currentColor",
                                                            viewBox="0 0 20 20",
                                                            children=[
                                                                dash_svg.Path(
                                                                    clipRule="evenodd",
                                                                    d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                                                                    fillRule="evenodd",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            children=["SQL Queries"]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white/5 backdrop-blur mt-8 p-6 border border-white/10 rounded-lg",
                            children=[
                                html.H3(
                                    className="mb-4 font-bold text-cyan-300 text-lg",
                                    children=["Arquitectura del Sistema"],
                                ),
                                html.Div(
                                    className="gap-6 grid md:grid-cols-3 text-slate-200 text-sm",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=[
                                                        "📊 Procesamiento de Datos"
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "Pandas para manipulación eficiente de grandes volúmenes de datos históricos de criminalidad"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=["🤖 Modelos Predictivos"],
                                                ),
                                                html.P(
                                                    children=[
                                                        "Scikit-learn para entrenamiento de algoritmos de clasificación y regresión"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=[
                                                        "🚀 API de Alto Rendimiento"
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "FastAPI proporciona endpoints REST rápidos y documentados automáticamente"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=[
                                                        "💾 Almacenamiento Robusto"
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "PostgreSQL gestiona millones de registros georreferenciados con consultas optimizadas"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=[
                                                        "📈 Visualización Interactiva"
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "Dash y Tableau Public crean dashboards dinámicos y mapas interactivos"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            children=[
                                                html.P(
                                                    className="mb-2 font-semibold text-white",
                                                    children=[
                                                        "🔄 Integración Continua"
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "Pipeline completo desde la base de datos hasta la presentación de resultados"
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white shadow-sm mb-12 p-10 border border-slate-200 rounded-lg",
                    children=[
                        html.H2(
                            className="flex items-center mb-8 font-bold text-slate-900 text-3xl",
                            children=[
                                dash_svg.Svg(
                                    className="mr-3 w-8 h-8 text-cyan-600",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                ),
                                html.Span(children=["Metodología del Proyecto"]),
                            ],
                        ),
                        html.Div(
                            className="space-y-6",
                            children=[
                                html.Div(
                                    className="flex items-start space-x-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10 font-bold text-white text-lg shrink-0",
                                            children=["1"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-2 font-bold text-slate-900 text-xl",
                                                    children=["Recopilación de Datos"],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Obtención de datos históricos de criminalidad del Chicago Police Department, incluyendo ubicación, tipo de delito, fecha y hora de cada incidente."
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
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10 font-bold text-white text-lg shrink-0",
                                            children=["2"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-2 font-bold text-slate-900 text-xl",
                                                    children=[
                                                        "Limpieza y Preprocesamiento"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Procesamiento de datos para eliminar inconsistencias, normalizar formatos y preparar el conjunto de datos para análisis estadístico y modelado."
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
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10 font-bold text-white text-lg shrink-0",
                                            children=["3"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-2 font-bold text-slate-900 text-xl",
                                                    children=["Análisis Exploratorio"],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Identificación de patrones, tendencias y correlaciones en los datos mediante técnicas estadísticas y visualización de información."
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
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10 font-bold text-white text-lg shrink-0",
                                            children=["4"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-2 font-bold text-slate-900 text-xl",
                                                    children=[
                                                        "Desarrollo de Modelos Predictivos"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Entrenamiento de algoritmos de machine learning para predecir probabilidades de criminalidad basándose en variables espaciales y temporales."
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
                                            className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10 font-bold text-white text-lg shrink-0",
                                            children=["5"],
                                        ),
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="mb-2 font-bold text-slate-900 text-xl",
                                                    children=[
                                                        "Visualización y Presentación"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-slate-600",
                                                    children=[
                                                        "Creación de dashboards interactivos y mapas geoespaciales que facilitan la interpretación y uso práctico de los resultados del análisis."
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
                html.Div(
                    className="bg-slate-50 mb-12 p-8 border-cyan-500 border-l-4 rounded",
                    children=[
                        html.H3(
                            className="flex items-center mb-4 font-bold text-slate-900 text-2xl",
                            children=[
                                dash_svg.Svg(
                                    className="mr-3 w-7 h-7 text-cyan-600",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                ),
                                html.Span(children=["Fuente de Datos"]),
                            ],
                        ),
                        html.P(
                            className="mb-4 text-slate-700 leading-relaxed",
                            children=[
                                "Este proyecto utiliza datos públicos proporcionados por el",
                                html.Strong(children=["Chicago Police Department"]),
                                html.Span(
                                    children=[
                                        "a través del portal de datos abiertos de la ciudad de Chicago. El dataset incluye registros detallados de incidentes criminales reportados, con información georreferenciada y clasificación por tipo de delito."
                                    ]
                                ),
                            ],
                        ),
                        html.Div(
                            className="gap-4 grid md:grid-cols-2 text-sm",
                            children=[
                                html.Div(
                                    className="flex items-center text-slate-700",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-2 w-5 h-5 text-cyan-600",
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
                                                html.Strong(children=["Cobertura:"]),
                                                html.Span(
                                                    children=[
                                                        "Múltiples años de registros históricos"
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-center text-slate-700",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-2 w-5 h-5 text-cyan-600",
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
                                                html.Strong(
                                                    children=["Actualización:"]
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Datos actualizados periódicamente"
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-center text-slate-700",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-2 w-5 h-5 text-cyan-600",
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
                                                html.Strong(children=["Volumen:"]),
                                                html.Span(
                                                    children=[
                                                        "Cientos de miles de registros"
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex items-center text-slate-700",
                                    children=[
                                        dash_svg.Svg(
                                            className="mr-2 w-5 h-5 text-cyan-600",
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
                                                html.Strong(children=["Acceso:"]),
                                                html.Span(
                                                    children=["Open Data de Chicago"]
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-yellow-50 p-8 border-yellow-500 border-l-4 rounded",
                    children=[
                        html.Div(
                            className="flex items-start",
                            children=[
                                dash_svg.Svg(
                                    className="mt-0.5 mr-3 w-7 h-7 text-yellow-600 shrink-0",
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
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="mb-2 font-bold text-yellow-900 text-xl",
                                            children=["Aviso Importante"],
                                        ),
                                        html.P(
                                            className="text-yellow-800 leading-relaxed",
                                            children=[
                                                "Las predicciones y análisis proporcionados por este sitio tienen fines educativos e informativos. Los resultados se basan en datos históricos y modelos estadísticos que, aunque precisos, no garantizan la ocurrencia o ausencia de eventos futuros. Esta herramienta no debe utilizarse como única base para decisiones críticas de seguridad. Siempre consulte con autoridades locales y profesionales en seguridad pública para obtener información actualizada y recomendaciones específicas."
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ]
)
