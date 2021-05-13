import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_pages.components import navbar


content = html.Div([
    navbar,
    dbc.Card(className="bg-success", children=[
        dbc.CardBody([
            html.Br(),
            dbc.Row(className="text-white", justify="center", align="center", children=[
                html.H3("Project sources"),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(md=2),
                dbc.Col(md=8, children=[
                    dbc.Card(className="border-success", children=[
                        dbc.CardBody([
                            html.H4("Visualizing the “Jim Crow Power” through Electoral College data", className="card-title"),
                            html.P(className="card-text", children=[
                                html.B("Citations:"),
                                html.Ol(children=[
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 17",
                                    ]),
                                    html.Li(children=[
                                        "Ramtin Arablouei and Rund Abdelfatah (Hosts), Akhil Reed Amar (Guest), ", dcc.Link("“The Electoral College”",
                                        href="https://www.npr.org/2020/09/30/918717270/the-electoral-college", target="_blank"), " (Oct. 15, 2020) [Audio podcast episode], ", 
                                        html.I("NPR"), " “Throughline”, [39:00 - 41:05]"
                                    ]),
                                    html.Li(children=[
                                        "John P. Roche, ", dcc.Link("“The Founding Fathers: A Reform Caucus in Action”", target="_blank",
                                        href="https://pdfs.semanticscholar.org/b3ff/15fe35ed640a80875519e4ed7777d969102f.pdf?_ga=2.183925857.653257014.1615793773-371115737.1615793773"), 
                                        ", ", html.I("American Political Science Review"), ", Vol. 55, No. 4 (Dec. 1961), p. 811",
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
                                        dcc.Link("“Black Soldiers in the U.S. Military During the Civil War”", target="_blank", 
                                        href="https://www.archives.gov/education/lessons/blacks-civil-war"), ", ", html.I("National Archives"), " (last reviewed Sep. 1 2017)",
                                    ]),
                                    html.Li(children=[
                                        "Frederick Douglass, ", html.I("Speech to Massachusetts Anti-Slavery Society"), ", (1865), transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 200",
                                    ]),
                                    html.Li(children=[
                                        "Carl Schurz, ", html.I(children=[dcc.Link("Report on the Condition of the South", target="_blank", 
                                        href="https://wwnorton.com/college/history/america9/brief/docs/CSchurz-South_Report-1865.pdf")]), ", (1865), transcribed by W.E.B. Du \
                                        Bois in ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 203",
                                    ]),
                                    html.Li(children=[
                                        "John F. Cook, ", html.I("Congressional Globe"), ", 39th Congress (1866), 1st Session, Part 1, p. 183, transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 285",
                                    ]),
                                    html.Li(children=[
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 213-215",
                                    ]),
                                    html.Li(children=[
                                        "Eric Foner, ", html.I("The Second Founding: How the Civil War and Reconstruction Remade the Constitution"), " (2019), p. 61",
                                    ]),
                                    html.Li(children=[
                                        "Final Report of the Congressional Joint Committee on Reconstruction (1866), via Edward McPherson, ", 
                                        html.I("The Political History of the United States of America During the Period of Reconstruction"), ", (1871), p. 88-93, transcribed by \
                                        W.E.B. Du Bois in ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 311-312",
                                    ]),
                                    html.Li(children=[
                                        html.I(children=[dcc.Link("Fourteenth Amendment, Section 2", href="https://constitution.congress.gov/browse/amendment-14/section-2/",
                                        target="_blank")]), " (1868)",
                                    ]),
                                    html.Li(children=[
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 294-296, 306, 308-310, 329-333",
                                    ]),
                                    html.Li(children=[
                                        "W.E.B. Du Bois, ", html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 371",
                                    ]),
                                    html.Li(children=[
                                        "William Lloyd Garrison, ", html.I("Life of Garrison, IV"), " (1861-1879), p. 123-124, transcribed by W.E.B. Du Bois in ", 
                                        html.I("Black Reconstruction in America: 1860-1880"), " (1935), p. 200-201",
                                    ]),
                                    html.Li(children=[
                                        "Eric Foner, ", html.I("The Second Founding: How the Civil War and Reconstruction Remade the Constitution"), " (2019), p. 105, 164-165",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 108",
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
                                        dcc.Link("“State Voting Bills Tracker 2021”", target="_blank",
                                        href="https://www.brennancenter.org/our-work/research-reports/state-voting-bills-tracker-2021"), ", ", 
                                        html.I("Brennan Center for Justice"), " (Feb 24, 2021)",
                                    ]),
                                    html.Li(children=[
                                        "Akhil Reed Amar, ", html.I("The Law of the Land: A Grand Tour of our Constitutional Republic"), " (2015), p. 51"
                                    ]), 
                                    html.Li(children=[
                                        "Paul Finkleman, ", html.I("Slavery and the Founders: Race and Liberty in the Age of Jefferson"), " (1996), p. 14; Jesse Wegman, ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 66-67"
                                    ]),   
                                    html.Li(children=[
                                        "Eric Foner, ", html.I("The Second Founding: How the Civil War and Reconstruction Remade the Constitution"), " (2019), p. 85; \
                                        Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 109-110",
                                    ]),  
                                    html.Li(children=[
                                        "E. W. Hutter, ", dcc.Link("“The Nation's Great Triumph”", href="https://newspaperarchive.com/politics-clipping-apr-10-1865-2081429/",
                                        target="_blank"), ", ", html.I("Philadelphia Press"), " (April 10, 1865), p. 4",
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 106-107",
                                    ]),  
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), ", dcc.Link("“The Racist History Of The Senate Filibuster”",
                                        href="https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster", target="_blank"), " (Jan. 12 2021) [Audio \
                                        podcast episode], ", html.I("NPR"), " “Fresh Air”, [16:45 - 17:50]"
                                    ]),
                                    html.Li(children=[
                                        "Frederick Douglass, ", html.I("Life and Times of Frederick Douglass"), " (1892), p. 280-282",
                                    ]),
                                    html.Li(children=[
                                        "C. Vann Woodward, “The Anachronistic Electoral System”, ", html.I("New Republic"), " (June 1, 1968), p. 44-45, cited by Jesse Wegman in ", 
                                        html.I("Let the People Pick the President"), " (2020), p. 118",
                                    ]),
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), ", dcc.Link("“The Racist History Of The Senate Filibuster”",
                                        href="https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster", target="_blank"), " (Jan. 12 2021) [Audio \
                                        podcast episode], ", html.I("NPR"), " “Fresh Air”, [21:15 - 23:30]"
                                    ]),
                                    html.Li(children=[
                                        "Terry Gross (Host), Adam Jentleson (Guest), ", dcc.Link("“The Racist History Of The Senate Filibuster”",
                                        href="https://www.npr.org/2021/01/12/956018064/the-racist-history-of-the-senate-filibuster", target="_blank"), " (Jan. 12 2021) [Audio \
                                        podcast episode], ", html.I("NPR"), " “Fresh Air”, [23:30 - 25:00]"
                                    ]),
                                    html.Li(children=[
                                        "Richard Rothstein, ", html.I("The Color of Law"), " (2017), p. 63-67",
                                    ]),
                                    html.Li(children=[
                                        "Richard Rothstein, ", html.I("The Color of Law"), " (2017), p. 54-56, p. 128-131",
                                    ]),
                                    html.Li(children=[
                                        "Eric Foner, ", html.I("The Second Founding: How the Civil War and Reconstruction Remade the Constitution"), " (2019), p. 158, 164; ",
                                        "Jamelle Bouie, ", dcc.Link("“One Old Way of Keeping Black People From Voting Still Works”", target="_blank", 
                                        href="https://www.nytimes.com/2021/03/05/opinion/filibuster-voting-rights.html"), ", ", html.I("New York Times"), 
                                        " (Mar. 5 2021)",
                                    ]),
                                    html.Li(children=[
                                        "Juan F. Perea, ", dcc.Link("“The Echoes of Slavery: Recognizing the Racist Origins of the Agricultural and Domestic Worker Exclusion from \
                                        the National Labor Relations Act”", href="https://lawecommons.luc.edu/cgi/viewcontent.cgi?article=1150&context=facpubs", target="_blank"), 
                                        ", ", html.I("Ohio State Law Journal"), ", Vol. 72:1 (2011), p. 104-109",
                                    ]),
                                    html.Li(children=[
                                        "Rachel E. Greenspan, ", dcc.Link("“'It's the Legacy of Slavery': Here's the Troubling History Behind Tipping Practices in the U.S.”", 
                                        href="https://time.com/5404475/history-tipping-american-restaurants-civil-war/", target="_blank"), ", ", html.I("Time"), 
                                        " (Oct. 15 2018), p. 104-109", 
                                    ]),
                                    html.Li(children=[
                                        "Ramtin Arablouei and Rund Abdelfatah (Hosts), ", dcc.Link("“The Land of the Fee”", target="_blank",
                                        href="https://www.npr.org/2021/03/22/980047710/the-land-of-the-fee"), " (March 25, 2021) [Audio podcast episode], ", html.I("NPR"), 
                                        " “Throughline”, [16:20 - 21:00]"
                                    ]),
                                    html.Li(children=[
                                        "Eric Foner, ", html.I("The Second Founding: How the Civil War and Reconstruction Remade the Constitution"), " (2019), p. 110-111",
                                    ]),
                                    html.Li(children=[
                                        "Michelle Alexander, ", html.I("The New Jim Crow: Mass Incarceration in the Age of Colorblindness"), " (2010), p. 35-36, 80, \
                                        86-88, 97"
                                    ]), 
                                    html.Li(children=[
                                        "Gary Potter, ", html.I(dcc.Link("The History of Policing in the United States", target="_blank",
                                        href="https://plsonline.eku.edu/sites/plsonline.eku.edu/files/the-history-of-policing-in-us.pdf")), " (June 25, 2013), p. 5-7",
                                    ]),                                 
                                    html.Li(children=[
                                        "Akhil Reed Amar, ", html.I("The Law of the Land: A Grand Tour of our Constitutional Republic"), " (2015), p. 109"
                                    ]),
                                    html.Li(children=[
                                        "Alvin Chang, ", dcc.Link("“The data proves that school segregation is getting worse”", target="_blank",
                                        href="https://www.vox.com/2018/3/5/17080218/school-segregation-getting-worse-data"), ", ", html.I("Vox"), " (March 5, 2018)", 
                                    ]),
                                    html.Li(children=[
                                        "Ibram X. Kendi, ", html.I("Stamped From the Beginning"), " (2016), p. 311-312"
                                    ]),
                                    html.Li(children=[
                                        "Jesse Wegman, ", html.I("Let the People Pick the President"), " (2020), p. 123",
                                    ]),
                                    html.Li(children=[
                                        "Michael Perman, ", html.I(dcc.Link("Struggle for Mastery: Disfranchisement in the South, 1888–1908", target="_blank",
                                        href="https://uncpress.org/book/9780807849095/struggle-for-mastery/")), " (2001), Introduction",
                                    ]),
                                ]),
                                html.B("Images:"),
                                html.Br(),
                                dcc.Link("Intro: American voter enfranchisement: A zero-sum game", href="/voter-weight-electoral-college-bias-intro"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "Alfred R. Waud, “The First Vote”, ", html.I("Harper’s Weekly"), " (Nov. 16 1867), ", dcc.Link("Library of Congress", 
                                        href="https://www.loc.gov/resource/cph.3a52371/", target="_blank"),
                                    ]),
                                ]),
                                dcc.Link("Part 1: Electoral College bias: Equality for states, not for voters", href="/voter-weight-electoral-college-bias-page1"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "1790 Census of the United States (Oct. 24, 1791), ", dcc.Link("familytree.com", target="_blank",
                                        href="https://www.familytree.com/blog/two-hundred-and-twenty-eight-years/"),
                                    ]),
                                    html.Li(children=[
                                        "Thomas Nast, “A National Game That Is Played Out”, ", html.I([dcc.Link("Harper’s Weekly", 
                                        href="https://elections.harpweek.com/1876/cartoon-1876-Medium.asp?UniqueID=29&Year=1876", target="_blank")]), " (Dec. 23, 1876)"
                                    ]),
                                ]),
                                dcc.Link("Part 2: Small-state bias and slave-state bias: As the framers intended", href="/voter-weight-electoral-college-bias-page2"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "List of votes for President and Vice President of the United States, ", html.I("Records of the U.S. Senate, Record Group 46"),
                                        " (Feb. 8, 1837), ", dcc.Link("docsteach.org", target="_blank",
                                        href="https://www.docsteach.org/documents/document/list-of-votes-for-president-and-vice-president-of-the-united-states"),
                                    ]),
                                ]),
                                dcc.Link("Part 3: Reconstruction and Black voting rights", href="/voter-weight-electoral-college-bias-page3"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "Thomas Nast, “Shall We Call Home Our Troops?”, ", html.I("Harper’s Weekly"), " (Jan. 9, 1875), ", dcc.Link("Library of Congress",
                                        href="https://www.loc.gov/resource/cph.3a03175/", target="_blank"),
                                    ]),
                                    html.Li(children=[
                                        "Photo montage: Frederick Douglass, William Lloyd Garrison, Wendell Phillips, ", dcc.Link("americanabolitionists.com",
                                        href="http://www.americanabolitionists.com/abolitionists-and-anti-slavery-activists.html", target="_blank"),
                                    ]),
                                    html.Li(children=[
                                        "“Freedmen’s Bureau”, ", html.I("Harper’s Weekly"), " (1868), ", dcc.Link("encyclopediaofalabama.org", target="_blank", 
                                        href="http://encyclopediaofalabama.org/article/m-6202"),
                                    ]),
                                    html.Li(children=[
                                        "W. L. Sheppard, “Electioneering at the South”, ", html.I([dcc.Link("Harper’s Weekly", target="_blank",
                                        href="https://blackhistory.harpweek.com/7Illustrations/Reconstruction/ElectioneeringAtTheSouth.htm")]), " (July 25, 1868)"
                                    ]),
                                    html.Li(children=[
                                        "Thomas Nast, “The Georgetown Election - The Negro at the Ballot-Box”, ", html.I("Harper’s Weekly"), " (Mar. 16, 1867), ",
                                        dcc.Link("Getty Images", target="_blank", 
                                        href="https://www.gettyimages.com/detail/news-photo/march-1867-harpers-weekly-political-cartoon-by-american-news-photo/51240022"),
                                    ]),
                                ]),
                                dcc.Link("Part 4: Suppression-state bias", href="/voter-weight-electoral-college-bias-page4"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "Thomas Nast, “The Union As It Was”, ", html.I([dcc.Link("Harper’s Weekly", target="_blank",
                                        href="https://blackhistory.harpweek.com/7Illustrations/Reconstruction/UnionAsItWas.htm")]), " (Oct. 24, 1874)"
                                    ]),
                                ]),
                                dcc.Link("Part 5: Results and observations", href="/voter-weight-results"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "A. B. Frost, “Of Course He Wants To Vote The Democratic Ticket”, ", html.I("Harper’s Weekly"), " (Oct. 1876), ",
                                        dcc.Link("Wikimedia", target="_blank", 
                                        href="https://commons.wikimedia.org/wiki/File:%27Of_Course_He_Wants_To_Vote_The_Democratic_Ticket%27_(October_1876),_Harper%27s_Weekly.jpg"),
                                    ]),
                                    html.Li(children=[
                                        "Russell Lee, “A poll tax sign in Mineola, Texas” (Jan. 1939), ", dcc.Link("Library of Congress", target="_blank",
                                        href="https://www.loc.gov/item/2017738854/"),
                                    ]),
                                    html.Li(children=[
                                        "1860 Census of the United States, ", dcc.Link("census.gov", target="_blank",
                                        href="https://www.census.gov/history/pdf/ApportionmentInformation-1860Census.pdf"),
                                    ]),
                                    html.Li(children=[
                                        "“Supreme Court Invalidates Key Part of Voting Rights Act”, ", html.I([dcc.Link("New York Times", target="_blank",
                                        href="https://www.nytimes.com/2013/06/26/us/supreme-court-ruling.html")]), " (June 25, 2013)"
                                    ]),
                                ]),
                                dcc.Link("Part 6: Conclusions and interpretation", href="/voter-weight-conclusions"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "E. W. Kemble, “Congress - 14th Amendment 2nd section” (1902), ", dcc.Link("Library of Congress", target="_blank", 
                                        href="https://www.loc.gov/resource/ppmsca.07161/"), 
                                    ]),
                                    html.Li(children=[
                                        "Newspaper clipping: “High Court Rules Scott Still a Slave” (Mar. 7, 1857), ", dcc.Link("Ferris State University", target="_blank", 
                                        href="https://www.ferris.edu/htmls/news/jimcrow/timeline/slavery.htm"), 
                                    ]),
                                    html.Li(children=[
                                        "Newspaper clipping: “Read and Ponder the Fugitive Slave Law” (1850), ", dcc.Link("Getty Images", target="_blank", 
                                        href="https://www.gettyimages.com/detail/news-photo/an-anti-whig-editorial-regarding-the-fugitive-slave-law-of-news-photo/640486403"),
                                    ]),
                                    html.Li(children=[
                                        "J. L. Magee, “Forcing slavery down the throat of a freesoiler” (1856), ", dcc.Link("Library of Congress", target="_blank", 
                                        href="https://www.loc.gov/resource/lprbscsm.scsm0326/"), 
                                    ]),
                                    html.Li(children=[
                                        "Pamphlet: “A voice from the South: comprising letters from Georgia to Massachusetts, and to the southern states”, ",
                                        html.I("Baltimore, Western Continent Press"), " (1847), ", dcc.Link("Library of Congress", target="_blank", 
                                        href="https://www.loc.gov/resource/rbaapc.16300/?sp=1"), 
                                    ]),
                                    html.Li(children=[
                                        "Chip Somodevilla, “The Russell Senate Office Building on Capitol Hill”, ", html.I([dcc.Link("The Atlanta Journal-Constitution",
                                        href="https://www.loc.gov/resource/lprbscsm.scsm0326/", target="_blank")]), " (Aug. 27 , 2018)"
                                    ]),
                                    html.Li(children=[
                                        "“The 1938 Home Owners’ Loan Corporation map of Brooklyn”, ", dcc.Link("Red Line Archives", target="_blank", 
                                        href="https://www.redlinearchive.net/portfolio/red-line-maps/"), 
                                    ]),
                                    html.Li(children=[
                                        "“Luxurious Early American Railway Pullman Dining Car” (1877), ", dcc.Link("Getty Images", target="_blank", 
                                        href="https://www.gettyimages.com/detail/illustration/luxurious-early-american-railway-pullman-royalty-free-illustration/977712268"), 
                                    ]),
                                    html.Li(children=[
                                        "Johnny Jenkins or Will Counts, “Little Rock Crisis” (Sep. 23, 1957), ", dcc.Link("Getty Images", target="_blank",
                                        href="https://www.gettyimages.com/detail/news-photo/elizabeth-eckford-ignores-the-hostile-screams-and-stares-of-news-photo/517322800"), 
                                    ]),
                                    html.Li(children=[
                                        "Original Film Art: “Gone with the Wind” (1939)",
                                    ]),
                                    html.Li(children=[
                                        "“A group of Klan members lead their children through a parade.” (Circa 1912-1930), ", dcc.Link("allthatsinteresting.com",
                                        href="https://allthatsinteresting.com/ku-klux-klan-youth#5", target="_blank"), 
                                    ]),
                                    html.Li(children=[
                                        "Saul Loeb, “A supporter of US President Donald Trump carries a Confederate flag as he protests in the US Capitol Rotunda on \
                                        January 6, 2021, in Washington, DC.” (Jan. 6, 2021), ", dcc.Link("Getty Images", target="_blank",
                                        href="https://www.gettyimages.com/detail/news-photo/supporter-of-us-president-donald-trump-carries-a-news-photo/1230455296"), 
                                    ]),
                                ]),
                                dcc.Link("Appendix 2: Annotated Timeline Charting Voter Weight Trends: 1800 - 2020", href="/voter-weight-timeline-visualization"),
                                html.Ul(children=[
                                    html.Li(children=[
                                        "Portrait of President Andrew Jackson (1832), ", dcc.Link("University of Tennessee Knoxville", target="_blank", 
                                        href="https://history.utk.edu/uts-andrew-jackson-project-now-available-online/"), 
                                    ]),
                                ]),
                            ]),
                        ])
                    ])
                ]),
                dbc.Col(md=2),
            ])
        ])
    ])
])