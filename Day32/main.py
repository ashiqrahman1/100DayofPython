##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
from datetime import datetime
import random
import smtplib
# Read Data from CSV
data = pd.read_csv("birthdays.csv")
data_list = data.values.tolist()

# Get Current Date and Time
current = datetime.now()
c_day = current.day
c_month = current.month

search_text = "[NAME]"
person = {}
username = "test@gmail.com"
password = "fefrefrfgrfwgr"

# gettining information for csv
for info in data_list:
    if c_day in info and c_month in info:
        person['name'] = info[0]
        person['email'] = info[1]
        person['day'] = info[3]
        person['month'] = info[4]

print(person)

if person is not None:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        data = letter.read()
        message_letter = data.replace(search_text, person['name'])

    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        try:
            con.login(user=username, password=password)
        except smtplib.SMTPAuthenticationError:
            print("Check your Username/Password")
        except smtplib.SMTPNotSupportedError:
            print("SMTP AUTH extension not supported by server")
        else:
            con.sendmail(to_addrs=person['email'],
                         from_addr=username, msg=message_letter)
