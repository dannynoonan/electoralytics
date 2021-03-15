import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar, data_obj


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Project sources & notes"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=2),
                dbc.Col(md=8, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Visualizing Jim Crow Voter Suppression", className="card-title"),
                            html.P(className="card-text", children=[
                                html.B("Books:"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935)",
                                    ]),
                                    html.Li(children=[
                                        "Henry Louis Gates, Jr., ", html.I("Stony the Road: Reconstruction, White Supremacy, and the Rise of Jim Crow"), " (2019)",
                                    ]),
                                    html.Li(children=[
                                        "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020)"
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020)",
                                    ]),
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Podcasts:"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "Ramtin Arablouei and Rund Abdelfatah (Hosts), Lawrence Wu (Producer), “The Electoral College” (Oct. 15, 2020) [Audio podcast episode] ",
                                        html.I("NPR"), " “Throughline”"
                                        # https://www.npr.org/2020/09/30/918717270/the-electoral-college
                                    ]),
                                ])
                            ]),
                            html.P(className="card-text", children=[
                                html.B("Citations:"),
                                html.Ol(children=[
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 17",
                                    ]),
                                    html.Li(children=[
                                        "Ramtin Arablouei and Rund Abdelfatah (Hosts), Lawrence Wu (Producer), “The Electoral College” (Oct. 15, 2020) [Audio podcast episode] ",
                                        html.I("NPR"), " “Throughline”"
                                        # https://www.npr.org/2020/09/30/918717270/the-electoral-college
                                    ]),
                                    html.Li(children=[
                                        "John P. Roche, “The Founding Fathers: A Reform Caucus in Action”, ", html.I("American Political Science Review"), 
                                        ", Vol. 55, No. 4 (Dec., 1961), p. 811",
                                        # https://pdfs.semanticscholar.org/b3ff/15fe35ed640a80875519e4ed7777d969102f.pdf?_ga=2.183925857.653257014.1615793773-371115737.1615793773
                                    ]),
                                    html.Li(children=[
                                        "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020), p. 171"
                                    ]),
                                    html.Li(children=[
                                        "George Mason, ", html.I("Notes of the Debates in the Federal Convention of 1787"), ", p. 266, transcribed by Jesse Wegman in ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 71",
                                    ]),
                                    html.Li(children=[
                                        "Wendell Phillips, ", html.I("Speech to Massachusetts Anti-Slavery Society"), ", (1865), transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 199-200",
                                    ]),
                                    html.Li(children=[
                                        "Frederick Douglass, ", html.I("Speech to Massachusetts Anti-Slavery Society"), ", (1865), transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 200",
                                    ]),
                                    html.Li(children=[
                                        "Carl Schurz, ", html.I("Report on the Condition of the South"), ", (1865), transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 203",
                                        # https://wwnorton.com/college/history/america9/brief/docs/CSchurz-South_Report-1865.pdf
                                    ]),
                                    html.Li(children=[
                                        "John F. Cook, ", html.I("Congressional Globe"), ", 39th Congress (1866), 1st Session, Part 1, p. 183, transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 285",
                                    ]),
                                    html.Li(children=[
                                        "W.E.B. Du Bois in ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 185",
                                    ]),
                                    html.Li(children=[
                                        "Final Report of the Congressional Joint Committee on Reconstruction (1866), via Edward McPherson, ", 
                                        html.I("The Political History of the United States of America During the Period of Reconstruction"), ", (1871), p. 88-93, transcribed by \
                                        W.E.B. Du Bois in ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 311-312",
                                    ]),
                                    html.Li(children=[
                                        html.I("Fourteenth Amendment"), ", Section 2 (1868)",
                                        # https://en.wikipedia.org/wiki/Fourteenth_Amendment_to_the_United_States_Constitution#Section_2:_Apportionment_of_Representatives
                                    ]),
                                    html.Li(children=[
                                        "Charles Sumner, Final speech in the U.S. Senate on Fourteenth Amendment, transcribed by Elias Nason in ", 
                                        html.I("The Life and Times of Charles Sumner: His Boyhood, Education and Public Career"), " (1874), p. 307",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 108",
                                    ]),
                                    html.Li(children=[
                                        "William Lloyd Garrison, ", html.I("Life of Garrison, IV"), " (1861-1879), p. 123-124, transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 200-201",
                                    ]),
                                    html.Li(children=[
                                        "Henry Louis Gates, Jr., ", html.I("Stony the Road: Reconstruction, White Supremacy, and the Rise of Jim Crow"), " (2019), p. 186",
                                    ]),
                                    html.Li(children=[
                                        "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020), p. 189-190"
                                    ]),
                                    html.Li(children=[
                                        "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020), p. 189"
                                    ]),
                                    html.Li(children=[
                                        "C. Vann Woodward, “The Anachronistic Electoral System”,", html.I("New Republic"), " June 1, 1968 p. 44-45, cited by Jesse Wegman in ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 118",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 109-110",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 123",
                                    ]),
                                ])
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=2),
            ])
        ])
    ])
])