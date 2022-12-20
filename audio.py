import speech_recognition as sr
import os
from gtts import gTTS

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    mytext = r.recognize_google(audio)

    #myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj = gTTS(text=mytext, lang='af')
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")    
