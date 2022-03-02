from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data
import pandas as pd

# Read in global data
traits_raw_df = pd.read_csv("../data/breed_traits.csv")
breed_rank_raw_df = pd.read_csv("../data/breed_rank.csv")

# The following static input should be replaced by the input from the dashboard's checkboxes and 
# slidebars.

traits_list = ['Affectionate With Family',
               'Good With Young Children',
               'Good With Other Dogs',
               'Shedding Level']

traits_weights = [5, 3, -3, -1]

# The following is the helper function for creating the top 5 plot and also prepare the 
# dataframe for other parts of the dashboard.

def top_5_plot_func(traits_raw_df, traits_list, traits_weights, breed_rank_raw_df):
    """
    Returns an altair object of a bar chart of top 5 dog breeds.
    
    Parameters:
        traits_raw_df (pandas.DataFrame): a dataframe of breed traits
        traits_list (list): the list of traits that the users have specified
        traits_weights (list): the list of weights of the traits
        
    Returns:
        top_5_plot (altair): altair chart object of the top 5 bar charts
        top_5_df (pandas.DataFrame): the dataframe with the top 5 breeds, the traits, the total 
            scores and the links to the images.
    """
    traits_raw_df["BreedID"] = traits_raw_df.index
    breed_rank_raw_df["BreedID"] = breed_rank_raw_df.index

    print(f"traits_list={traits_list}") #for debug
    traits_df = traits_raw_df.set_index('BreedID')[traits_list]
    
    traits_df['score'] = 0

    for i in range(len(traits_list)):
        traits_df['score'] += traits_df[traits_list[i]] * traits_weights[i]
        
    top_5_df = traits_df.sort_values('score', ascending=False).head(5).merge(
        breed_rank_raw_df, how='left', 
        on='BreedID'
    )
        
    top_5_plot = alt.Chart(top_5_df).mark_bar().encode(
        x=alt.X('score:Q'),
        y=alt.Y('Breed:N', sort='-x')
    )

    return top_5_plot, top_5_df

#top_5_plot, top_5_df = top_5_plot_func(traits_raw_df, traits_list, traits_weights, 
#                                       breed_rank_raw_df)

#top_5_plot
#print(top_5_df)

# The following code comes from Florencia's sample
cars = data.cars()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='Horsepower',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart, top_5_df = top_5_plot_func(traits_raw_df, traits_list, traits_weights, 
                                      breed_rank_raw_df)
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)