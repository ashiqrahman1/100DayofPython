import smtplib
from datetime import datetime
import random
# sender = "test@gmail.co,"
# password = "12345678"
# reciver = "test2@gmail.com"
# message = "this is a test message"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# try:
#     connection.login(user=sender, password=password)
# except smtplib.SMTPAuthenticationError:
#     print("Auth Error")
# else:
#     connection.sendmail(from_addr=sender, to_addrs=reciver, msg=message)
# connection.quit()
# from datetime import datetime

# print(datetime.now().weekday())
# with open("quotes.txt") as quote:
#     data = random.choice(quote.readlines())
#     # print(data)

# if datetime.now().weekday == 1:
#     print(random.choice(data))
# else:
#     print("It's works only in monday")
sender = "test@gmail.com"
password = "testpass123"
reciver = "test1@gmail.com"
if datetime.now().weekday() == 0:
    with open("quotes.txt") as quote:
        data = random.choice(quote.readlines())
        # print(data)

    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        try:
            connection.login(user=sender, password=password)
        except smtplib.SMTPAuthenticationError:
            print("Please Check the Username/Password")
        except smtplib.SMTPNotSupportedError:
            print("SMTP AUTH extension not supported by server")
        else:
            connection.send_message(
                from_addr=sender, to_addrs=reciver, msg=data)
else:
    print("This Script Only Works in Monday")
