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

#Header section 
st.subheader("Hi I am Iyed :wave:")
st.title("A Computer Engineering Student from Tunisia")
st.write("I am passionate about finding new ways to use Python and Deep Learning to be more efficient and effective.")
st.write("[LinkedIn Profile >] (https://www.linkedin.com/in/iyedzarrougui/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do?")
        st.write("##")
        st.write(''' 👋 Hello there, I'm Iyed Zarrougui! 
                    🎓 Computer Engineering Student at the Faculty of Sciences, Gafsa.
💻 Passionate about coding and exploring new technologies.
🤖 Fascinated by the world of Artificial Intelligence Deep Learning and Web Development.
🌟 Always eager to learn and innovate.
🔍 Exploring the intersections of logic and creativity.
Dreaming of shaping a better digital future.
Connect with me and let's share our coding journeys!🤝''')
        st.write("[Github Profile >] (https://www.github.com/iyedzarrougui14)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


#----Projects-----

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Emotion Detection using CNN")
        st.markdown("""**Description**: I undertook the development of an emotion detection system using convolutional neural networks (CNNs). The goal of this project was to accurately recognize human emotions from facial images. Employing deep learning techniques, I designed a robust model capable of classifying emotions, including happiness, sadness, anger, and more, with high accuracy.""")
        st.markdown("[Demand me > ] (iyedzarrou14@gmail.com)")
        
with st.container():
    image_column, text_column = st.columns(((1,2)))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Hand Gesture Detection using MediaPipe")
        st.markdown("""**Description**: I developed a real-time hand gesture detection system using MediaPipe, enabling instantaneous interpretation and response to manual movements. Leveraging the capabilities of MediaPipe, the project explores precise recognition of hand motions in real-time, offering an immersive and touchless user interface experience. This innovative approach not only enhances interaction but also provides immediate and dynamic responsiveness, making it suitable for applications in real-time scenarios across various fields, including virtual reality, robotics, and advanced human-machine interfaces.""")
        st.markdown("[Demand me > ] (iyedzarrou14@gmail.com)")

#---- Contact -----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/el/hulimi" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <textarea name= "message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

