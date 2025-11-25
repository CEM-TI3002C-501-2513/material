import dash
import dash_svg
import httpx
from dash import Dash, html, dcc, callback, Output, Input, State
from datetime import datetime

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}
]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    title="Proyecto Thales",
    use_pages=True,
    use_async=True,
    # suppress_callback_exceptions=True,
)

header = html.Header(
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
                                dcc.Link(
                                    className="hover:text-cyan-400 transition-colors",
                                    href="/",
                                    children=["Chicago Crime Prediction"],
                                )
                            ],
                        ),
                        html.Ul(
                            className="flex space-x-6 text-sm",
                            children=[
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="pb-1 border-cyan-400 border-b-2 font-medium hover:text-cyan-400 transition-colors",
                                            href="/",
                                            children=["Inicio"],
                                            id="nav-home-link",
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="/tableros",
                                            children=["Tableros"],
                                            id="nav-tableros-link",
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="/prediccion",
                                            children=["Predicción"],
                                            id="nav-prediccion-link",
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="/mapa",
                                            children=["Mapa de Delitos"],
                                            id="nav-mapa-link",
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors",
                                            href="/acerca",
                                            children=["Acerca de"],
                                            id="nav-acerca-link",
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

footer = html.Footer(
    className="bg-slate-900 mt-20 py-12 text-white",
    children=[
        html.Div(
            className="mx-auto px-6 container",
            children=[
                html.Div(
                    className="text-center",
                    children=[
                        html.P(
                            className="mb-2 text-lg",
                            children=[
                                "© 2025 Chicago Crime Prediction - Proyecto Thales"
                            ],
                        ),
                        html.P(
                            className="text-slate-400",
                            children=[
                                "Análisis y predicción de crimen basado en datos históricos de Chicago"
                            ],
                        ),
                    ],
                )
            ],
        )
    ],
)

chatbot_button = html.Button(
    className="right-6 bottom-6 z-50 fixed flex justify-center items-center bg-linear-to-r from-cyan-500 hover:from-cyan-600 to-cyan-600 hover:to-cyan-700 shadow-2xl rounded-full w-16 h-16 text-white hover:scale-110 transition-all duration-300",
    id="chatbot_button",
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
    )

def bot_message(message):
    return html.Div(
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
                            dcc.Markdown(
                                className="text-slate-800 text-sm leading-relaxed",
                                children=[
                                    message
                                ],
                            )
                        ],
                    ),
                    html.P(
                        className="mt-1 ml-3 text-slate-500 text-xs",
                        children=[datetime.now().strftime("%I:%M %p")],
                    ),
                ],
            ),
        ],
    )
    
def user_message(message):
    return html.Div(
        className="flex justify-end items-start space-x-3",
        children=[
            html.Div(
                className="flex flex-col flex-1 items-end",
                children=[
                    html.Div(
                        className="bg-linear-to-r from-cyan-500 to-cyan-600 shadow-sm p-4 rounded-2xl rounded-tr-none max-w-[80%]",
                        children=[
                            dcc.Markdown(
                                className="text-white text-sm leading-relaxed",
                                children=[
                                    message
                                ],
                            )
                        ],
                    ),
                    html.P(
                        className="mt-1 mr-3 text-slate-500 text-xs",
                        children=[datetime.now().strftime("%I:%M %p")],
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
    )

chatbot_window = html.Div(
    className="hidden right-6 bottom-6 z-50 fixed flex-col bg-white shadow-2xl border border-slate-200 rounded-2xl w-96 h-[600px] overflow-hidden",
    id="chatbot_window",
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
                    id="close_chatbot_button",
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
            id="chat_container",
            children=[
                dcc.Loading(
                    children=[
                        html.Div(
                            id="chat_messages",
                            children=[
                                bot_message("¡Hola! 👋 Soy el Asistente del Proyecto Thales. Puedo ayudarte con información sobre predicción de crimen en Chicago, nuestros tableros y cómo usar la plataforma.")
                                ],
                            )
                        ],
                    overlay_style={"visibility": "visible", "filter": "blur(2px)"},
                    ),
                dcc.Store(id="chat_scroll_store", data={"scroll": "bottom"}),
                html.Div(id="chat_scroll_anchor", className="hidden"),
                ],
            ),
        html.Div(
            className="bg-white p-4 border-slate-200 border-t",
            children=[
                html.Div(
                    className="flex items-center space-x-2",
                    children=[
                        dcc.Input(
                            className="flex-grow px-3 py-2 border rounded-l-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm", 
                            id="chat_input",
                            type="text", 
                            placeholder="Escribe tu mensaje aquí..."),
                        html.Button(
                            className="bg-linear-to-r from-cyan-500 hover:from-cyan-600 to-cyan-600 hover:to-cyan-700 p-3 rounded-xl text-white transition-colors shrink-0",
                            id="send_chat_button",
                            children=[
                                dash_svg.Svg(
                                    className="w-5 h-5",
                                    fill="none",
                                    stroke="currentColor",
                                    viewBox="0 0 24 24",
                                    children=[
                                        dash_svg.Path(
                                            d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5",
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
            ],
        ),
    ],
)

@callback(
    Output("nav-home-link", "className"),
    Output("nav-tableros-link", "className"),
    Output("nav-prediccion-link", "className"),
    Output("nav-mapa-link", "className"),
    Output("nav-acerca-link", "className"),
    Input("active-url", "pathname"),
)
def update_active_link(pathname):
    base_class = "pb-1 border-transparent border-b-2 hover:text-cyan-400 transition-colors"
    active_class = "pb-1 border-cyan-400 border-b-2 font-medium hover:text-cyan-400 transition-colors"
    links = {
        "/": "nav-home-link",
        "/tableros": "nav-tableros-link",
        "/prediccion": "nav-prediccion-link",
        "/mapa": "nav-mapa-link",
        "/acerca": "nav-acerca-link",
    }
    return [
        active_class if pathname == path else base_class
        for path in links.keys()
    ]
    
@callback(
    Output("chatbot_button", "className"),
    Output("chatbot_window", "className"),
    Input("chatbot_button", "n_clicks"),
    Input("close_chatbot_button", "n_clicks"),
    State("chatbot_button", "className"),
    State("chatbot_window", "className"),
)
def toggle_chatbot(n_clicks_open, n_clicks_close, button_class, window_class):
    if n_clicks_open or n_clicks_close:
        if "hidden" in window_class:
            new_window_class = window_class.replace("hidden", "flex")
            new_button_class = button_class
        else:
            new_window_class = window_class.replace("flex", "hidden")
            new_button_class = button_class
        return new_button_class, new_window_class
    return button_class, window_class

app.layout = html.Div(
    className="bg-slate-100",
    children=[
        dcc.Location(id="active-url"),
        header,
        dash.page_container,
        chatbot_button,
        chatbot_window,
        footer
    ]
)

@callback(
    Output("chat_messages", "children"),
    Output("chat_input", "value"),
    Output("chat_scroll_store", "data"),
    Input("send_chat_button", "n_clicks"),
    Input("chat_input", "n_submit"),
    State("chat_input", "value"),
    State("chat_messages", "children"),
    prevent_initial_call=True
)
def handle_chat(n_clicks, n_submit, user_input, existing_messages):
    if (n_clicks or n_submit) and user_input:
        try:
            payload = {"prompt": user_input}
            response = httpx.post("http://localhost:8000/gemini_query", json=payload)
            response.raise_for_status()
            bot_reply = response.json().get("response", "Lo siento, no pude procesar tu solicitud en este momento.")
        except httpx.RequestError:
            bot_reply = "Lo siento, hubo un error al conectar con el servidor."
        except httpx.HTTPStatusError:
            bot_reply = "Lo siento, el servidor respondió con un error."
        existing_messages.append(user_message(user_input))
        existing_messages.append(bot_message(bot_reply))
    return existing_messages, "", {"scroll": "bottom"}

app.clientside_callback(
    """
    function(trigger) {
        const chatContainer = document.getElementById('chat_container');
        if (chatContainer) {
            chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: 'smooth' });
        }
        return null;
    }
    """,
    Output("chat_scroll_anchor", "children"),
    Input("chat_scroll_store", "data"),
)

if __name__ == "__main__":
    app.run(debug=True)