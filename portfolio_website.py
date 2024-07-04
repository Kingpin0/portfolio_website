import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Mehmet Akif Arslan")
    st.write("As a recent graduate of Ankara Yıldırım Beyazıt University in Aerospace Engineering, I would like to further develop myself in the field of flight dynamics and pursue a career in this field. I aim to make significant contributions to projects with my effective communication skills and technical knowledge in teamwork. My passion and commitment to aerospace engineering is combined with my desire to contribute to projects in this sector and play a role in the development of aviation technology. I look forward to taking part in future projects and contributing to the advancement of the aerospace industry.")

with col2:
    st.header("")
    st.image("images/vesikalik.jpg")

persona = """ 
            You are Mehmet Akif's AI bot. You help people answer questions about yourself (i.e Akif)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Mehmet Akif:
        
        Mehmet Akif was born in Trabzon on November 1, 2001. He has two names: Mehmet and Akif, but he prefers to use 
        Akif. He lived in Trabzon until he was six, and then he moved to 
        Ankara in 2006. Since then, he has lived in Ankara. Akif obtained his bachelor's degree in aerospace engineering.
        in 2024. He wants to pursue a career in the aircraft flight dynamics field. He is working on improving himself 
        on modeling and simulation, he is also interested in automatic flight control. He is a hard worker and has high
        communication skills which makes him a good team member. His hobbies are football, post-apocalyptic stories and
        walking. Especially he loves watching and playing football. He is a fan of Trabzonspor which is the greatest
        football team in Turkey. He has a girlfriend, Beyza, and he is deeply in love with her.
        
        Akif's e-mail: akifarslan001@gmail.com
        Akifs Linkedin: https://www.linkedin.com/in/mehmet-akif-arslan-3184b7254/
    
            """

st.title("Akif's AI Bot")
user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)


col1, col2 = st.columns(2)
with col1:
        st.subheader("Maneuver Control with 6 Degrees of Freedom Aircraft Model")
        st.write("- In this project I was a member of who created a 6-DOF aircraft model using simulink.")
        st.write("- By using this model and help of the PID controller we did Loop and Aileron Roll maneuvers.")
        st.write("- The paper we wrote is published in Lift-Up.")

with col2:
    st.video("images/loop.mp4")
    st.video("images/roll.mp4")

st.header("My Skills")
st.slider("MATLAB/Simulink", 0, 5, 4)
st.slider("Python", 0, 5, 4)
st.slider("Ansys/Fluent", 0, 5, 3)
st.slider("MS Office", 0, 5, 4)
st.slider("LaTex", 0, 5, 5)

st.write(" ")
st.write("Contact")
st.write("akifarslan001@gmail.com")
