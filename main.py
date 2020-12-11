from win10toast import ToastNotifier
import time
title = str(input("Title of notification: "))
message = str(input("Message of notification: "))
time = int(input("Amont of alert: "))
duration = int(input("Duration of alert: "))

hr = ToastNotifier()
for x in range(time):
    hr.show_toast(f"{title}",f"{message}",duration=duration)