import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Mehmet Akif Arslan")
    st.write("I am a young, dynamic and hardworking engineer candidate who is constantly striving for self-development. I believe that I have high communication skills and I have experienced many times in my projects and internship processes that this feature has a positive effect on teamwork. My passion and determination in the field of aerospace engineering strengthens my goal of pursuing a career in this sector. I look forward to contributing to future projects and playing an important role in the development of aviation technology.")

with col2:
    st.header("")
    st.image("images/vesikalik.jpg")

persona = """ 
            You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza). Answer as if you are responding . dont answer in second or third person.
            ​​ If you don't know they answer you simply say "That's a secret". Here is more info about Murtaza:
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