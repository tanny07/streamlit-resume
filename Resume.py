import streamlit as st
from pathlib import Path
from PIL import Image 
from streamlit_option_menu import option_menu
from bokeh.models.widgets import Div



############################################ General Settings ###########################################################

# PAGE LAYOUT

st.set_page_config(
    page_title = "Digital Resume", 
    layout="wide",
    page_icon="✨"
) 
st.title(" Digital Resume ")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir / "profile.png"

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
        st.subheader("Data Science Graduate")
        st.write("Email : tanmaymondkar07@gmail.com")

    with col2:
        image = Image.open(profile_pic)
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

        
        with st.sidebar:

            st.markdown('# Links', unsafe_allow_html=True)  

            st.write(" Github : [link](https://github.com/tanny07)")
            st.write(" LinkedIn : [link](https://www.linkedin.com/in/mondkartanmay)")
            st.write(" Address : [link](https://goo.gl/maps/axbpvEqEDT9J9jeG7)")
 
            st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name= "TanmayMondkarCV.pdf",
            mime="application/octet-stream",)
   
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
                    - Jira
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
                - EPITA - Ecole d'ingénieurs informatique - Paris, France (Septembre, 2021 - Juillet, 2023)

                ### BACHELOR'S SCIENCES EN TECHNOLOGIE DE L'INFORMATION  
                - Mumbai University - Mumbai, India (juillet, 2018 - Mai, 2021)
                ''')


############################################ Experience Function(Français) ##############################################################


    def Expérience():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### VIRTUAL REALITY PRODUCT DATA ANALYST - MASTER's of CS INTERNSHIP
                ##### EMPLACEMENT - MGM'S COLLEGE OF COMPUTER SCIENCE, NAVI MUMBAI, INDIA
                - Dirigé le développement d'une application mobile VR pour la formation médicale, ce qui a permis une économie de 200 € par formation en RCR - deux fois par mois.
                - En tant que Data Product Owner, j'étais responsable de la collecte, de la protection et de la gestion des données des utilisateurs.
                - Responsable de la création de capteurs tactiles pour la collecte et le stockage de données.
                - Creating and documentation of research papers, reports, regarding the development of the product.
                - Développement d'un tableau de bord KPI pour la performance de la formation CPR.
                - Technologies mises en œuvre dans le développement : Unity3d, C#, C++, Python, Data Analytics, développement Arduino, SQL, AWS - Cloud, Jira.

                
                ### HIGH PERFORMANCE DATA ANALYST - WORK STUDY/ VOLUNTEER
                ##### EMPLACEMENT - ROSHAN CRICKET CLUB, NAVI MUMBAI, INDIA
                - Développement de tableaux de bord KPI pour plus de 200 joueurs de cricket d'un club. Ma principale responsabilité était de gérer, d'exploiter et d'analyser les données.
                - Techniques de vision par ordinateur optimisées pour analyser les performances vidéo des joueurs de cricket avec un taux de réussite effectif de plus de 95%.
                - Impliqué dans l'équipe Analytics qui a fourni des solutions techniques en temps réel à l'aide d'Excel, SQL, Tableau, Kinovea et de logiciels de correspondance personnalisés.         
                - ### Liens vers le travail du projet :
                - ###### OPEN PROJECT : [link](https://www.linkedin.com/posts/mondkartanmay_datavisualization-cricket-indiancricket-activity-6736244448189059072-ZFJ2?utm_source=share&utm_medium=member_desktop)
                - ###### OPEN PROJECT : [link](https://www.linkedin.com/posts/mondkartanmay_performanceanalysis-datavisualization-dataanalytics-activity-6732320808548515840-gX6u?utm_source=share&utm_medium=member_desktop)
                ''')

############################################ Projects Function (Français) ##############################################################

    def Projets():


        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### TABLEAU DE BORD (IPL DATASET)- DASH PLOTLY    
                - L'ensemble de données comprenait plusieurs fichiers CSV en tant qu'enregistrement individuel, d'équipe et d'enregistrement au sol. Techniques de prétraitement des données mises en œuvre lors de l'analyse.
                - Dans le processus EDA, j'ai créé plusieurs graphiques à l'aide de bibliothèques python pour les implémenter en dash plotly. 
                - Technologie implémentée : python, pandas, matplotlib, numpy, dash, html-css.
                - ###### OPEN PROJECT : [link](https://github.com/tanny07/Dash-Plotly)

                ### TABLEAU DE BORD (BREAST CANCER DATASET) - STREAMLIT 
                - Le tableau de bord consiste en une analyse de l'ensemble de données sur le cancer du sein de la bibliothèque sklearn.
                - L'analyse se compose de quatre graphiques qui peuvent être configurés selon les besoins.
                - Technologie implémentée : python,sklearn, pandas, matplotlib, numpy, streamlit, html.
                - ###### OPEN PROJECT : [link](https://tanny07-streamlit-dashboard-dashboard-tanny-y6gu34.streamlitapp.com/)
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
        image = Image.open(profile_pic)
        st.image(image, width= 200)

############################################ Navigation Bar(Angais) ##############################################################

    selection = option_menu(None, ["Profile", "Education", "Experience", "Projects"],
                       icons=['badge-tm', 'building', 'briefcase', 'bookmark-check'],
                       menu_icon="cast", default_index=0, orientation="horizontal")

############################################ Proflie Function (Anglais) ##############################################################

    def profile():
        resume_file = "/Users/tanmaymondkar/Documents/France_Epita/streamlit-resume/TanmayMondkarResume.pdf"
        with open("TanmayMondkarResume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
    
        with st.sidebar:

            st.markdown('# Links', unsafe_allow_html=True)  

            st.write(" Github : [link](https://github.com/tanny07)")
            st.write(" LinkedIn : [link](https://www.linkedin.com/in/mondkartanmay)")
            st.write(" Address : [link](https://goo.gl/maps/axbpvEqEDT9J9jeG7)")
 
            st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name= "TanmayMondkarCV.pdf",
            mime="application/octet-stream",)
                
        st.markdown('## Summary', unsafe_allow_html=True)
        st.info('''
                - I am a 23 year young data science graduate who enjoys exploring various fields and sectors in IT where I can utilise my experience and knowledge of Computer Science 
                - I have experience of working in SportsTech and MedTech industries.
                - I enjoy working in a team and I know how to manage time and risks while being motivated and goal-oriented.
                - I love talking with people to share and learn to develop strategies and improve productivity.
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
                    - Jira
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
                - EPITA - Ecole d'ingénieurs informatique - Paris, France (September, 2021 - July, 2023)

                ### BACHELOR'S OF INFORMATION TECHNOLOGY  
                - Mumbai University - Mumbai, India (July, 2018 - May, 2021)
                ''')


############################################ Experience Function(Angais) ##############################################################


    def Experience():

        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### VIRTUAL REALITY PRODUCT DATA ANALYST - MASTER's of CS INTERNSHIP
                #### LOCATIOIN - MGM'S COLLEGE OF COMPUTER SCIENCE, NAVI MUMBAI, INDIA
                - Leaded the development of VR mobile application for medical training resulting in cost saving of €200 per CPR training - twice a month.
                - As a Data Product Owner I was responsible for collection, protection and management of user's data.
                - Responsible for creating touch sensors for data collection and storage.
                - Creating and documentation of research papers, reports, regarding the development of the product.
                - Development of KPI dashboard for the CPR training performance.
                - Implemented technologies in the development : Unity3d, C#, C++, Python, Data Analytics, Arduino development, SQL, AWS - Cloud, Jira.
                
                ### HIGH PERFORMANCE DATA ANALYST - WORK STUDY/ VOLUNTEER 
                #### LOCATION - ROSHAN CRICKET CLUB - MUMBAI, INDIA 
                - Development of KPI dashboards for over 200 cricketers at a club. My main responsibility was to manage, exploit and analyze data.
                - Computer vision techniques optimized to analyze the video performance of cricketers with an effective success rate of over 95%.
                - Involved in the Analytics team which provided real-time technical solutions using Excel, SQL, Tableau, Kinovea and custom matching software.         
                - ### Links to Project Work :
                - ###### OPEN PROJECT : [link](https://www.linkedin.com/posts/mondkartanmay_datavisualization-cricket-indiancricket-activity-6736244448189059072-ZFJ2?utm_source=share&utm_medium=member_desktop)
                - ###### OPEN PROJECT : [link](https://www.linkedin.com/posts/mondkartanmay_performanceanalysis-datavisualization-dataanalytics-activity-6732320808548515840-gX6u?utm_source=share&utm_medium=member_desktop)
                ''')

############################################ Projects Function (Angais) ##############################################################

    def Projects():


        st.markdown('## ', unsafe_allow_html=True)
        st.info('''
                ### IPL DATASET DASHBOARD (SPORTS DATA) - DASH PLOTLY   
                - The dataset included multiple CSV files as individual, team and ground recording. Data pre-processing techniques implemented during the analysis.
                - In the EDA process, I created several plots using python libraries to implement them in dash plotly 
                - Implemented technology: python, pandas, matplotlib, numpy, dash, html-css
                - ###### OPEN PROJECT : [link](https://github.com/tanny07/Dash-Plotly)

                ### BREAST CANCER DATASET - DASHBOARD USING STREAMLIT  
                - The dashboard consists of an analysis of the breast cancer dataset from the sklearn library.
                - The analysis consists of four charts that can be configured as needed
                - Implemented technology: python, sklearn, pandas, matplotlib, numpy, streamlit, html
                - ###### OPEN PROJECT : [link](https://tanny07-streamlit-dashboard-dashboard-tanny-y6gu34.streamlitapp.com/)
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

############################################ Language Option ####33###############################################################

if option == 'Français':
    Francais()
if option == 'Anglais':
    Anglais()


