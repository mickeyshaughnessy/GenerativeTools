import speech_recognition as sr
import requests

def handle_speech_input(request):
    # Extract the audio data from the request
    audio_data = request.data

    # Use the SpeechRecognition library to convert the audio data to text
    r = sr.Recognizer()
    audio = sr.AudioData(data=audio_data, sample_rate=44100, 
                         sample_width=2)
    text = r.recognize_google(audio)


if __name__ == "__main__":
    port = int(sys.argv[1])
    paced = int(sys.argv[2])
    bidder = Bidder(p=port, budget=1000, price_paced=paced)

    app = falcon.App()
    app.add_route('/bid', bidder)
    app.add_route('/win', bidder)
    app.add_route('/conv', bidder)
    httpd = simple_server.make_server('0.0.0.0', int(sys.argv[1]), app)
    httpd.serve_forever() 
