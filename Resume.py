from pathlib import Path
import streamlit as st
from PIL import Image 
from streamlit_option_menu import option_menu
from bokeh.models.widgets import Div
import streamlit.components.v1 as components


############################################ General Settings ###########################################################

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



############################################ For Langauge Selection Box #################################################
col1, col2, col3 = st.columns(3)

with col1 :
    pass
with col2 :
    pass
with col3 :
    option = st.selectbox(
        'Digital Resume Language',
        ('Français', 'Anglais'))

def Francais():

    col1, col2 = st.columns(2)

    with col1:
        st.header("Tanmay MONDKAR")
        st.subheader("Data Analyst")
        st.write("Email : tanmaymondkar07@gmail.com")

    with col2:
        image = Image.open("/Users/tanmaymondkar/Documents/France_Epita/streamlit-resume/Profile.png")
        st.image(image, width= 200)

############################################ Navigation Bar(Français) ##############################################################

    selection = option_menu(None, ["Profil", "Formation", "Expérience", "Projets"],
                        icons=['badge-tm', 'building', 'briefcase', 'bookmark-check'],
                        menu_icon="cast", default_index=0, orientation="horizontal")

############################################ Proflie Function (Français) ##############################################################


    def profil():
        resume_file = "/Users/tanmaymondkar/Documents/France_Epita/streamlit-resume/TanmayMondkarCV.pdf"
        with open("TanmayMondkarCV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        col1, col2, col3,col4 = st.columns(4)

        with col1:
            if st.button('Github'):
                js = "window.open('https://github.com/tanny07')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)

        with col2:
                st.download_button(
            label="Resume",
            data=PDFbyte,
            file_name= "TanmayMondkarCV.pdf",
            mime="application/octet-stream",)
    
        with col3:
            if st.button('LinkedIn'):
                js = "window.open('https://www.linkedin.com/in/mondkartanmay')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)
 
        with col4:
            if st.button('Address'):
                js = "window.open('https://goo.gl/maps/axbpvEqEDT9J9jeG7')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)

              

        st.markdown('## Sommaire', unsafe_allow_html=True)
        st.info('''
                - Je suis un analyste de données de 22 ans qui aime analyser les données et raconter des histoires avec. 
                - Parmi mes compétences figurent SQL, Excel, Python, PowerBI, Tableau, Dataiku, AWS-Cloud et Github.
                - J'aime travailler en équipe et sait gérer le temps et les risques tout en étant organisé et axé sur les objectifs 
                - J'apprécie de parler avec les gens pour partager et apprendre comment les choses fonctionnent afin d'améliorer la productivité.
                ''')  

        st.markdown('## Langues Parlées', unsafe_allow_html=True)
        st.info('''
                - Français
                - Anglais
                - Hindi
                - Marathi
                ''')

        st.markdown('## Compétences', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1 :
            st.info('''
                    #### Compétences Techniques 
                    - Python Programming langauge 
                    - Streamlit  
                    - SQL and PostgreSQL
                    - Data Analytics Softwares  
                    - AWS Cloud
                    - Machine Learning Algorithms 
                    ''')

        with col2 :
            st.info('''
                #### Compétences Générales 
                - Gestion du temps
                - Résolution de problème
                - Enthousiaste
                - Rayonnement
                - Joueur d'équipe
                - Souplesse
                ''')


        
############################################ Education Function(Français) ##############################################################

    def Formation():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### MASTER INFORMATIQUE SPÉCIALISATION DATA SCIENCE   
                - EPITA - Ecole d'ingénieurs informatique - Paris, France (Septembre, 2021 - Present)

                ### BACHELOR'S SCIENCES EN TECHNOLOGIE DE L'INFORMATION  
                - Mumbai University - Mumbai, India (juillet, 2018 - Mai, 2021)
                ''')


############################################ Experience Function(Français) ##############################################################


    def Expérience():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### HIGH PERFORMANCE DATA ANALYST - VOLUNTEER (ROSHAN CRICKET CLUB) - MUMBAI, INDIA   
                - Développement de tableaux de bord KPI pour plus de 200 joueurs de cricket d'un club. Ma principale responsabilité était de gérer, d'exploiter et d'analyser les données.
                - Techniques de vision par ordinateur optimisées pour analyser les performances vidéo des joueurs de cricket avec un taux de réussite effectif de plus de 95%.
                - Impliqué dans l'équipe Analytics qui a fourni des solutions techniques en temps réel à l'aide d'Excel, SQL, Tableau, Kinovea et de logiciels de correspondance personnalisés.         
                ''')
        
        st.markdown('## Analyse de mouvement', unsafe_allow_html=True)

        st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C4E22AQGiR6-wDSaQpA/feedshare-shrink_800/0/1606045828233?e=1667433600&v=beta&t=gPnFwQGDxDDMBtcUe4Lcmz8ZRf2yEHIJLqQunKYrn4k)](https://www.linkedin.com/posts/mondkartanmay_datavisualization-cricket-indiancricket-activity-6736244448189059072-ZFJ2?utm_source=share&utm_medium=member_desktop)")

        st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C4E22AQErnYer7XlPDA/feedshare-shrink_800/0/1605110360541?e=1667433600&v=beta&t=Pv9ZBGjr82QlRpF8V-U4tbb4hWZ6ZBOa9-QkozJ8Q7Q)](https://www.linkedin.com/posts/mondkartanmay_performanceanalysis-datavisualization-dataanalytics-activity-6732320808548515840-gX6u?utm_source=share&utm_medium=member_desktop)")


############################################ Projects Function (Français) ##############################################################

    def Projets():


        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### TABLEAU DE BORD (IPL DATASET)- DASH PLOTLY    
                - L'ensemble de données comprenait plusieurs fichiers CSV en tant qu'enregistrement individuel, d'équipe et d'enregistrement au sol. Techniques de prétraitement des données mises en œuvre lors de l'analyse.
                - Dans le processus EDA, j'ai créé plusieurs graphiques à l'aide de bibliothèques python pour les implémenter en dash plotly. 
                - Technologie implémentée : python, pandas, matplotlib, numpy, dash, html-css.
                - Project Link : https://github.com/tanny07/Dash-Plotly

                ### TABLEAU DE BORD (BREAST CANCER DATASET) - STREAMLIT 
                - Le tableau de bord consiste en une analyse de l'ensemble de données sur le cancer du sein de la bibliothèque sklearn.
                - L'analyse se compose de quatre graphiques qui peuvent être configurés selon les besoins.
                - Technologie implémentée : python,sklearn, pandas, matplotlib, numpy, streamlit, html.
                - Project Link : https://tanny07-streamlit-dashboard-dashboard-tanny-y6gu34.streamlitapp.com/
                ''')


############################################ Function call(Français) ##############################################################

    if selection == 'Profil':
        profil()

    if selection == 'Formation':
        Formation()

    if selection == 'Expérience':
        Expérience()

    if selection == 'Projets':
        Projets()





############################################ For Title Bar (Anglais) ##############################################################
def Anglais():

    col1, col2 = st.columns(2)

    with col1:
        st.header("Tanmay MONDKAR")
        st.subheader("Data Analyst")
        st.write("Email : tanmaymondkar07@gmail.com")

    with col2:
        image = Image.open("/Users/tanmaymondkar/Documents/France_Epita/streamlit-resume/Profile.png")
        st.image(image, width= 200)

############################################ Navigation Bar(Angais) ##############################################################

    selection = option_menu(None, ["Profile", "Education", "Experience", "Projects"],
                       icons=['badge-tm', 'building', 'briefcase', 'bookmark-check'],
                       menu_icon="cast", default_index=0, orientation="horizontal")

############################################ Proflie Function (Angais) ##############################################################

    def profile():
        resume_file = "/Users/tanmaymondkar/Documents/France_Epita/streamlit-resume/TanmayMondkarResume.pdf"
        with open("TanmayMondkarResume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        col1, col2, col3,col4 = st.columns(4)

        with col1:
            if st.button('Github'):
                js = "window.open('https://github.com/tanny07')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)

        with col2:
                st.download_button(
            label="Resume",
            data=PDFbyte,
            file_name= "TanmayMondkarResume.pdf",
            mime="application/octet-stream",)
    
        with col3:
            if st.button('LinkedIn'):
                js = "window.open('https://www.linkedin.com/in/mondkartanmay')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)
 
        with col4:
            if st.button('Adresse'):
                js = "window.open('https://goo.gl/maps/axbpvEqEDT9J9jeG7')" 
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)

        st.markdown('## Summary', unsafe_allow_html=True)
        st.info('''
                - I am a 22 year old data analyst who enjoys analyzing data and telling stories with it. 
                - Among my skills are SQL, Excel, Python, PowerBI, Tableau, Dataiku, AWS-Cloud and Github. 
                - I enjoy working in a team and know how to manage time and risks while being organized and goal-oriented. 
                - I enjoy talking with people to share and learn how things work to improve productivity.
                ''')

        st.markdown('## Skills', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1 :
            st.info('''
                    #### Hard Skills 
                    - Python Programming langauge 
                    - Streamlit  
                    - SQL and PostgreSQL
                    - Data Analytics Softwares  
                    - AWS Cloud
                    - Machine Learning Algorithms 
                    ''')

        with col2 :
            st.info('''
                #### Soft Skills 
                - Time Management
                - Problem Solving
                - Enthusiatic
                - Influence
                - Team Player
                - Flexibility
                ''')

############################################ Education Function(Angais) ##############################################################

    def Education():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### MASTER'S OF COMPUTER SCIENCE SPECIALIZATION IN DATA SCIENCE   
                - EPITA - Ecole d'ingénieurs informatique - Paris, France (September, 2021 - Present)

                ### BACHELOR'S OF INFORMATION TECHNOLOGY  
                - Mumbai University - Mumbai, India (July, 2018 - May, 2021)
                ''')


############################################ Experience Function(Angais) ##############################################################


    def Experience():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### HIGH PERFORMANCE DATA ANALYST - VOLUNTEER (ROSHAN CRICKET CLUB) - MUMBAI, INDIA   
                - Development of KPI dashboards for over 200 cricketers at a club. My main responsibility was to manage, exploit and analyze data.
                - Computer vision techniques optimized to analyze the video performance of cricketers with an effective success rate of over 95%.
                - Involved in the Analytics team which provided real-time technical solutions using Excel, SQL, Tableau, Kinovea and custom matching software.         
                ''')

        st.markdown('## Motion Analysis', unsafe_allow_html=True)

        st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C4E22AQGiR6-wDSaQpA/feedshare-shrink_800/0/1606045828233?e=1667433600&v=beta&t=gPnFwQGDxDDMBtcUe4Lcmz8ZRf2yEHIJLqQunKYrn4k)](https://www.linkedin.com/posts/mondkartanmay_datavisualization-cricket-indiancricket-activity-6736244448189059072-ZFJ2?utm_source=share&utm_medium=member_desktop)")

        st.markdown("[![Foo](https://media-exp1.licdn.com/dms/image/C4E22AQErnYer7XlPDA/feedshare-shrink_800/0/1605110360541?e=1667433600&v=beta&t=Pv9ZBGjr82QlRpF8V-U4tbb4hWZ6ZBOa9-QkozJ8Q7Q)](https://www.linkedin.com/posts/mondkartanmay_performanceanalysis-datavisualization-dataanalytics-activity-6732320808548515840-gX6u?utm_source=share&utm_medium=member_desktop)")


############################################ Projects Function (Angais) ##############################################################

    def Projects():


        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### IPL DATASET DASHBOARD (SPORTS DATA) - DASH PLOTLY   
                - The dataset included multiple CSV files as individual, team and ground recording. Data pre-processing techniques implemented during the analysis.
                - In the EDA process, I created several plots using python libraries to implement them in dash plotly 
                - Implemented technology: python, pandas, matplotlib, numpy, dash, html-css
                - Project Link : https://github.com/tanny07/Dash-Plotly

                ### BREAST CANCER DATASET - DASHBOARD USING STREAMLIT  
                - The dashboard consists of an analysis of the breast cancer dataset from the sklearn library.
                - The analysis consists of four charts that can be configured as needed
                - Implemented technology: python, sklearn, pandas, matplotlib, numpy, streamlit, html
                - Project Link : https://tanny07-streamlit-dashboard-dashboard-tanny-y6gu34.streamlitapp.com/
                ''')

############################################ Function call(Angais) ##############################################################

    if selection == 'Profile':
        profile()

    if selection == 'Education':
        Education()

    if selection == 'Experience':
        Experience()

    if selection == 'Projects':
        Projects()

############################################ Function call(Angais) ##############################################################

if option == 'Français':
    Francais()
if option == 'Anglais':
    Anglais()


