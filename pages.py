import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import steamlit.components.v1 as components
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

                
                
                
                
        

    # Page 4 - "Methods and Analysis"
    def pitch():
    # Write the title and the subheader
        st.title(
            "The question now is, how can we help NOBITA make the Daily Top 200?"
        )
        st.image('5.png')
        st.image("6.png")
        st.image("7.png")
        st.image("8.png")
        st.image("9.png")
        st.image("10.png")
        st.image("11.png")
        
        



    # Page 5 - "Recommender Engines"
    def rec_engines():
    # Write the title and the subheader
        st.title(
            "Methodology and Recommender Engine"
        )
        st.subheader(
            "Here is the pipeline that we followed, analyzing the related songs and artists to NOBITA. We utilized a recommender pool of tracks from the Spotify Philippines Top 200 Charts."
        )
        st.image('12.png')

    # Page 6 - "Playlists"
    def playlists():
    # Write the title and the subheader
        st.title(
            "Suggested Songs and Playlists"
        )

        st.subheader(
            "These are the recommended songs from our engine."
        )
        
        components.html('<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2GrafQPopdSdPobRxU6OST?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>')

        

    # Page 7 - "Recommendations and Conclusion"
    def conc_recomm():
    # Write the title and the subheader
        st.title(
            "So, how can we help make NOBITA get on the Daily Top 200?"
        )
        st.image("13.png")
        st.image("14.png")
        st.image("15.png")
        st.image("16.png")
