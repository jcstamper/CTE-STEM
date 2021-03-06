import numpy as np
from PIL import Image
import streamlit as st
from Helper import load_data, summary_poster

stats_df = load_data("./data/Occupations.csv")

st.set_page_config(page_title="CTE STEM Index", 
                   layout='wide')

#--------------------------------- ---------------------------------  ---------------------------------
#--------------------------------- SETTING UP THE APP
#--------------------------------- ---------------------------------  ---------------------------------
title_image = Image.open("./plots/AppTitle.png")
st.image(title_image)

st.markdown("DEMO for the CTE STEM Index")
st.markdown("This app is meant as a demo explore the dataset created by the CTE STEM Index team.")
#---------------------------------------------------------------#
# SELECT ARTIST AND SETUP DATA
#---------------------------------------------------------------#
sorted_artists = stats_df.groupby('occupation')['workValues.code'].count()\
    .sort_values(ascending=False).index

st.markdown("### **Select Job Title:**")
select_artist = []

select_artist.append(st.selectbox('', sorted_artists))

#Filter df based on selection
artist_df = stats_df[stats_df['occupation'].isin(select_artist)]

major_cluster = artist_df.groupby('Science')['workValues.code'].count()\
    .sort_values(ascending = True).index[0]

col1, col2 = st.beta_columns(2)
    
#with col1:
#    st.markdown(f"**Total Songs:** {artist_df.shape[0]}")
#    st.markdown(f"**Top Song:** " +\
#                f"{artist_df.loc[artist_df['track_rank']==np.min(artist_df['track_rank']),'search_query'].values[0]}")
    
#with col2:
#    st.markdown(f"**Highest Rank:** {np.min(artist_df['track_rank'])}")
#    st.markdown(f"**Major Cluster:** {major_cluster}")

st.text("")
#---------------------------------------------------------------#
# CREATE SUMMARY POSTER
#---------------------------------------------------------------#
fig = summary_poster(artist_df)
st.write(fig)

#---------------------------------------------------------------#
# PROJECT BRIEF
#---------------------------------------------------------------#
#workflow_image = Image.open("./plots/Workflow.jpg")
#
#st.text("")
#st.markdown("### Project Brief  ([Medium Article](https://tanulmathur.medium.com/music-through-the-ages-b7acbfa9eb7c))")
#st.image(workflow_image)

#with st.beta_expander("Spotify Audio Feature definitions"):
#    
#    col1, col2, col3 = st.beta_columns(3)
#    
#    with col1:
#        st.subheader("Acousticness")
#        st.markdown("A confidence measure from 0.0 to 1.0 of whether the "+
#                    "track is acoustic. 1.0 represents high confidence the track is acoustic.")
#        
#        st.subheader("Liveness")
#        st.markdown("Detects the presence of an audience in the recording. Higher liveness values "+
#                    "represent an increased probability that the track was performed live. A value above 0.8 "+
#                    "provides strong likelihood that the track is live.")
#        
#        st.subheader("Speechiness ")        
#        st.markdown("Detects the presence of spoken words in a track. The more exclusively speech-like the "+
#            "recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values "+
#            "above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and"+
#            "0.66 describe tracks that may contain both music and speech, either in sections or layered, including such"+
#            "cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks") 
#        
#    with col2:
#        st.subheader("Danceability")
#        st.markdown("Describes how suitable a track is for dancing based on a "+
#                    "combination of musical elements including tempo, rhythm stability, beat strength, "+
#                    "and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.")
#        
#        st.subheader("Instrumentalness")
#        st.markdown("Predicts whether a track contains no vocals. "+
#            "???Ooh??? and ???aah??? sounds are treated as instrumental in this context. "+
#            "Rap or spoken word tracks are clearly ???vocal???. The closer the instrumentalness "+
#            "value is to 1.0, the greater likelihood the track contains no vocal content. Values "+
#            "above 0.5 are intended to represent instrumental tracks, but confidence is higher as the "+
#            "value approaches 1.0")
        
  
