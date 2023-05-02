from pyttsx3_setting import *
import os
import time
import datetime


def shutdown_timer(mins):
    seconds = mins * 60
    jarvis.say(f"Shutdown after {mins} minutes!")
    jarvis.runAndWait()
    while seconds > 0:
        timer = datetime.timedelta(seconds=seconds)
        print(f"\r{timer}", end="")
        time.sleep(1)
        seconds -= 1
    os.system("shutdown /s /t 1")


# def stop_timer():


minutes = int(input("Enter your timer:"))
shutdown_timer(minutes)

