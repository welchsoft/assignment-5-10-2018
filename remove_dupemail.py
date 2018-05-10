import json
import random

#generates random emails by generating ranom numbers, casting to string and concatinating @random.com, spits out a huge string of emails
def generate_randommail():
    randommails = ''
    for index in range(100):
        randommails += (str(random.randint(1,10))+"@random.com, ")
    return randommails

#function to remove duplicates from the text file of randomly generated emails
def random_dupemail_removal(randommails):
    with open('randommail.txt','w') as file:
        file.write(randommails)

    with open('randommail.txt') as file:
        emails = file.read()

    splitmail = str(emails).split(", ")

    non_dupe_email = []

    for email in splitmail:
        if email not in non_dupe_email:
            non_dupe_email.append(email)

    non_dupe_string = ''
    for email in non_dupe_email:
        non_dupe_string += email+", "

    with open('duplicate-free-random-email-list.txt','w') as file:
        file.write(non_dupe_string)

#function to remove duplicates from the text file of provided emails
def dupemail_removal():
    with open('emails.txt') as file:
        emails = file.read()

    splitmail = str(emails).split(", ")

    non_dupe_email = []

    for email in splitmail:
        if email not in non_dupe_email:
            non_dupe_email.append(email)

    non_dupe_string = ''
    for email in non_dupe_email:
        non_dupe_string += email+", "

    with open('duplicate-free-email-list.txt','w') as file:
        file.write(non_dupe_string)

#function calls to run the stuff
randommails = generate_randommail()
random_dupemail_removal(randommails)
dupemail_removal()
