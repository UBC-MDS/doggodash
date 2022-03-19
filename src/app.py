# libraries
from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc

# Read in data
traits_raw_df = pd.read_csv("data/breed_traits.csv")
breed_rank_raw_df = pd.read_csv("data/breed_rank.csv")

# For traits list in checklist input
traits_list_full = traits_raw_df.drop(columns=['Breed' ,'Coat Type', 'Coat Length']).columns

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = dbc.Container(
    [
        # Header for app
        html.H1(
            'Doggodash', 
             style = { 
                'color': 'white', 
                'fontSize': 40,
                'background-color': 'Indigo',
                'textAlign': 'center'
                }
        ),
            

        # Drop down for list of columns
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                                'Choose Dog traits you like and dislike',
                                style = { 
                                    'color': 'Indigo', 
                                    'fontSize': 18,
                                    'textAlign': 'center',
                                    'background-color': 'lavender',
                                    'width': '100%',
                                },
                        ),

                        dcc.Dropdown(
                            id='traits-widget',
                            value= traits_list_full[1:5],      # Default list
                            options=[{'label': col, 'value': col} for col in traits_list_full],
                            placeholder='Select Doggo traits',
                            multi=True,
                            style={
                                'height': '80%',
                                'width': '100%',
                                'fontSize': 18,
                                'background-color': 'white',
                            },
                        ),
                    ], 
                    md=3
                ),

                dbc.Col(
                    [
                        html.P(
                            'Select weights',
                            style = { 
                                'color': 'Indigo', 
                                'fontSize': 18,
                                'textAlign': 'center',
                                'align': 'top',
                                'background-color': 'lavender',
                                'width': '100%'
                            },
                        ),
                        
                        html.P(
                               'Weight for traits you like',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 14,
                                        'textAlign': 'center',
                               },
                        ),
                        
                        dcc.Slider(
                            id='xslider_like',
                            min=0,
                            max=2.5,
                            step=0.5,
                            value=1 
                         ),
                        
                        html.P(
                               'Weight for traits you dislike',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 14,
                                        'textAlign': 'center',
                               },
                        ),
                        dcc.Slider(
                           id='xslider_dislike',
                            min=-2.5,
                            max=0,
                            step=0.5,
                            value=-0.5
                         ),
                        
                        html.Br(),
                        
                        html.P(
                               'Higher weights increase scoring on likeable traits and decrease scoring on dislikeable traits (drooling and shedding levels)',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 14,
                                        'textAlign': 'center',
                               },
                        ),
                        
                    ], 
                    md=3,
                    align='top'
                ),
                        
                dbc.Col(
                    [
                        html.P(
                               'Top 5 recommended Dog breeds as per chosen traits. Click to view them!',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                                        'width': '100%'
                               },
                        ),

                        html.Iframe(
                                id='top5dogs_plot',
                                style={
                                    'display': 'block',
                                    'border-width': '1', 
                                    'height': '300px',
                                    'width': '100%',
                                    
                                },
                        ),
                        
                        
                        html.P(
                               'Hover over to see 2020 rank and click to see image. To go back, click on browser back button',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 14,
                                        'textAlign': 'center',
                               },
                        ),
                    ], 
                    md=6,
                ),
            ],
        ),
                
        html.Hr(
            style={
                'height': '2px',
                'border-width': '0',
                'color': 'Indigo'
            },
        ),
                
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                               'Details of the recommended dog breeds',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                               },
                        ),
                        
                        html.Iframe(
                            id='top5dogs_details',
                            style={
                                'display': 'block',
                                'border-width': '0', 
                                'width': '100%', 
                                'height': '75%',
                                'background-color': 'lavender',
                                'align': 'center'
                            },
                        ),
                    ],
                    md=6,
                    align='left'
                ),

                dbc.Col(
                    [
                        html.P(
                               'Yearly ranking trend of top 5 dog breeds',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                               },
                        ),
                        html.Iframe(
                            id='top5dogs_ranking_trend',
                            style={
                                'display': 'block',
                                'border-width': '0', 
                                'width': '100%', 
                                'height': '300px',
                                'background-color': 'lavender'
                            },
                        ),
                        
                        html.P(
                               'Zoom in to see top rank trends over the years',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 14,
                                        'textAlign': 'center',
                               },
                        ),
                    ],
                    md=6,
                    align='right'
                ),

            ],

        ),
        
        # New feature - surprise me
        html.Hr(
            style={
                'height': '2px',
                'border-width': '0',
                'color': 'Indigo'
            },
        ),
                
        dbc.Row(
            [
                dbc.Row(
                    [
                       html.P(
                               'Want to be amused about a randomly selected dog? Click on surpise me, have fun learning (forget the analytics, this could be your new interest!)',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                               },
                        ),
                        
                        dbc.Button(
                            "Surprise me", 
                            id="surpise-me-button", 
                            className="me-2", 
                            n_clicks=1
                        )
                    ]
                ),
                
                html.Br(),
                
                html.Br(),
                
                dbc.Col(
                    [
                        html.P(
                               'Details of the surpise me dog breed',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                               },
                        ),
                        
                        html.Iframe(
                            id='surpise_me_dog_details',
                            style={
                                'display': 'block',
                                'border-width': '0', 
                                'width': '100%', 
                                'height': '350px',
                                'background-color': 'lavender',
                                'align': 'center'
                            },
                        ),
                    ],
                    md=6,
                    align='left'
                ),

                dbc.Col(
                    [
                        html.P(
                               'Yearly ranking trend of top 5 dog breeds',
                               style = { 
                                        'color': 'Indigo', 
                                        'fontSize': 18,
                                        'textAlign': 'center',
                                        'background-color': 'lavender',
                               },
                        ),
                        html.Iframe(
                            id='surpise_me_dog_ranking_trend',
                            style={
                                'display': 'block',
                                'border-width': '0', 
                                'width': '100%', 
                                'height': '300px',
                                'background-color': 'lavender'
                            },
                        ),
                        
                        
                    ],
                    md=6
                ),

            ],

        ),
    ],
    style={
        'background-color': 'Beige'
    },
    fluid=True
)
           
            
# Set up callbacks/backend

# Plot1
@app.callback(
    Output('top5dogs_plot', 'srcDoc'),
    Output('top5dogs_details', 'srcDoc'),
    Output('top5dogs_ranking_trend', 'srcDoc'),
    Input('traits-widget', 'value'),
    Input('xslider_like', 'value'),
    Input('xslider_dislike', 'value')
)

def plot_altair(traits_list, positive_weight, negative_weight):
    """
    Returns an altair object of a bar chart of top 5 dog breeds.
    
    Parameters
    ----------
    traits_raw_df (pandas.DataFrame): a dataframe of breed traits
    traits_list (list): the list of traits that the users have specified
    traits_weights (list): the list of weights of the traits
        
    Returns
    -------
    top_5_plot (altair to html object): altair chart object of the top 5 dog breeds in html
    top_5_df (pandas.DataFrame to html object): the dataframe with the top 5 breeds, the traits, 
            the total scores and the links to the images.
    top_5_rank_plot (altair to html object): altair chart object of yearly trend of ranks of top 5 dogs in html
    """
    
    traits_raw_df["BreedID"] = traits_raw_df.index
    breed_rank_raw_df["BreedID"] = breed_rank_raw_df.index

    print(f"traits_list={traits_list}") #for debug
    traits_df = traits_raw_df.set_index('BreedID')[traits_list]
    
    traits_df['score'] = 0
    
    traits_dislikeable = [
        'Shedding Level',
        'Drooling Level'
    ]

    for i in range(len(traits_list)):
        if len(traits_list)==0:
            continue
        elif set(traits_list[i]).intersection(set(traits_dislikeable)):
            traits_df['score'] += traits_df[traits_list[i]] * negative_weight
        else:
            traits_df['score'] += traits_df[traits_list[i]] * positive_weight
        
    top_5_df = traits_df.sort_values('score', ascending=False).head(5).merge(
        breed_rank_raw_df, how='left', 
        on='BreedID'
    ) # Havent tried multiple outputs yet as it wasnt possible in single callback
        
    top_5_plot = alt.Chart(top_5_df, title='Your Top 5 Dog Breeds').mark_bar().encode(
        x=alt.X('score:Q'),
        y=alt.Y('Breed:N', sort='-x'),
        color=alt.Color('Breed', 
                        scale=alt.Scale(scheme='greenblue'),
                        legend=None
                       ),
        href='Image',
        tooltip=['Breed', '2020', 'Image']
    ).properties(
        width=400,
        height=200,
    ).interactive()
    
    # The following code is for plotting the trend of ranking of the top 5 breeds.
    col_list = list()

    for year in range(2013, 2021):
        new_col_name = str(year)
        col_list.append(str(year))
        old_col_name = new_col_name + " " + "Rank"
        top_5_df.rename(columns={old_col_name:new_col_name}, inplace=True)

    top_5_rank_df = top_5_df.melt(id_vars = ['Breed', 'BreedID'], value_vars=col_list, var_name='Rank year', value_name='Rank')    
    

    top_5_rank_plot = (alt.Chart(top_5_rank_df).mark_line().encode(
        y=alt.Y('Rank:Q', scale=alt.Scale(zero=False, reverse=True)),
        x=alt.X('Rank year:Q', axis=alt.Axis(format='.0f')),
        color=alt.Color('Breed', 
                        scale=alt.Scale(scheme='viridis'),
                       ),
        tooltip=['Breed','score:Q']
    ).properties(
        width=400,
        height=200,
    ).interactive()
    )
    traits_list.extend(['Breed','score'])
    return top_5_plot.to_html(),  top_5_df[traits_list].to_html(), top_5_rank_plot.to_html()

@app.callback(
    Output("surpise_me_dog_details", "srcDoc"),
    Output("surpise_me_dog_ranking_trend", "srcDoc"),
    [Input("surpise-me-button", "n_clicks")]
)

def surprise_me(n):
    if n:
        surprise_me_raw_df = breed_rank_raw_df.sample()

    # The following 3 lines is for avoiding picking a breed that does not have past rank data.
    while (surprise_me_raw_df.isnull().any().any()):
        print("something is null.  picking another sample.") #for debug
        surprise_me_raw_df = breed_rank_raw_df.sample()
        
        
    # Merge the 2 dataframes together
    surprise_me_raw_df = surprise_me_raw_df.merge(traits_raw_df.drop('Breed', axis=1), 
                                              how='left', on='BreedID')
    
    # The following few lines of code is for changing the column names to tidy the "Rank year" and "Rank" columns.
    col_list = list()
    for year in range(2013, 2021):
        new_col_name = str(year)
        col_list.append(str(year))
        old_col_name = new_col_name + " " + "Rank"
        surprise_me_raw_df.rename(columns={old_col_name:new_col_name}, inplace=True)
        
    # The dataframe now has the columns Breed, BreedID, Image (URL), Rank year and Rank. Please 
    surprise_me_df = surprise_me_raw_df.melt(
        id_vars = ['Breed', 'BreedID', 'Image'], 
        value_vars=col_list, 
        var_name='Rank year', 
        value_name='Rank'
    )
    
    # This is the ranking trend plot.
    surprise_me_plot = alt.Chart(surprise_me_df).mark_line().encode(
        y=alt.Y('Rank:Q', scale=alt.Scale(zero=False, reverse=True)),
        x=alt.X('Rank year:Q', axis=alt.Axis(format='.0f')),
        tooltip=['Breed', 'Rank:Q']
    ).properties(
        width=400,
        height=200,
        title=f"Surprise! Have you heard of {surprise_me_df.Breed[0]}? Here is its ranking trend."
    ).interactive()
    
    return(surprise_me_df.to_html(), surprise_me_plot.to_html())
        
 
if __name__ == '__main__':
    app.run_server(debug=True)
