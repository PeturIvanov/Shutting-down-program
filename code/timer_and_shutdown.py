from pyttsx3_setting import *
import os
import time
import datetime



def speak(hours_to_say, minutes_to_say):
    if hours_to_say != 0:
        if hours_to_say == 1:
            jarvis.say(f"Shutdown after {hours_to_say} hour and {minutes_to_say} minutes")
        else:
            jarvis.say(f"Shutdown after {hours_to_say} hours and {minutes_to_say} minutes")
    else:
        jarvis.say(f"Shutdown after {minutes_to_say} minutes!")
    jarvis.runAndWait()


def shutdown_timer(minutes, hours):
    seconds = hours * 3600 + minutes * 60
    speak(hours, minutes)
    while seconds > 0:
        timer = datetime.timedelta(seconds=seconds)
        print(f"\rTime remaining - {timer}", end="")
        time.sleep(1)
        seconds -= 1
    os.system("shutdown /s /t 1")


hours = int(input("Enter countdown hours:"))
minutes = int(input("Enter countdown minutes:"))
shutdown_timer(minutes, hours)

