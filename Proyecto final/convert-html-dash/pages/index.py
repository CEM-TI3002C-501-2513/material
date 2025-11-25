html.Div(
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
                                        html.A(
                                            className="bg-cyan-500 hover:bg-cyan-600 px-8 py-3 font-semibold text-white transition-colors",
                                            href="prediccion.html",
                                            children=["Hacer una Predicción →"],
                                        ),
                                        html.A(
                                            className="hover:bg-white/10 px-8 py-3 border-2 border-white font-semibold text-white transition-colors",
                                            href="tableros.html",
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
                                                    src="images/tableros.jpg",
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
                                                        html.A(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="tableros.html",
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
                                                    src="images/prediccion.jpg",
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
                                                        html.A(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="prediccion.html",
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
                                                    src="images/mapa.jpg",
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
                                                        html.A(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="mapa.html",
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
                                                    src="images/acerca.jpg",
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
                                                        html.A(
                                                            className="inline-block bg-slate-900 hover:bg-cyan-500 px-8 py-3 font-semibold text-white transition-colors",
                                                            href="acerca.html",
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
        html.Button(
            className="right-6 bottom-6 z-50 fixed flex justify-center items-center bg-linear-to-r from-cyan-500 hover:from-cyan-600 to-cyan-600 hover:to-cyan-700 shadow-2xl rounded-full w-16 h-16 text-white hover:scale-110 transition-all duration-300",
            id="chatbotButton",
            children=[
                dash_svg.Svg(
                    className="w-8 h-8",
                    fill="none",
                    stroke="currentColor",
                    viewBox="0 0 24 24",
                    children=[
                        dash_svg.Path(
                            d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z",
                            strokeLinecap="round",
                            strokeLinejoin="round",
                            strokeWidth="2",
                        )
                    ],
                )
            ],
        ),
        html.Div(
            className="hidden right-6 bottom-6 z-50 fixed flex-col bg-white shadow-2xl border border-slate-200 rounded-2xl w-96 h-[600px] overflow-hidden",
            id="chatbotWindow",
            children=[
                html.Div(
                    className="flex justify-between items-center bg-linear-to-r from-slate-900 to-slate-800 p-4 text-white",
                    children=[
                        html.Div(
                            className="flex items-center space-x-3",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-500 rounded-full w-10 h-10",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-6 h-6",
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
                                            className="font-bold text-lg",
                                            children=["Asistente Thales"],
                                        ),
                                        html.P(
                                            className="text-cyan-300 text-xs",
                                            children=["En línea"],
                                        ),
                                    ]
                                ),
                            ],
                        ),
                        html.Button(
                            className="hover:bg-white/10 p-2 rounded-lg transition-colors",
                            id="closeChatbot",
                            children=[
                                dash_svg.Svg(
                                    className="w-5 h-5",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M6 18L18 6M6 6l12 12",
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            strokeWidth="2",
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="flex-1 space-y-4 bg-slate-50 p-4 overflow-y-auto",
                    children=[
                        html.Div(
                            className="flex items-start space-x-3",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 shrink-0",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-5 h-5 text-white",
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
                                    className="flex-1",
                                    children=[
                                        html.Div(
                                            className="bg-white shadow-sm p-4 border border-slate-200 rounded-2xl rounded-tl-none",
                                            children=[
                                                html.P(
                                                    className="text-slate-800 text-sm leading-relaxed",
                                                    children=[
                                                        "¡Hola! 👋 Soy el Asistente del Proyecto Thales. Puedo ayudarte con información sobre predicción de crimen en Chicago, nuestros tableros y cómo usar la plataforma."
                                                    ],
                                                )
                                            ],
                                        ),
                                        html.P(
                                            className="mt-1 ml-3 text-slate-500 text-xs",
                                            children=["10:24 AM"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="flex items-start space-x-3",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 shrink-0",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-5 h-5 text-white",
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
                                    className="flex-1",
                                    children=[
                                        html.Div(
                                            className="bg-white shadow-sm p-4 border border-slate-200 rounded-2xl rounded-tl-none",
                                            children=[
                                                html.P(
                                                    className="mb-3 text-slate-800 text-sm leading-relaxed",
                                                    children=[
                                                        "¿En qué puedo ayudarte hoy? Puedes preguntarme sobre:"
                                                    ],
                                                ),
                                                html.Div(
                                                    className="space-y-2",
                                                    children=[
                                                        html.Button(
                                                            className="group bg-slate-50 hover:bg-cyan-50 p-3 border border-slate-200 hover:border-cyan-300 rounded-lg w-full text-left transition-colors",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center space-x-2",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="w-4 h-4 text-slate-500 group-hover:text-cyan-600",
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
                                                                            className="font-medium text-slate-700 group-hover:text-cyan-700 text-sm",
                                                                            children=[
                                                                                "Ver estadísticas de crimen"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        html.Button(
                                                            className="group bg-slate-50 hover:bg-cyan-50 p-3 border border-slate-200 hover:border-cyan-300 rounded-lg w-full text-left transition-colors",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center space-x-2",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="w-4 h-4 text-slate-500 group-hover:text-cyan-600",
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
                                                                        html.Span(
                                                                            className="font-medium text-slate-700 group-hover:text-cyan-700 text-sm",
                                                                            children=[
                                                                                "Hacer una predicción"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        html.Button(
                                                            className="group bg-slate-50 hover:bg-cyan-50 p-3 border border-slate-200 hover:border-cyan-300 rounded-lg w-full text-left transition-colors",
                                                            children=[
                                                                html.Div(
                                                                    className="flex items-center space-x-2",
                                                                    children=[
                                                                        dash_svg.Svg(
                                                                            className="w-4 h-4 text-slate-500 group-hover:text-cyan-600",
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
                                                                            className="font-medium text-slate-700 group-hover:text-cyan-700 text-sm",
                                                                            children=[
                                                                                "Conocer el proyecto"
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
                                        html.P(
                                            className="mt-1 ml-3 text-slate-500 text-xs",
                                            children=["10:24 AM"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="flex justify-end items-start space-x-3",
                            children=[
                                html.Div(
                                    className="flex flex-col flex-1 items-end",
                                    children=[
                                        html.Div(
                                            className="bg-linear-to-r from-cyan-500 to-cyan-600 shadow-sm p-4 rounded-2xl rounded-tr-none max-w-[80%]",
                                            children=[
                                                html.P(
                                                    className="text-white text-sm leading-relaxed",
                                                    children=[
                                                        "¿Cómo puedo hacer una predicción de crimen?"
                                                    ],
                                                )
                                            ],
                                        ),
                                        html.P(
                                            className="mt-1 mr-3 text-slate-500 text-xs",
                                            children=["10:25 AM"],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="flex justify-center items-center bg-slate-700 rounded-full w-8 h-8 shrink-0",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-5 h-5 text-white",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        )
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="flex items-start space-x-3",
                            children=[
                                html.Div(
                                    className="flex justify-center items-center bg-cyan-500 rounded-full w-8 h-8 shrink-0",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-5 h-5 text-white",
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
                                    className="flex-1",
                                    children=[
                                        html.Div(
                                            className="bg-white shadow-sm p-4 border border-slate-200 rounded-2xl rounded-tl-none",
                                            children=[
                                                html.P(
                                                    className="mb-3 text-slate-800 text-sm leading-relaxed",
                                                    children=[
                                                        "¡Excelente pregunta! Para hacer una predicción de crimen, sigue estos pasos:"
                                                    ],
                                                ),
                                                html.Ol(
                                                    className="space-y-2 ml-4 text-slate-700 text-sm list-decimal",
                                                    children=[
                                                        html.Li(
                                                            children=[
                                                                "Ve a la página de",
                                                                html.Strong(
                                                                    children=[
                                                                        "Predicción"
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Selecciona la",
                                                                html.Strong(
                                                                    children=[
                                                                        "zona (Ward)"
                                                                    ]
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "de Chicago"
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Elige la",
                                                                html.Strong(
                                                                    children=["fecha"]
                                                                ),
                                                                html.Span(
                                                                    children=["y"]
                                                                ),
                                                                html.Strong(
                                                                    children=["hora"]
                                                                ),
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Haz clic en",
                                                                html.Strong(
                                                                    children=[
                                                                        "'Generar Predicción'"
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="mt-3 pt-3 border-slate-200 border-t",
                                                    children=[
                                                        html.A(
                                                            className="inline-flex items-center space-x-2 font-medium text-cyan-600 hover:text-cyan-700 text-sm",
                                                            href="prediccion.html",
                                                            children=[
                                                                html.Span(
                                                                    children=[
                                                                        "Ir a Predicción"
                                                                    ]
                                                                ),
                                                                dash_svg.Svg(
                                                                    className="w-4 h-4",
                                                                    fill="none",
                                                                    stroke="currentColor",
                                                                    viewBox="0 0 24 24",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            d="M13 7l5 5m0 0l-5 5m5-5H6",
                                                                            strokeLinecap="round",
                                                                            strokeLinejoin="round",
                                                                            strokeWidth="2",
                                                                        )
                                                                    ],
                                                                ),
                                                            ],
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.P(
                                            className="mt-1 ml-3 text-slate-500 text-xs",
                                            children=["10:25 AM"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white p-4 border-slate-200 border-t",
                    children=[
                        html.Div(
                            className="flex items-center space-x-2",
                            children=[
                                html.Button(
                                    className="bg-linear-to-r from-cyan-500 hover:from-cyan-600 to-cyan-600 hover:to-cyan-700 p-3 rounded-xl text-white transition-colors shrink-0",
                                    children=[
                                        dash_svg.Svg(
                                            className="w-5 h-5",
                                            fill="none",
                                            stroke="currentColor",
                                            viewBox="0 0 24 24",
                                            children=[
                                                dash_svg.Path(
                                                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8",
                                                    strokeLinecap="round",
                                                    strokeLinejoin="round",
                                                    strokeWidth="2",
                                                )
                                            ],
                                        )
                                    ],
                                )
                            ],
                        ),
                        html.P(
                            className="mt-2 text-slate-500 text-xs text-center",
                            children=["Presiona Enter para enviar"],
                        ),
                    ],
                ),
            ],
        ),
        html.Script(
            children=[
                """
                // Chatbot toggle functionality
                const chatbotButton = document.getElementById('chatbotButton');
                const chatbotWindow = document.getElementById('chatbotWindow');
                const closeChatbot = document.getElementById('closeChatbot');

                chatbotButton.addEventListener('click', () => {
                    chatbotWindow.classList.toggle('hidden');
                    chatbotWindow.classList.toggle('flex');
                });

                closeChatbot.addEventListener('click', () => {
                    chatbotWindow.classList.add('hidden');
                    chatbotWindow.classList.remove('flex');
                });
                """
            ]
        ),
    ]
)
