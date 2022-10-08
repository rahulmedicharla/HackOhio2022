import speech_recognition as sr
import pyaudio
#import webbrowser as wb

r = sr.Recognizer()

toggle_mic = False

#gets the speech over a given time interval in seconds (dur)
def get_speech_over_duration(dur):

    with sr.Microphone() as source:
        audio_data = r.record(source, duration=dur)
        print("Listening...")
        audio = r.recognize_google(audio_data)
        #print(audio)

    return audio

print(get_speech_over_duration(10))

