import streamlit as st
from pages import Pages

list_of_pages = [
    "The Project",
    "Big News for Zack!",
    "Look back, Zack!",
    "Zack's Musical Numbers",
    "The Pitch",
    "Recommender Engines",
    "Playlists",
    "Conclusions and Recommendations",
    "References"

]

st.sidebar.title('Breaking into the US! :notes:')
st.sidebar.markdown('by Group Mic :microphone: | DSFC10')
st.sidebar.image("sidebarpic.jpg")
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "The Project":
    Pages.introduction()

elif selection == "Big News for Zack!":
    Pages.news()

elif selection == "Look back, Zack!":
    Pages.background()

elif selection == "Zack's Musical Numbers":
    Pages.statistics()

elif selection == "The Pitch":
    Pages.pitch()

elif selection == "Recommender Engines":
    Pages.rec_engines()

elif selection == "Playlists":
    Pages.playlists()

elif selection == "Conclusions and Recommendations":
    Pages.conc_recomm()

elif selection == "References":
    Pages.references()