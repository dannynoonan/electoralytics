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
                            # html.P(className="card-text", children=[
                            #     html.B("Books:"),
                            #     html.Ul(children=[
                            #         html.Li(children=[
                            #             "Michelle Alexander, ", html.I("The New Jim Crow: Mass Incarceration in the Age of Colorblindness"), " (2010)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Akhil Reed Amar, ", html.I("The Law of the Land: A Grand Tour of our Constitutional Republic"), " (2015)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Frederick Douglass, ", html.I("Life and Times of Frederick Douglass"), " (1892)"
                            #         ]),
                            #         html.Li(children=[
                            #             "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935)"
                            #         ]),                  
                            #         html.Li(children=[
                            #             "Henry Louis Gates, Jr., ", html.I("Stony the Road: Reconstruction, White Supremacy, and the Rise of Jim Crow"), " (2019)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Ibram X. Kendi, ", html.I("Stamped From the Beginning"), " (2016)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Richard Rothstein, ", html.I("The Color of Law"), " (2017)"
                            #         ]),
                            #         html.Li(children=[
                            #             "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020)"
                            #         ]),
                            #     ])
                            # ]),
                            # html.P(className="card-text", children=[
                            #     html.B("Podcasts:"),
                            #     html.Ul(children=[
                            #         html.Li(children=[
                            #             "Ramtin Arablouei and Rund Abdelfatah (Hosts), Akhil Reed Amar (Guest), Lawrence Wu (Producer), “The Electoral College” (Oct. 15, 2020) \
                            #             [Audio podcast episode] ", html.I("NPR"), " “Throughline”"
                            #             # https://www.npr.org/2020/09/30/918717270/the-electoral-college
                            #         ]),
                            #         html.Li(children=[
                            #             "Terry Gross (Host), Adam Jentleson (Guest), “The Racist History Of The Senate Filibuster” (Jan. 12 2021) [Audio podcast episode] ",
                            #             html.I("NPR"), " “Fresh Air"
                            #             # https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster
                            #         ]),
                            #     ])
                            # ]),
                            html.P(className="card-text", children=[
                                html.B("Citations:"),
                                html.Ol(children=[
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 17",
                                    ]),
                                    html.Li(children=[
                                        "Ramtin Arablouei and Rund Abdelfatah (Hosts), Akhil Reed Amar (Guest), Lawrence Wu (Producer), “The Electoral College” (Oct. 15, 2020) \
                                        [Audio podcast episode] ", html.I("NPR"), " “Throughline”"
                                        # https://www.npr.org/2020/09/30/918717270/the-electoral-college
                                    ]),
                                    html.Li(children=[
                                        "John P. Roche, “The Founding Fathers: A Reform Caucus in Action”, ", html.I("American Political Science Review"), 
                                        ", Vol. 55, No. 4 (Dec. 1961), p. 811",
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
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 191-195",
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
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 213-215",
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
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 294-296, 306, 308-310, 329-333",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 108",
                                    ]),
                                    html.Li(children=[
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 371",
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
                                        "Ibram X. Kendi, ", html.I("Stamped From the Beginning"), " (2016), p. 273; Henry Louis Gates, Jr., ", html.I("Stony the Road: \
                                        Reconstruction, White Supremacy, and the Rise of Jim Crow"), " (2019), p. 28; W.E.B. Du Bois, ", html.I("Black Reconstruction in \
                                        America: 1860-1880"), " (1935), p. 412, 449-450",
                                    ]),
                                    html.Li(children=[
                                        "Alexander Keyssar, ", html.I("Why Do We Still Have the Electoral College?"), " (2020), p. TODO"
                                    ]),
                                    html.Li(children=[
                                        "“State Voting Bills Tracker 2021”, ", html.I("Brennan Center for Justice"), " (Feb 24, 2021)",
                                        # https://www.brennancenter.org/our-work/research-reports/state-voting-bills-tracker-2021
                                    ]),
                                    html.Li(children=[
                                        "Akhil Reed Amar, ", html.I("The Law of the Land: A Grand Tour of our Constitutional Republic"), " (2015), p. 51"
                                    ]), 
                                    html.Li(children=[
                                        "Paul Finkleman, ", html.I("Slavery and the Founders: Race and Liberty in the Age of Jefferson"), " (1996), p. 14; Jesse Wegman, ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 66-67"
                                    ]),   
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 109-110",
                                    ]),  
                                    html.Li(children=[
                                        "E. W. Hutter, “The Nation's Great Triumph”, ", html.I("Philadelphia Press"), " (April 10, 1865), p. 4",
                                        # https://newspaperarchive.com/politics-clipping-apr-10-1865-2081429/
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 106-107",
                                    ]),  
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), “The Racist History Of The Senate Filibuster” (Jan. 12 2021) [Audio podcast episode] ",
                                        html.I("NPR"), " “Fresh Air”, [16:45 - 17:50]"
                                        # https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster
                                    ]),
                                    html.Li(children=[
                                        "Frederick Douglass, ", html.I("Life and Times of Frederick Douglass"), " (1892), p. 280-282",
                                    ]),
                                    html.Li(children=[
                                        "C. Vann Woodward, “The Anachronistic Electoral System”, ", html.I("New Republic"), " (June 1, 1968), p. 44-45, cited by Jesse Wegman in ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 118",
                                    ]),
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), “The Racist History Of The Senate Filibuster” (Jan. 12 2021) [Audio podcast episode] ",
                                        html.I("NPR"), " “Fresh Air”, [21:15 - 23:30]"
                                        # https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster
                                    ]),
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), “The Racist History Of The Senate Filibuster” (Jan. 12 2021) [Audio podcast episode] ",
                                        html.I("NPR"), " “Fresh Air”, [23:30 - 25:00]"
                                        # https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster
                                    ]),
                                    html.Li(children=[
                                        "Richard Rothstein, ", html.I("The Color of Law"), " (2017), p. 63-67",
                                    ]),
                                    html.Li(children=[
                                        "Richard Rothstein, ", html.I("The Color of Law"), " (2017), p. 54-56, p. 128-131",
                                    ]),
                                    html.Li(children=[
                                        "Juan F. Perea, “The Echoes of Slavery: Recognizing the Racist Origins of the Agricultural and Domestic Worker Exclusion from the \
                                        National Labor Relations Act”, ", html.I("Ohio State Law Journal"), ", Vol. 72:1 (2011), p. 104-109",
                                    ]),
                                    html.Li(children=[
                                        "Rachel E. Greenspan, “'It's the Legacy of Slavery': Here's the Troubling History Behind Tipping Practices in the U.S.”, ", 
                                        html.I("Time"), " (Oct. 15 2018), p. 104-109",
                                        # https://time.com/5404475/history-tipping-american-restaurants-civil-war/
                                    ]),
                                    html.Li(children=[
                                        "Michelle Alexander, ", html.I("The New Jim Crow: Mass Incarceration in the Age of Colorblindness"), " (2010), p. 35-36, 80, \
                                        86-88, 97, 140-143"
                                    ]),
                                    html.Li(children=[
                                        "Akhil Reed Amar, ", html.I("The Law of the Land: A Grand Tour of our Constitutional Republic"), " (2015), p. 109"
                                    ]),
                                    html.Li(children=[
                                        "Ibram X. Kendi, ", html.I("Stamped From the Beginning"), " (2016), p. 311-312"
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