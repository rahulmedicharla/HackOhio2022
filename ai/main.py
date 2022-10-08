import speech_recognition as sr
import pyaudio
import time
#import webbrowser as wb

r1= sr.Recognizer()
r2 = sr.Recognizer()

mic1 = sr.Microphone()
mic2 = sr.Microphone()

def listen_indefinitely():
    while(True):

        with mic1 as source1:
            r1.adjust_for_ambient_noise(source1)
            cue = r1.listen(source1)

            try:
                command=r1.recognize_google(cue)
                if(command=="edit"):
                    print("Entering edit mode")
                    time.sleep(2)
                    while(True):
                        print("what do you want to code?")
                        with mic2 as source2:
                            r2.adjust_for_ambient_noise(source2)
                            audio_data = r2.listen(source2)

                            try:
                                audio = r2.recognize_google(audio_data)
                                if(audio=="exit"):
                                    print("Exiting edit mode")
                                    break
                                else:
                                    print(audio)

                            except sr.UnknownValueError:
                                continue
                            except sr.RequestError:
                                continue

          
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue

                


listen_indefinitely()

