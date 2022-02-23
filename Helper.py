import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def load_data(filename):
    df = pd.read_csv(filename, index_col=0)
    return df

def summary_poster(occupation_df, color_dict):
    #MAKE SUBPLOTS
    fig = make_subplots(
        rows=2, cols=2, 
        column_widths=[0.4, 0.6],
        specs=[[{"type": "pie"}, {"type": "bar"}],
            [ {"type":"scatter", "colspan": 2}, None]],
            subplot_titles=('S, T, E, M Clusters', 
                            'S, T, E, M Bar Graph', 
                            'Test Graph'),
            vertical_spacing=0.1, horizontal_spacing= 0.09)
    #PIE
    #data for pie
    colors = ['royalblue', 'darkorange', 'grey', 'gold']
    stem = []
    stem.append(occupation_df['Science'].values[0]) 
    stem.append(occupation_df['Technology'].values[0]) 
    stem.append(occupation_df['Engineering'].values[0]) 
    stem.append(occupation_df['Mathematics'].values[0]) 
    pie_data = pd.DataFrame(columns=['clusters'])
    #pie_data.loc['Science'] = [job_df['science']]
    #pie_data.loc['Technology'] = [job_df['technolgy']]
    #fig.add_trace(go.Pie(labels = pie_data.index,
    #                        values = pie_data.values,
    fig.add_trace(go.Pie(labels = ['Science', 'Technology', 'Engineering', 'Mathematics'],
                            values = stem,
                            hole = 0.7,
                            legendgroup = 'grp1',
                            showlegend=False),
                            row = 1, col = 1)
    fig.update_traces(hoverinfo = 'label+percent',
                        textinfo = 'label+value',
                        textfont_color = 'white',
                        marker = dict(colors = colors,
                                    line=dict(color='white', width=1)),
                        row = 1, col = 1)

    #STACKED BAR
    pivot_occupation_df = occupation_df.groupby(['title','education.code'])['Science'].count()
    pivot_occupation_df = pivot_occupation_df.unstack()
    pivot_occupation_df.fillna(0, inplace = True)

    #plot params
    labels = pivot_occupation_df.columns    

    
    clusters = ['Science', 'Technology', 'Engineering', 'Mathematics']
    values = stem
    
    #colors = [[#F63366], [#2BB1BB], [#22466B], '' ]
    fig.add_trace(go.Bar(x = clusters, 
                         y = values,
                         marker=dict(color = colors),
                         hoverinfo = 'x+y'),
                         row = 1, col = 2)
    fig.update_yaxes(title_text = 'Level',linecolor = 'grey', mirror = True, 
                        title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                        zeroline = False,
                        row = 1, col = 2)
    fig.update_xaxes(linecolor = 'grey', mirror = True, dtick = 5,
                     row = 1, col = 2)

    #SCATTER
    fig.add_trace(go.Scatter(
                x=occupation_df['title'],
                y=occupation_df['education.code'],
                mode = 'markers',
                #marker_color = occupation_df['clusters'].map(color_dict),
                customdata = occupation_df.loc[:,['title','education.code','occupation']],
                hovertemplate='<b>Year: %{customdata[0]}</b><br>Rank: %{customdata[1]} <br>Title: %{customdata[2]}',
                legendgroup = 'grp1',
                showlegend=False
                ),
                row = 2, col = 1
                )
    fig.update_traces(marker = dict(symbol = 'triangle-right', size = 12
                                    #,line = dict(color = 'grey', width = 0.5)
                                    ),
                      name = "",
                      row = 2, col =1)
    fig.update_yaxes(autorange = 'reversed',title = 'Rank',showgrid=True, 
                    mirror = True, zeroline = False, linecolor = 'grey',
                    title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                    row = 2, col = 1)
    fig.update_xaxes(title="",showgrid=True, mirror = True,
                    linecolor = 'grey', range = [1969,2021],
                    gridcolor = 'grey', gridwidth = 0.1
                    , row = 2, col =1)

    fig.update_layout( # customize font and margins
                        barmode = 'stack',
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        #plot_bgcolor = '#0E1117',#'black',
                        font_family= 'Nunito',#"Helvetica",
                        width=1200,
                        height=800,
                        template = 'plotly_dark',
                        legend=dict(title="", orientation = 'v',
                                    font=dict(size = 10),
                                    bordercolor = 'LightGrey',
                                    borderwidth=0.5),
                        margin = dict(l = 40, t = 40, r = 40, b = 40)
                    )
    
    return fig