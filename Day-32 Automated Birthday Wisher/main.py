import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "bhavyapandurangan494@gmail.com"
MY_PASSWORD = "kxwo sybm flie mwfx"
datas = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day
datas_list = datas.values.tolist()
print(datas_list)
for i in range(len(datas_list)):
    if datas_list[i][3] == month and datas_list[i][4] == day:
        random_letter = random.randint(1,3)
        with open(f"letter_templates/letter_{random_letter}.txt","r") as letter_file:
            letter = letter_file.read()
        letter_changed = letter.replace("[NAME]",datas_list[i][0])
        print(letter_changed)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=datas_list[i][1],msg=f"Subject:MY HEARTY WISHES {datas_list[i][0]}!\n\n{letter_changed}")
