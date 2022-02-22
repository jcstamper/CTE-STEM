import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def load_data(filename):
    df = pd.read_csv(filename, index_col=0)
    return df

def summary_poster(artist_df, color_dict):
    #MAKE SUBPLOTS
    fig = make_subplots(
        rows=2, cols=2, 
        column_widths=[0.4, 0.6],
        specs=[[{"type": "pie"}, {"type": "bar"}],
            subplot_titles=('S, T, E, M Clusters', 
                            'Change Year to Year'),
            vertical_spacing=0.1, horizontal_spacing= 0.09)
    #PIE
    #data for pie
    pie_data = artist_df.groupby('clusters')['search_query'].count()

    fig.add_trace(go.Pie(labels = pie_data.index,
                            values = pie_data.values,
                            hole = 0.4,
                            legendgroup = 'grp1',
                            showlegend=False),
                row = 1, col = 1)
    fig.update_traces(hoverinfo = 'label+percent',
                        textinfo = 'value+percent',
                        textfont_color = 'white',
                        marker = dict(colors = pie_data.index.map(color_dict),
                                    line=dict(color='white', width=1)),
                        row = 1, col = 1)

    #STACKED BAR
    pivot_artist_df = artist_df.groupby(['year','clusters'])['search_query'].count()
    pivot_artist_df = pivot_artist_df.unstack()
    pivot_artist_df.fillna(0, inplace = True)

    #plot params
    labels = pivot_artist_df.columns    

    for i, label_name in enumerate(labels):
        x = pivot_artist_df.iloc[:,i].index
        fig.add_trace(go.Bar(x = x, 
                                y = pivot_artist_df.iloc[:,i],
                                name = label_name,
                                hovertemplate='<b>Year: %{x}</b><br>#Songs: %{y}',
                                marker_color = pd.Series([label_name]*len(x)).map(color_dict),
                                legendgroup = 'grp2',
                                showlegend=True),
                                row = 1, col = 2)
    fig.update_yaxes(title_text = '#Songs',linecolor = 'grey', mirror = True, 
                        title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                        zeroline = False,
                        row = 1, col = 2)
    fig.update_xaxes(linecolor = 'grey', mirror = True, dtick = 5,
                     row = 1, col = 2)

   
    
    return fig