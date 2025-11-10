import smtplib
import datetime as dt
import random

MY_EMAIL = "tester.python.course@gmail.com"
MY_PASSWORD = "xyra oyas awkc hncf"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Today's Motivational Quote!\n\n{random_quote}")

