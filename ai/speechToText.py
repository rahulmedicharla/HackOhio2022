import speech_recognition as sr
import pyaudio
import time
#import webbrowser as wb

r1= sr.Recognizer()
r2 = sr.Recognizer()

HOT_WORDS = ("while", "for", "variable", "if", "end", "else")

mic1 = sr.Microphone()
mic2 = sr.Microphone()  

def get_single_phrase():

    with mic1 as source:
        print("Say Something: ")
        r1.adjust_for_ambient_noise(source, duration=1)
        audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio).lower()
        first_space= text.index(" ")
        first_word= text[:first_space]
        if(first_word in HOT_WORDS):
            # pass to jack
            print(text + " is a \"valid\" statement")
    except sr.UnknownValueError:
        text = "Didn't Understand, try again"
    except sr.RequestError:
        text = "Problem with Google Speech Recognition"
    except sr.WaitTimeoutError:
        text = "Speak quicker"

    return text

def run():
    while (True):
        with mic2 as source: 
            r2.adjust_for_ambient_noise(source, duration=1)
            audio = r2.listen(source)
        try:
            cue = r2.recognize_google(audio).lower()
        except sr.UnknownValueError:
            cue = "Didn't Understand, try again"
        except sr.RequestError:
            cue = "Problem with Google Speech Recognition"
        except sr.WaitTimeoutError:
            cue = "Speak quicker"

        if (cue == "edit"):
            print("Entering edit mode.")
            while (True):
                phrase = (get_single_phrase())

                if (phrase == "exit"):
                    print("Exiting edit mode.")
                    break
                else:
                    print(phrase)
            
run()


#listen_indefinitely()
