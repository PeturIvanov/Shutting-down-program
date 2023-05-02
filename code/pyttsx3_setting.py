import pyttsx3

jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[1].id)
