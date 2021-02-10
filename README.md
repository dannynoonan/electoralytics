# Using electoralytics

This repo currently combines three functions:
* source data transformer & csv file-builder
* plotly figure generator 
* dash website

If the project grows or diversifies it will make sense to separate these pieces, but for now they inhabit the same repo.

*There is no installer* but you should be able to run the site locally, run figure-building modules from command line, and execute the file-builder script locally.

## Figure builders

The core of the project are the plotly express figure builders, which all live in `/fig_builder`. Each module contains functions that wrap a specific type of plotly express figure call, e.g. `px.bar` for a bar plot or `px.choropleth` for a map. In theory you should be able to import and run the functions in these modules independent of their `dash` context, though personally I haven't done so. 

## Dash site

Running the site locally should be achievable in two steps:
* run `pip install -r requirements.txt` from the project root once you've checked it out locally
* run `python run.py` from the project root once dependencies are installed

Execution of `run.py` should generate a small amount of command-line output, mostly confirming that resources from `/data/gen` have been loaded into pandas dataframes. Following this, the site should be reachable at `http://localhost:8050/`.

## Data files and file-builder script

The electoralytics repo runs off two types of data files: source files and generated files. Source files live in the project's base `/data` directory. Generated files live in the `/data/gen` subdirectory. 

Plotly figures are built off of the generated files in the `/data/gen` subdirectory. Having these figure-backing csv files pre-built minimizes the runtime pandas dataframe transformations necessary to build figures tailored to specific scenarios. In essence, the source files are the database, while the generated files are indexed views of that data optimized for delivery. 

Generated files are kept up-to-date in the repo, you should never need to generate them on your end. But if the transformation process from source data files to generated data files interests you, the transformation process lives in `multi_ring_filebuilder.py` and you may explore its usage by running `./multi_ring_filebuilder.py --help` from the project root. The `multi_ring_filebuilder.py` processes use the source csv files (listed next) to write csv files to `/data/gen` (listed after). Note that the source files themselves are not modified or overwritten by `multi_ring_filebuilder.py`.

Source csv files, containing all historical presidential election data used to generate figure-backing csv files: 
* `theOneRing.csv` - state-level turnout, electoral college vote, swing margin, and some derived data for every presidential election since 1800
* `totalsByYear.csv` - national aggregate summary data for every presidential election since 1788

Generated "figure-backing" csv files, containing views of historical presidential election data optimized to build plotly figures: 
* `stateVoteWeightsPivot.csv` - state-level turnout, ec vote, swing margin, and derived weight data, pivoted on election year
* `groupAggWeightsPivot.csv` - national- and group-level aggregate turnout, ec vote, and derived weight data, pivoted on election year

Multiple variations of these two generated files live in subdirectories organized by two criteria:
* state grouping heuristic:
 * `/acw`: American Civil War
 * `/census`: Regional Census
* small-state threshold:
 * `/noSmall`: no small state group
 * `/small3`: small states are those with 3 electoral college votes
 * `/small4`: small states are those with 4 or fewer electoral college votes
 * `/small5`: small states are those with 5 or fewer electoral college votes

## Site content

Presently there's no separation between site text content and core pandas, plotly express, and dash functionality, other than the fact that most of the text content lives in the `/dash_pages` directory.
