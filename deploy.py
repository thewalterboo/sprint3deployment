import streamlit as st
from pages import Pages

list_of_pages = [
    "The Project",
    "NOBITA's Origins",
    "NOBITA's Musical Numbers",
    "Methods and Analysis",
    "Recommender Engines",
    "Playlists",
    "Conclusions and Recommendations"

]

st.sidebar.title('Beating the Beats of NOBITA! :notes:')
st.sidebar.markdown('by Group py2n :snake: | DSFC11')
st.sidebar.image("sidebarpic.jpg")
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "The Project":
    Pages.introduction()

elif selection == "NOBITA's Origins":
    Pages.origins()

elif selection == "NOBITA's Musical Numbers":
    Pages.statistics()

elif selection == "Methods and Analysis":
    Pages.pitch()

elif selection == "Recommender Engines":
    Pages.rec_engines()

elif selection == "Playlists":
    Pages.playlists()

elif selection == "Conclusions and Recommendations":
    Pages.conc_recomm()