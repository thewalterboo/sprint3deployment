import streamlit as st

from views import Pages

list_of_pages = [
    "The Project",
    "Big News for Zack!",
    "Zack Tabudlo: Background",
    "Zack Tabudlo: Statistics",
    "The Pitch",
    "Recommender Engines",
    "Playlists",
    "Conclusions and Recommendations",
    "References"

]

st.sidebar.title(':scroll: Breaking into the US!')
st.sidebar.markdown('by Group Mic :microphone2: | DSFC10')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "The Project":
    Pages.introduction()

elif selection == "Big News for Zack!":
    Pages.demog()

elif selection == "Zack Tabudlo: Background":
    Pages.show_factors_and_profile()

elif selection == "Zack Tabudlo: Statistics":
    Pages.show_conclusion()

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