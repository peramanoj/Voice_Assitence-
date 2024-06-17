import speech_recognition as sr
import pyttsx3
import wolframalpha
from datetime import datetime

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Wolfram Alpha API client
WOLFRAM_API_KEY = 'THVWJR-KPGAJ6EJVY'
wolfram_client = wolframalpha.Client(WOLFRAM_API_KEY)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: ", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def wolfram_search(query):
    try:
        res = wolfram_client.query(query)
        answer = next(res.results).text
        return answer
    except StopIteration:
        print("No results found for the query.")
        return "I couldn't find any relevant results."
    except Exception as e:
        print(f"Error using Wolfram Alpha API: {e}")
        return f"Error using Wolfram Alpha API: {e}"

def process_command(command):
    global waiting_for_question
    print(f"Processing command: {command}")
    if command:
        if "question" in command:
            speak("Yes, ask me.")
            waiting_for_question = True
        elif waiting_for_question:
            waiting_for_question = False
            answer = wolfram_search(command)
            speak(answer)
        else:
            speak("I'm sorry, I didn't understand that command.")
    return True

def main():
    global waiting_for_question
    waiting_for_question = False
    greeting = get_greeting()
    speak(f"Hi Manoj, {greeting}")
    running = True
    while running:
        command = listen()
        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()
