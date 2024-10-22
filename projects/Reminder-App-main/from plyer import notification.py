from plyer import notification
from threading import Timer
import time


def reminder():
    notification.notify(title="Reminder", message=message, timeout=10)


while True:
    message = input("Enter your message: ")
    days = int(input("\nEnter the number of days: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    total_time = (days * 86400) + (hours * 3600) + minutes * 60 + seconds

    timer = Timer(total_time, reminder)
    timer.start()

    if input("\nDo you want to add more reminders? If so please enter 'yes': ").casefold() == "yes":
        continue

    time.sleep(total_time)
    break