
import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")




class Pages:
    st.set_page_config (layout="wide")
    # Page 1 - "The Project"
    def introduction():
    # Write the title and the subheader
        st.title(
            "Breaking Zack Tabudlo into the US!"
        )
        st.subheader(
            'by Group Mic :microphone: | DSFC10'
            )
        st.markdown('Div | Sofia | JA | Pim | Andres | R | Mentor: Mike')

        col1, col2 = st.columns(2)

        with col1:
            st.image("page1col1.jpg")

        with col2:
            st.title('Harnessing data to help Zack Tabudlo make big hits in US Charts.')
            st.subheader('Empowering OPM artists into the global stage.')

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Check out his latest release here!")
            st.video("https://www.youtube.com/watch?v=i_G6wewjOuY", format="video", start_time=0)

        with col2:
            st.image("page1col2.png")


        

    # Page 2 - "Big News for Zack!
    def news():
        # Write the title
        st.title(
            "Big News for Zack and other OPM Artists!"
        )
        st.image("page2pic1.png")
        st.caption(
            "Republic Records, the same record label with Ariana Grande, Drake, \
            Taylor Swift, John Legend, and many other major names in the US Music industry, launches in the Philippines \
            to **bring Filipino artists to the U.S.**")

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

    # Page 3 - "Zack Tabudlo: Background"
    def background():
        st.title(
            "Who is Zack Tabudlo?"
        )

        col1, col2 = st.columns(2, gap="small")

        with col1:
            st.image("page3hist1.png")

        with col2:
            st.image("page3hist2.png")
        
        

        st.subheader("Get to know Zack more!")
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.video("https://www.youtube.com/watch?v=dEVphwbu2xc", format="video", start_time=0)

        with col2:
            st.markdown('### Zack "Morning" Tabudlo has been present in the music industry since his first appearance in 2014.')
            st.markdown("### As the years progressed, Zack ventured into songwriting and music production. \
            In 2020, he joined Island Records Philippines where he continued honing his identity as a musician by releasing solo songs.")
            st.markdown('### He is now actively collaborating with other OPM and international artists such as **James TW, Billkin, James Reid, and Moira**.')
            st.write("Visit his channel [here](https://www.youtube.com/channel/UCkOcpvTzdGIygSbNGdaNdSg)!")
        
        

        


    # Page 4 - "Zack Tabudlo: Statistics"
    def statistics():
        # Write the title
        st.title(
            "Zack, by the Numbers"
        )

        tab1, tab2 = st.tabs(["Zack on Spotify", "Zack and Other OPM Artists"])

        # Songs
        with tab1:
            st.image("page4.png ")
            st.header("These are his solo release songs since 2018.")
            df_pg4 = pd.read_csv('Zack_Tabudlo_2.csv')
            df_pg4 = df_pg4.drop(['Album'], axis=1)
            df_pg4 = df_pg4.set_index('Year')
            df_pg4 = df_pg4.iloc[1:,:]
            st.dataframe(df_pg4, width = 1600)

        # Stats
        with tab2:
            st.markdown("""
            ## Here is Zack Tabuldo's music by the numbers, compared to other popular OPM artists.
            """)
            
            st.markdown("""
            #### Here's Zack compared to related SOLO artists.
            """)
            col1, col2 = st.columns(2, gap="large")

            with col1:
                
                st.image("page4pic4.png")
                st.image("page4pic5.png")
                st.image("page4pic6.png")
                

            with col2:
                st.image("page5pic22.png")
                st.image("page4pic2.png")
                
            
            st.markdown("""
            ####       
            """)
            st.markdown("""
            #### Here's Zack compared to related bands.
            """)
            col1, col2 = st.columns(2, gap="large")

            with col1:
                
                st.image("page4pic3.png")
                
            with col2:
                st.image("page5pic23.png")
                
                
                
        

    # Page 5 - "The Pitch"
    def pitch():
    # Write the title and the subheader
        st.title(
            "The question now is, how can we help Zack make US hits?"
        )
        st.image('page5pic1.png')
        st.image("page51.png")
        st.image("page52.png")
        st.image("page53.png")
        
        



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

    # Page 8 - "Conclusions and Recommendations"
    def conc_recomm():
    # Write the title and the subheader
        st.title(
            "So, how can we help make Zack Tabuldo make the next biggest hit in the United States?"
        )
    
    # Page 9 - "References"
    def references():
    # Write the title and the subheader
        st.title(
            "Project MabuhAI: Uncovering the Different Factors that Make up Unbanked Filipinos"
        )

