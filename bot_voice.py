import pyttsx3
import speech_recognition as sr
def voice():
    speech=sr.Recognizer()
    with sr.Microphone() as source2:
        print("Try to be in a silent environment....")
        speech.adjust_for_ambient_noise(source2,duration=4)
        print("Speak now....")
        audio2= speech.listen(source2)
        
        try:
            text = speech.recognize_google(audio2)
            text = text.lower()
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio. Please try again.")
            return None 
        except sr.RequestError:
            print(f"Could not request results from Google Speech Recognition service")
            return None

    

 