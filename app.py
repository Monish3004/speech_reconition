import streamlit as st
import speech_recognition as sr

def listen_and_trigger(keyword):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening for activation keyword...")
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                if keyword in text.lower():
                    st.write(f"Activation keyword '{keyword}' detected.")
                    return True
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                st.error(f"Recognition request failed: {e}")
                return False

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            st.write("Audio captured. Recognizing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            st.error("No speech detected. Please speak something.")
        except sr.RequestError as e:
            st.error(f"Recognition request failed: {e}")
        except sr.UnknownValueError:
            st.error("Unable to recognize speech.")

st.title("Speech Recognition Streamlit App")

activation_keyword = st.text_input("Enter activation keyword:")

if st.button("Activate Speech Recognition"):
    if listen_and_trigger(activation_keyword):
        recognized_text = recognize_speech()
        if recognized_text:
            st.write(f"Recognized Text: {recognized_text}")
            
