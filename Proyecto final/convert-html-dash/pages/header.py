html.Header(
    className="top-0 z-50 sticky bg-slate-900 shadow-md text-white",
    children=[
        html.Nav(
            className="mx-auto px-6 py-3 container",
            children=[
                html.Div(
                    className="flex justify-between items-center",
                    children=[
                        html.Div(
                            className="font-bold text-xl tracking-tight",
                            children=[
                                html.A(
                                    className="hover:text-cyan-400 transition-colors",
                                    href="index.html",
                                    children=["Chicago Crime Prediction"],
                                )
                            ],
                        ),
                        html.Ul(
                            className="flex space-x-6 text-sm",
                            children=[
                                html.Li(
                                    children=[
                                        html.A(
                                            className="pb-1 border-cyan-400 border-b-2 font-medium hover:text-cyan-400 transition-colors",
                                            href="index.html",
                                            children=["Inicio"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="tableros.html",
                                            children=["Tableros"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="prediccion.html",
                                            children=["Predicción"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="mapa.html",
                                            children=["Mapa de Delitos"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="acerca.html",
                                            children=["Acerca de"],
                                        )
                                    ]
                                ),
                            ],
                        ),
                    ],
                )
            ],
        )
    ],
)
