# This script deploys a single bot

from bots import ChatBot, MemoryBot

import speech_recognition as sr
import sys, requests


def handle_speech_input(request):
    # Extract the audio data from the request
    audio_data = request.data

    # Use the SpeechRecognition library to convert the audio data to text
    r = sr.Recognizer()
    audio = sr.AudioData(data=audio_data, sample_rate=44100, 
                         sample_width=2)
    text = r.recognize_google(audio)
    print(text)


if __name__ == "__main__":
    port = 9000
    bot = ChatBot(p=port)

    app = falcon.App()
    app.add_route('/listen', bot)
    httpd = simple_server.make_server('0.0.0.0',port,app)
    httpd.serve_forever() 
