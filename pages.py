import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")
st.set_page_config (layout="wide")



class Pages:
    
    # Page 1 - "The Project"
    def introduction():
    # Write the title and the subheader
        st.title(
            "Beating the Beats of NOBITA!"
        )
        st.subheader(
            'by Group py2n :snake: | DSFC11'
            )
        st.markdown('Denise | Patrick | Walter | Mentor: Andres')

        st.image("1.png")

        col1, col2 = st.columns(2)

        with col1:
            st.image("page1col1.jpg")

        with col2:
            st.title('A Data-Driven Approach to Improving NOBITA\'s Chart Performance.')
            st.subheader('Empowering OPM artists in the Philippines and beyond.')

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Check out Nobita's all time hit, Ikaw Lang!")
            st.video("https://www.youtube.com/watch?v=rxXsdj7EBm4", format="video", start_time=0)

        with col2:
            st.image("page1col2.jpg")


        

    # Page 2 - "NOBITA's Origins"
    def origins():
        # Write the title
        st.title(
            "An origin story unlike any other"
        )
        st.image("page2pic1.png")
        st.caption(
            "According to Sony Music Philippines, NOBITA is a 5-piece Pop Rock band known for their unique take on hugot love songs, such as Ikaw Lang and Unang Sayaw. The band’s layered arrangements are reminiscent of old school Pinoy rock, mixed with intricate vocal blending.")

        # tab_educ, tab_emp, tab_sex = st.tabs(["Education", "Employment", "Sex"])
       
        # with tab_educ:
        #     # Show in terms of educational attainment
        #     st.subheader("In terms of Educational Attainment")
        #     st.markdown("""
        #     ##### Among the unbanked Filipinos aged 21 and above, around 56% have finished up to secondary level or high school only.
        #     """)

        # with tab_emp:
        #     # Show in terms of employment status
        #     st.subheader("In terms of Employment Status")
        #     st.markdown("""
        #     ##### 4 out of 6 unbanked adult Filipinos are unemployed.
        #     """)


        # with tab_sex:
        #     # Show in terms of gender
        #     st.subheader("In terms of Sex")
        #     st.markdown("""
        #     ##### There are more adult _female_ Filipinos who are unbanked than males.
        #     """)



    # Page 3 - "NOBITA's Musical Numbers"
    def statistics():
        # Write the title
        st.title(
            "NOBITA, by the Numbers"
        )

        st.image("3.png")
        st.image("4.png")

                
                
                
                
        

    # Page 5 - "The Pitch"
    def pitch():
    # Write the title and the subheader
        st.title(
            "The question now is, how can we help Zack make US hits?"
        )
        st.image('page5pic1.png')
        st.image("page51.png")
        st.image("page4picc2.png")
        st.image("page5pic22.png")
        st.image("page5pic23.png")
        st.image("page52.png")
        st.image("page53.png")
        st.image("17.png")
        st.image("18.png")
        st.image("19.png")
        st.image("20.png")
        st.image("21.png")
        st.image("22.png")
        st.image("23.png")
        st.image("24.png")
        st.image("26.png")
        st.image("27.png")
        
        



    # Page 6 - "Recommender Engines"
    def rec_engines():
    # Write the title and the subheader
        st.title(
            "Methodology and Recommender Engine"
        )
        st.subheader(
            "Here is the pipeline that we followed, analyzing the related songs and artists to Zack. We utilized a recommender pool of tracks from the Spotify Philippines Top 200 Charts."
        )
        st.image('page6pic1.png')

    # Page 7 - "Playlists"
    def playlists():
    # Write the title and the subheader
        st.title(
            "Suggested Songs and Playlists"
        )

        st.subheader(
            "These are the recommended songs from our engine."
        )
        reco = pd.read_csv("fullreco_playlist.csv")
        reco = reco[["track_name", "artist_name"]]
        reco.rename(columns = {'track_name':'Track', 'artist_name' : 'Artist'}, inplace = True)  
        reco = reco.drop_duplicates()
        st.dataframe(reco)
        

    # Page 8 - "Conclusions and Recommendations"
    def conc_recomm():
    # Write the title and the subheader
        st.title(
            "So, how can we help make Zack Tabuldo make the next biggest hit in the United States?"
        )
        st.image("conclu.png")
