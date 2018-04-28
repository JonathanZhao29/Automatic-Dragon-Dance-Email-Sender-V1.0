#automatic python email sender v0.3
import smtplib
import datetime
from email.mime.text import MIMEText
from time import strftime
#find current date
current = datetime.datetime.now()
#find what date Sunday is

#takes acct info from user and stores in vars
print("Enter your email")
gmail_user = input()
print("Enter your password")
gmail_password = input()
#sets sender to email entered above
sent_from = gmail_user
#creates an array for storing contacts
contacts =[]

#reads file of contacts
readFile = open("contacts.txt", "r")
if readFile.mode == 'r':
    contents = readFile.read().splitlines()
    contacts = contacts + contents

#creates an array for storing message
email_txt =[]
#read file of message
readMess = open("message.txt", "r")
if readMess.mode == 'r':
    messageTxt = readMess.read()
    dateFri = int(strftime("%d")) +2 #this finds Friday's date, then adds 2 to get to Sunday
    dateSun =strftime("%b") +" " + str(dateFri) #Sunday's date with month and day
    email_text = messageTxt.replace("{0}",dateSun)
	
#creates message with headers
msg = MIMEText("".join(email_text) )#<-- this is the email contents
msg['Subject'] = 'Automatic Python Email Sender V0.2'
msg['From'] = sent_from
msg['To'] = " ,".join(contacts) 

#sends email if it is Friday
dayOfWeek = strftime("%a")
if dayOfWeek =="Fri":
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from,contacts, msg.as_string())
        server.close()
        print ('Email sent!')
    except:
        print ('Something went wrong...')

else:
    print("Since its not friday, message won't send :(")
