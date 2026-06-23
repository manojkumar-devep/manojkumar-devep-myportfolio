import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
        except:
            return ""

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You said:", command)
        return command

    except sr.UnknownValueError:
        print("Could not understand.")
        return ""

    except sr.RequestError:
        print("Internet connection required.")
        return ""

speak("Voice assistant started")

while True:
    command = listen()

    if not command:
        continue

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "hello" in command:
        speak("Hello! How can I help you?")

    elif "exit" in command or "goodbye" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I don't know that command yet.")