html.Div(
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
                                                    d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        ),
                                        html.H1(
                                            className="font-bold text-4xl",
                                            children=["Mapa Interactivo de Delitos"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-200 text-xl leading-relaxed",
                                    children=[
                                        "Visualiza la distribución geográfica y temporal de los crímenes en Chicago. Explora patrones espaciales y observa la evolución de la criminalidad a través del tiempo."
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
                    className="gap-6 grid md:grid-cols-3 mb-8",
                    children=[
                        html.Div(
                            className="bg-white p-6 border border-slate-200 rounded-lg",
                            children=[
                                html.Div(
                                    className="flex items-center mb-3",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mr-3 rounded-lg w-12 h-12",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-7 h-7 text-cyan-600",
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
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-slate-900 text-lg",
                                            children=["Ubicación Precisa"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-600 text-sm",
                                    children=[
                                        "Cada punto en el mapa representa la ubicación exacta donde ocurrió un incidente criminal."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white p-6 border border-slate-200 rounded-lg",
                            children=[
                                html.Div(
                                    className="flex items-center mb-3",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mr-3 rounded-lg w-12 h-12",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-7 h-7 text-cyan-600",
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
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-slate-900 text-lg",
                                            children=["Línea de Tiempo"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-600 text-sm",
                                    children=[
                                        "Filtra y visualiza los crímenes según diferentes períodos de tiempo y observa patrones temporales."
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white p-6 border border-slate-200 rounded-lg",
                            children=[
                                html.Div(
                                    className="flex items-center mb-3",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-cyan-100 mr-3 rounded-lg w-12 h-12",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-7 h-7 text-cyan-600",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="2",
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-slate-900 text-lg",
                                            children=["Mapas de Calor"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-slate-600 text-sm",
                                    children=[
                                        "Identifica zonas de alta concentración delictiva mediante visualizaciones de densidad de calor."
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white shadow-sm p-8 border border-slate-200 rounded-lg",
                    children=[
                        html.Div(
                            className="mb-6",
                            children=[
                                html.Div(
                                    className="flex justify-between items-center mb-3",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H2(
                                                    className="mb-2 font-bold text-slate-900 text-3xl",
                                                    children=[
                                                        "Mapa Geoespacial de Criminalidad"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-slate-600 text-lg",
                                                    children=[
                                                        "Explora la distribución espacial y temporal de los delitos reportados en la ciudad de Chicago"
                                                    ],
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            className="hidden md:block",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-16 h-16 text-slate-300",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="1.5",
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="bg-slate-50 border-2 border-slate-300 rounded-lg w-full overflow-hidden",
                            style={"height": "850px"},
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
                    className="bg-linear-to-r from-slate-800 to-slate-700 shadow-xl mt-12 p-10 rounded-lg text-white",
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
                                            d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                ),
                                html.Span(children=["Cómo Interactuar con el Mapa"]),
                            ],
                        ),
                        html.Div(
                            className="gap-8 grid md:grid-cols-2",
                            children=[
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="mb-4 font-semibold text-cyan-300 text-xl",
                                            children=["Controles de Navegación"],
                                        ),
                                        html.Ul(
                                            className="space-y-3",
                                            children=[
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
                                                            fill="none",
                                                            stroke="currentColor",
                                                            viewBox="0 0 24 24",
                                                            children=[
                                                                dash_svg.Path(
                                                                    d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122",
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    strokeWidth="2",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=["Zoom:"],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Usa la rueda del ratón o los controles + / - para acercar o alejar el mapa"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
                                                            fill="none",
                                                            stroke="currentColor",
                                                            viewBox="0 0 24 24",
                                                            children=[
                                                                dash_svg.Path(
                                                                    d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11",
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    strokeWidth="2",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=[
                                                                        "Desplazar:"
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Haz clic y arrastra para moverte por diferentes áreas de Chicago"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
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
                                                        html.Span(
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=[
                                                                        "Detalles:"
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Pasa el cursor sobre los puntos para ver información detallada de cada incidente"
                                                                    ]
                                                                ),
                                                            ],
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
                                            className="mb-4 font-semibold text-cyan-300 text-xl",
                                            children=["Filtros y Línea de Tiempo"],
                                        ),
                                        html.Ul(
                                            className="space-y-3",
                                            children=[
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
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
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=[
                                                                        "Período:"
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Selecciona rangos de fechas para visualizar crímenes en períodos específicos"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
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
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=["Tipo:"],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Filtra por categorías de delitos para análisis más específicos"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.Li(
                                                    className="flex items-start",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="mt-0.5 mr-3 w-5 h-5 text-cyan-400 shrink-0",
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
                                                        html.Span(
                                                            className="text-slate-200",
                                                            children=[
                                                                html.Strong(
                                                                    className="text-white",
                                                                    children=[
                                                                        "Animación:"
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Reproduce la línea de tiempo para observar la evolución temporal de los crímenes"
                                                                    ]
                                                                ),
                                                            ],
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
                    className="gap-8 grid md:grid-cols-2 mt-12",
                    children=[
                        html.Div(
                            className="bg-white shadow-sm p-8 border border-slate-200 rounded-lg",
                            children=[
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-red-100 mr-3 rounded-lg w-12 h-12",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-7 h-7 text-red-600",
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
                                            className="font-bold text-slate-900 text-xl",
                                            children=["Patrones Geográficos"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="mb-4 text-slate-600",
                                    children=[
                                        "El mapa revela concentraciones significativas de criminalidad en ciertas zonas de Chicago:"
                                    ],
                                ),
                                html.Ul(
                                    className="space-y-2 text-slate-700",
                                    children=[
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-red-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Áreas del South Side muestran mayor densidad de incidentes"
                                                    ]
                                                ),
                                            ],
                                        ),
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-yellow-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "El centro (Loop) presenta patrones distintos relacionados con comercio"
                                                    ]
                                                ),
                                            ],
                                        ),
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-green-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Zonas residenciales del North Side tienen menor incidencia"
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white shadow-sm p-8 border border-slate-200 rounded-lg",
                            children=[
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        html.Div(
                                            className="flex justify-center items-center bg-blue-100 mr-3 rounded-lg w-12 h-12",
                                            children=[
                                                dash_svg.Svg(
                                                    className="w-7 h-7 text-blue-600",
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
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="font-bold text-slate-900 text-xl",
                                            children=["Patrones Temporales"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="mb-4 text-slate-600",
                                    children=[
                                        "La línea de tiempo permite identificar variaciones en la ocurrencia de crímenes:"
                                    ],
                                ),
                                html.Ul(
                                    className="space-y-2 text-slate-700",
                                    children=[
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-blue-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Incrementos nocturnos en ciertas categorías de delitos"
                                                    ]
                                                ),
                                            ],
                                        ),
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-blue-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Variaciones estacionales a lo largo del año"
                                                    ]
                                                ),
                                            ],
                                        ),
                                        html.Li(
                                            className="flex items-start",
                                            children=[
                                                html.Span(
                                                    className="mt-1 mr-2 text-blue-500",
                                                    children=["●"],
                                                ),
                                                html.Span(
                                                    children=[
                                                        "Patrones de fin de semana vs. días laborales"
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
                html.Div(
                    className="bg-slate-50 mt-12 p-8 border-slate-900 border-l-4 rounded",
                    children=[
                        html.H3(
                            className="flex items-center mb-4 font-bold text-slate-900 text-xl",
                            children=[
                                dash_svg.Svg(
                                    className="mr-2 w-6 h-6 text-slate-700",
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
                                ),
                                html.Span(children=["Fuente de Datos"]),
                            ],
                        ),
                        html.Div(
                            className="gap-6 grid md:grid-cols-3 text-slate-700",
                            children=[
                                html.Div(
                                    children=[
                                        html.P(
                                            className="mb-1 font-semibold text-slate-900",
                                            children=["Origen"],
                                        ),
                                        html.P(
                                            className="text-sm",
                                            children=[
                                                "Chicago Police Department - Datos públicos de criminalidad"
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.P(
                                            className="mb-1 font-semibold text-slate-900",
                                            children=["Actualización"],
                                        ),
                                        html.P(
                                            className="text-sm",
                                            children=[
                                                "Los datos se actualizan periódicamente para reflejar reportes recientes"
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.P(
                                            className="mb-1 font-semibold text-slate-900",
                                            children=["Cobertura"],
                                        ),
                                        html.P(
                                            className="text-sm",
                                            children=[
                                                "Incluye múltiples años de registros históricos georreferenciados"
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
    ]
)
