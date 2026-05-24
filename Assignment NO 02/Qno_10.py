"""
10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
"""

from datetime import datetime

now=datetime.now()

date=now.strftime("%d-%m-%y")

time = now.strftime("%I:%M %p")
print("Date:",date)
print("Time:",time)