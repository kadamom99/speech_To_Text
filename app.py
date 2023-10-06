import speech_recognition as sr
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Record audio from the microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    try:
        # Perform speech recognition
        recognized_text = r.recognize_google(audio)
        print("You said: " + recognized_text)

        return recognized_text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

if __name__ == '__main__':
    app.run(debug=True)

