import smtplib as smp
import pandas as pd
import datetime as dt

def send_mail(from_email, to_email, content):
    host = "smtp-mail.outlook.com"
    port = 587

    password = "" # Enter Your own Password

    smtp = smp.SMTP(host, port)

    status_code, response = smtp.ehlo()
    print("Echoing the Server")
    print(f"Status Code: {status_code}") 
    print(f"Response: {response}")

    status_code, response = smtp.starttls()
    print("\nStarting TLS Connection")
    print(f"Status Code: {status_code}")
    print(f"Response: {response}")

    status_code, response = smtp.login(from_email, password)
    print("\nLogging In")
    print(f"Status Code: {status_code}")
    print(f"Response: {response}")

    smtp.sendmail(from_email, to_email, content)
    smtp.quit()

def checkForBirthday():
    data = pd.read_csv("birthdays.csv")

    if not data.empty:
        year = dt.datetime.now().year  
        date = f"{dt.datetime.now().strftime('%m')}-{dt.datetime.now().strftime('%d')}"

        birthdays_today_email = data[data.date == date].email.to_list()
        birthdays_today_name = data[data.date == date].name.to_list()
        birthdays_today_year = data[data.date == date].year.to_list()

        for i in range(len(birthdays_today_email)):
            email_content = f"Subject: Happy Birthday {birthdays_today_name[i]}!\n\nDear {birthdays_today_name[i]},\n\nHappy {year - birthdays_today_year[i]} birthday! On this special day, I hope you are surrounded by love, laughter, and all the things that make you happiest. May your year ahead be filled with joy, success, and unforgettable moments. You deserve all the best today and always!\n\nBest Wishes,\n" # Your name

            from_email = "" # Enter your own email
            to_email = birthdays_today_email[i]

            send_mail(from_email, to_email, email_content)

    else:
        print("There are no birthdays in the birthdays.csv file")
    

checkForBirthday()    