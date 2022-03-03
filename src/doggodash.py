# libraries
from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd

# Read in data
traits_raw_df = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-02-01/breed_traits.csv")
breed_rank_raw_df = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-02-01/breed_rank.csv")

# For traits list in checklist input
traits_list_full = traits_raw_df.drop(columns=['Breed' ,'Coat Type', 'Coat Length']).columns

# For scoring
traits_weights = [
    5,3,1,-1,0.2,-5,0.1,0.1,0.1,0.1,0.1
]   


# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
    html.Br(),
    html.Br(),

    # Header for app
    html.H1('Doggodash', 
            style = { 
                'color': 'white', 
                'fontSize': 40,
                'background-color': 'grey',
                'textAlign': 'center'
    }),

    # Drop down for list of columns

    html.Br(),
    html.P(
        'Select your favourite Doggo traits'
    ),

    dcc.Dropdown(
        id='traits-widget',
        value= traits_list_full[1:5],      # Default list

        options=[{'label': col, 'value': col} for col in traits_list_full],
        placeholder='Select Doggo traits',
        multi=True
    ), 
    html.Br(),

    html.Iframe(
        id='top5dogs_plot',
        style={
            'border-width': '0', 
            'width': '100%', 
            'height': '200px'}),

    html.Br(),
    html.P("Data for top dog breeds as per your traits selection"),
    html.Iframe(
        id='top5dogs_df',
        style={
            'border-width': '0', 
            'width': '100%', 
            'height': '400px'})

    ])

# Set up callbacks/backend
@app.callback(
    Output('top5dogs_plot', 'srcDoc'),
    Output('top5dogs_df', 'srcDoc'),
    Input('traits-widget', 'value')
)

def plot_altair(traits_list):
    """
    Returns an altair object of a bar chart of top 5 dog breeds.
    
    Parameters
    ----------
    traits_raw_df (pandas.DataFrame): a dataframe of breed traits
    traits_list (list): the list of traits that the users have specified
    traits_weights (list): the list of weights of the traits
        
    Returns
    -------
    top_5_plot (altair): altair chart object of the top 5 bar charts
    top_5_df (pandas.DataFrame): the dataframe with the top 5 breeds, the traits, 
            the total scores and the links to the images.
    """

    traits_raw_df["BreedID"] = traits_raw_df.index
    breed_rank_raw_df["BreedID"] = breed_rank_raw_df.index

    print(f"traits_list={traits_list}") #for debug
    traits_df = traits_raw_df.set_index('BreedID')[traits_list]

    traits_df['score'] = 0

    for i in range(len(traits_list)):
        if len(traits_list)==0:
            continue
        traits_df['score'] += traits_df[traits_list[i]] * traits_weights[i]

    top_5_df = traits_df.sort_values('score', ascending=False).head(5).merge(
        breed_rank_raw_df, how='left', 
        on='BreedID'
    ) # Havent tried multiple outputs yet as it wasnt possible in single callback

    top_5_plot = alt.Chart(top_5_df, title='Your Top 5 Dog Breeds').mark_bar().encode(
        x=alt.X('score:Q'),
        y=alt.Y('Breed:N', sort='-x')
    )

    return top_5_plot.to_html(), top_5_df.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)
