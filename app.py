from PIL import Image 
import requests
import streamlit as st 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Iyed Zarrougui Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


#---Load Assets
lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/375516612_830530748450079_5431732182712240573_n.jpg")
img_lottie_animation = Image.open("images/Capture d'écran 2023-11-12 175928.png")
img_sign = Image.open("images/sign.jpg")
img_rgb = Image.open("images/rgb.jpg")

# Add a navbar with links to different sections
def navbar():
    st.sidebar.title("Navigation")
    options = ["Home","Projects","About Me","Contact"]
    selection = st.sidebar.radio("Go to", options)

    return selection

#Header section 
selection = navbar()

#----Home-----
if selection == "Home":
    st.subheader("Hi I am Iyed Zarrougui :wave:")
    st.title("A Computer Engineering Student from Tunisia")
    st.write("I am passionate about finding new ways to use Python and Cloud Computing to be more efficient and effective.")
    st.write("[LinkedIn Profile >] (https://www.linkedin.com/in/iyedzarrougui/)")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do?")
            st.write("""
            I specialize in turning innovative ideas into impactful solutions by combining technical expertise with creativity.  

            🔹 **Web Development & Software Engineering:**  
            I design and build dynamic applications, including event management systems and travel platforms, using technologies like Flask, Streamlit, and Java.  

            🔹 **Cloud Computing & Systems Design:**  
            I explore and implement scalable, robust solutions to optimize application performance.  

            🔹 **Collaboration & Knowledge Sharing:**  
            Passionate about teamwork, mentoring, and sharing knowledge through clubs and collaborative initiatives.  

            🚀 Let’s connect and work on shaping smarter, transformative solutions together!
            """)
            st.write("[Github Profile >] (https://www.github.com/iyedzarrougui14)")

        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")


if selection=="About Me":
    st.title("About Me")
    st.write("##")

    st.subheader("Hi! I'm Iyed Zarrougui")
    st.markdown("""
    I'm a **Computer Engineering student** at the **Higher Institute of Computer Science and Multimedia of Sfax (ISIMSF)**, with a strong passion for **cloud computing** and **Python**.  
    During my time at the **Faculty of Sciences of Gafsa**, I had the honor of being the **top of my class** for three consecutive years during my **Bachelor's degree** in **Computer Science**.  
    I have a deep interest in **software engineering**, **cloud engineering**, and **telecommunication engineering**, and I thrive on developing innovative solutions that can address real-world challenges.

    Here’s a brief overview of my journey:
    - Currently pursuing my **Engineer's degree** in **Computer Engineering** at **ISIMSF**.
    - **Major of Promotion** for three years at the **Faculty of Sciences of Gafsa**, consistently ranking as the top student throughout my Bachelor’s degree.
    - I developed a **telemedicine application** as part of my **final-year internship** (PFE) with Dr. Kamel Besbes and CRMN, integrating the app into the **ReaRobot** mobile robot.
    - I have worked on projects such as **emotion detection using CNNs**, **hand gesture detection with MediaPipe**, and real-time **sign language recognition**.
    - I am also passionate about expanding my knowledge in **cloud computing**, **AI**, and **data engineering**, and I am currently preparing for the **Google Cloud Digital Leader certification**.

    In addition to my technical pursuits, I am actively involved in initiatives like **Formation des Formateurs** and have a keen interest in **biomedical engineering**.  
    I aim to leverage my skills in **cloud computing** and **Python** to develop impactful technologies, particularly in the fields of **healthcare** and **artificial intelligence**.

    **What excites me the most** is the potential for **AI and cloud technologies** to transform industries and make a real difference in people’s lives. I am dedicated to being part of this transformation by continually enhancing my skills and sharing knowledge with others.
    """)
    
    st.write("##")

    st.subheader("My Journey & Future Goals")
    st.markdown("""
    - **Passion for Cloud & Python:** With a strong foundation in **Python programming** and **cloud computing**, I am committed to staying ahead of the curve in these rapidly evolving fields.
    - **Innovative Problem Solver:** I focus on solving complex problems through **machine learning**, **AI**, and **data engineering** to build systems that improve efficiency and accessibility.
    - **Collaboration and Growth:** I thrive in collaborative environments and look forward to working with like-minded professionals to create meaningful, real-world solutions.
    - **Continued Learning:** I am always eager to learn and grow, currently expanding my knowledge in **cloud platforms** and **AI applications** to further my impact in these domains.
    
    As I continue my studies and explore new opportunities, I am excited to contribute to the **future of technology**, particularly in **healthcare**, **AI**, and **cloud innovation**.
    """)

    st.write("##")

    st.subheader("Let's Connect!")
    st.markdown("""
    You can reach me through my professional networks:

    - [LinkedIn Profile](https://www.linkedin.com/in/iyedzarrougui/)
    - [GitHub Profile](https://www.github.com/iyedzarrougui14)
    - [Email](mailto:iyed.zarrougui@example.com)

    I'm always excited to connect with fellow engineers, innovators, and anyone passionate about the future of technology!
    """)

#----Projects-----
if selection == "Projects":
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("Emotion Detection using CNN")
            st.markdown("""**Description**: I undertook the development of an emotion detection system using convolutional neural networks (CNNs). The goal of this project was to accurately recognize human emotions from facial images. Employing deep learning techniques, I designed a robust model capable of classifying emotions, including happiness, sadness, anger, and more, with high accuracy.""")

    with st.container():
        image_column, text_column = st.columns(((1,2)))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Hand Gesture Detection using MediaPipe")
            st.markdown("""**Description**: I developed a real-time hand gesture detection system using MediaPipe, enabling instantaneous interpretation and response to manual movements. Leveraging the capabilities of MediaPipe, the project explores precise recognition of hand motions in real-time, offering an immersive and touchless user interface experience. This innovative approach not only enhances interaction but also provides immediate and dynamic responsiveness, making it suitable for applications in real-time scenarios across various fields, including virtual reality, robotics, and advanced human-machine interfaces.""")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_sign)  # Replace with the relevant project image
        with text_column:
            st.subheader("Real-Time Sign Language Detection using MediaPipe and Keras")
            st.markdown("""
            **Description**: This project focuses on improving accessibility through technology.  
            I built a real-time system that uses **MediaPipe** for accurate hand tracking and **Keras** to classify sign language characters.  
            By combining computer vision and deep learning, the system bridges the gap for those with hearing impairments, enabling seamless communication. This project underscores the potential of innovative solutions to foster inclusivity and accessibility in our digital world.
            """)

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            img_landmarks = Image.open("images/landmarks.jpg")  # Replace with the relevant project image
            st.image(img_landmarks)
        with text_column:
            st.subheader("Face and Hand Landmarks Detection using Python – Mediapipe, OpenCV")
            st.markdown("""
            **Description**: This project leverages the capabilities of **MediaPipe** and **OpenCV** to detect and track facial and hand landmarks in real-time.   
            Key features include:  
            - **MediaPipe's Holistic Model**: Used for comprehensive detection of facial and hand landmarks, ensuring precise and reliable results.  
            - **Real-Time Processing**: Implemented video capture and processing pipelines with **OpenCV**, achieving smooth and responsive landmark tracking.  
            """)

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_rgb)  # Replace with the relevant project image
        with text_column:
            st.subheader("Detect RGB Color from Webcam using Python – OpenCV")
            st.markdown("""
            **Description**: In this project, I developed a real-time tool that captures video from a webcam and detects the RGB values of any point in the frame. Using **Python** and **OpenCV**, this tool showcases the power of computer vision for color detection and analysis. It's a step forward in understanding how real-time image processing can be applied in various domains.
            """)

    # Load the image for the AutoML section
    img_automl = Image.open("images/automl.png")

    # Display the project in a container
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_automl)
        with text_column:
            st.subheader("AutoML Model Training and Prediction")
            st.markdown("""
            **Description**: This AutoML project focuses on training and deploying machine learning models without requiring detailed manual intervention. 
            Using an automated pipeline, the goal is to efficiently create models by selecting the best features and algorithms for a given dataset.
            In this demo, I trained a Random Forest model on the **Iris dataset**, but you can extend this approach for different datasets and algorithms.
            The AutoML pipeline automates model training, tuning, and evaluation for optimal performance, making it easier to deploy models for real-time predictions.
            """)

    # Load image for the project
    img_rearobot = Image.open("images/tab2.jpg")

    with st.container():
        image_column, text_column = st.columns((1, 2))  
        with image_column:
            st.image(img_rearobot)  
        with text_column:
            st.subheader("Development of a Telemedicine Application on a Mobile Robot")
            st.markdown("""
            **Description**:  
            This project focuses on developing a telemedicine application integrated into a mobile robot, aimed at providing remote healthcare services. By enabling real-time interaction between doctors and patients, the robot leverages cutting-edge technologies such as AI, robotics, and telecommunication. This innovative solution makes healthcare more accessible, efficient, and responsive, especially in remote areas.
    
            **Key Features**:
            - **Real-Time Video Conferencing**: Enables seamless communication between doctors and patients for consultations.
            - **Health Monitoring**: The robot is equipped with sensors to monitor vital signs like heart rate, temperature, and blood pressure, providing real-time health data.
            - **Diagnostic Tools**: Integrated tools for diagnostic support, helping doctors make informed decisions remotely.
            """)

# ---- Contact Form Section ----
if selection == "Contact":
    with st.container():
        st.write("---")

        # Form HTML with added CSS for centering
        contact_form = """
        <style>
            .centered-form {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                max-width: 500px;
                margin: 0 auto;
            }
            h4{
                text-align: center;
            }
            input, textarea, button {
                margin: 10px 0;
                padding: 10px;
                font-size: 16px;
                width: 100%;
                max-width: 400px;
            }
            button {
                cursor: pointer;
                background-color: #4CAF50;
                color: white;
                border: none;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
        <h4>Get in touch with me!</h4>
        <form class="centered-form" action="https://formsubmit.co/iyedzarrou14@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        # Center the form directly in the container
        st.markdown(contact_form, unsafe_allow_html=True)
