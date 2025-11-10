# import smtplib
#
# my_email = "tester.python.course@gmail.com"
# my_password = "delx esfk mnhn sdzu"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # To make our connection secure (TLS - Transport security layer)
#     connection.starttls()
#     connection.login(user=my_email,password=my_password)
#     connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject:Regarding the Python Course\n\nVery good! You are consistent and good at your end preparation:)")
#

import datetime as dt

now = dt.datetime.now()
print(now)
hour = now.hour
print(now.weekday())

dob = dt.datetime(year=2004,month=11,day=9)
print(dob)
