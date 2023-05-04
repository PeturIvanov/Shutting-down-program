from pyttsx3_setting import *
import os
import time
import datetime
import threading

remaining_time = 0
adding_time_seconds = 0


def speak(hours_to_say, minutes_to_say):
    if hours_to_say != 0:
        if hours_to_say == 1:
            if minutes_to_say == 1:
                jarvis.say(f"Shutdown after {hours_to_say} hour and {minutes_to_say} minute.")
            elif minutes_to_say > 1:
                jarvis.say(f"Shutdown after {hours_to_say} hour and {minutes_to_say} minutes.")
            else:
                jarvis.say(f"Shutdown after {hours_to_say} hour.")
        elif hours_to_say > 1:
            if minutes_to_say == 1:
                jarvis.say(f"Shutdown after {hours_to_say} hours and {minutes_to_say} minute.")
            elif minutes_to_say > 1:
                jarvis.say(f"Shutdown after {hours_to_say} hours and {minutes_to_say} minutes.")
            else:
                jarvis.say(f"Shutdown after {hours_to_say} hours.")

    else:
        if minutes_to_say == 1:
            jarvis.say(f"Shutdown after {minutes_to_say} minute")
        elif minutes_to_say > 1:
            jarvis.say(f"Shutdown after {minutes_to_say} minutes")
    jarvis.runAndWait()


def shutdown_timer(hours, minutes):
    seconds = hours * 3600 + minutes * 60
    global remaining_time
    global adding_time_seconds
    while seconds > 0:
        timer = datetime.timedelta(seconds=seconds)
        remaining_time = timer
        if adding_time_seconds != 0:
            seconds += adding_time_seconds
            adding_time_seconds = 0
        time.sleep(1)
        seconds -= 1
    os.system("shutdown /s /t 1")


def menu():
    global remaining_time
    global adding_time_seconds
    while True:
        print("For time remaining enter (t). For adding time enter(a)."
              " For stop timer enter(s). For pause the time enter(p)")
        user_input = input()
        if user_input == "t":
            print(f"Time remaining - {remaining_time}")
        elif user_input == "a":
            hours_to_add = int(input("Enter your hours to add:"))
            minutes_to_add = int(input("Enter your minutes to add:"))
            adding_time_seconds += (hours_to_add * 3600 + minutes_to_add * 60)


remaining_hours = int(input("Enter countdown hours:"))
remaining_minutes = int(input("Enter countdown minutes:"))
speak(remaining_hours, remaining_minutes)

# tread for shutdown_timer.
shutdown_timer_tread = threading.Thread(target=shutdown_timer, args=(remaining_hours, remaining_minutes))
shutdown_timer_tread.start()


# tread for menu.
menu_thread = threading.Thread(target=menu)
menu_thread.start()

shutdown_timer_tread.join()
menu_thread.join()


