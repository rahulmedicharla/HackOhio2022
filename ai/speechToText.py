import numbers
import speech_recognition as sr
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyaudio
import time
#import webbrowser as wb

r1= sr.Recognizer()
r2 = sr.Recognizer()


HOT_WORDS = ("while", "for", "variable", "if", "close", "else", "call", "import", "from")

DECLARATIVE_WORDS = {"create a variable":"variable","declare":"variable","initialize":"variable","make":"variable", "while":"while"}

OPERATIONS = {"plus":"+","minus":"-","times":"*","divided by":"/","mod":"%","to the power of":"**","squared":"** 2" , "cubed":"** 3","less than or equal to":"<=","less than":"<",
    "greater than or equal to":">=","greater than":">","equivalent":"==","as":"=","equals":"=","equal":"=","not equal to":"!=","negation of":"!=", "true":"True", "false":"False",
    "quit":"exit","leave":"end","stop editing":"exit","quit editing":"exit","quit edit":"exit","start edit":"edit", "prince":"print","sprint":"print","loop":"for", "underscore":"_"}

NUMBERS = {
    'one': '1','two': '2','to':'2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0'}


mic1 = sr.Microphone()
mic2 = sr.Microphone()  

def get_single_phrase():

    with mic1 as source:
        print("Say Something: \n")
        r1.adjust_for_ambient_noise(source, duration=1)
        audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio).lower()

        firstWordInPhrase = ""
        #find the first word
        if (text.find(" ") > -1):
            firstWordInPhrase = text[0: text.find(" ")]
        
        # replace declarative words
        for dec in DECLARATIVE_WORDS.keys():
            if(dec in text):
                text=text.replace(dec,DECLARATIVE_WORDS[dec])
                break

        # replace operations 
        for op in OPERATIONS:
            if(op in text):
                text=text.replace(op,OPERATIONS[op])

        # replace numeric words
        for num in NUMBERS:
            if(num in text):
                text=text.replace(num,NUMBERS[num])

        if("with parameters " in text): text=text.replace("with parameters ", "")
        if("with parameter " in text): text=text.replace("with parameter ", "")
                
        if (firstWordInPhrase in HOT_WORDS or firstWordInPhrase in DECLARATIVE_WORDS):
            db.reference("/input").set(text)

    except sr.UnknownValueError:
        text = "Didn't Understand, try again \n"
    except sr.RequestError:
        text = "Problem with Google Speech Recognition \n"
    except sr.WaitTimeoutError:
        text = "Speak quicker \n"

    return text

def run():
    cred= credentials.Certificate("./firebaseConfig.json")
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'https://hackohio2022-1ccea-default-rtdb.firebaseio.com/'
    })
    while (True):
        with mic2 as source: 
            r2.adjust_for_ambient_noise(source, duration=1)

            audio = r2.listen(source)
        try:
            cue = r2.recognize_google(audio).lower()
        except sr.UnknownValueError:
            cue = "Didn't Understand, try again \n"
        except sr.RequestError:
            cue = "Problem with Google Speech Recognition \n"
        except sr.WaitTimeoutError:
            cue = "Speak quicker \n"

        if (cue == "edit"):
            print("Entering edit mode. \n")
            while (True):
                phrase = (get_single_phrase())

                if (phrase == "exit"):
                    print("Exiting edit mode. \n")
                    break
                else:
                    print(phrase + "\n")
        elif(cue == "run"):
            db.reference("/shouldRun").set(1)
            
run()
