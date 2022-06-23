import smtplib, ssl
import bs4,webbrowser
import requests
import time
import csv
import random
from datetime import date


def getGift(day,month,year):
    with open('Calendar-test.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        dateHasGift = False
        randomUnused = []
        i=0
        for row in reader:
            if row[0] == str(month) + "/" + str(day):
                dateHasGift = True            
                return row
            if row[0]=='':
                randomUnused.append(row)
                i+=1
        if not dateHasGift:
            #pick a random gift  
            giftToPick = random.randint(0, i-1)
            return randomUnused[giftToPick]
            #write to date the date that it was used

def getNumberOfLemons(day,month,year):
    if month > 5:
        twelveLemons = year - 2021
        monthModMay = month
    else:
        twelveLemons = year - 2021 - 1
        monthModMay = month +12

    if day < 26:
        monthModMay-=1
    
    howManyLemons = twelveLemons*12 + monthModMay - 5
    return howManyLemons


def getLink(number):
    link='https://www.google.com/search?q='+'geeksforgeeks puzzle '+number
    response=requests.get(link)
    
    ls=[]
    links=[]
    try:
        soup=bs4.BeautifulSoup(response.text,features="html.parser")
        
        for tag in soup.find_all('a'):
            ls.append(tag.get('href'))
        
        for link in ls:
            if(link.startswith('/url?q=https://www.geeksforgeeks.org/puzzle-'+number)==True):
                end=0
                index=37
                for c in link[37:]:
                    if c=='/':
                        end=index
                        break
                    index+=1
                links.append(link[7:end])
                break
        return links
    
    except:
        print('Error')
        return ['No Links Found!!']
        raise()

def sendMail():
    smtp_server = "smtp.gmail.com"
    port = 587                                    # For starttls
    sender_email = "tpalendar"               #sender's mail id
    receiver_email  = ['aubreyannthompson']        #list of reciever's mail ids
    #password = getpass.getpass(prompt="Type your password and press enter: ")
    password = "QtXWj7QYn5y8zb"

    print('Runnning\n')
    #file1 = open("data.txt","r")  
    #number = file1.read() 
    #file1.close() 


    today = date.today()
    day = today.day
    month = today.month
    year = today.year

    howManyLemons = getNumberOfLemons(day,month,year)
    gift = getGift(day,month,year)

    subject="Lemon Calendar {}".format(int(number))
    #puzzle_link=getLink(number)
    text = "🍋"*getNumberOfLemons(day,month,year)
    text = '\nGood morning! "Today\'s gift is a', gift[1],':', gift[2]
    if day == 26:
        text = text + "\nIt's a lemon day! Happy ", howManyLemons, " lemons!"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()                               # Can be omitted
        server.starttls(context=context)            # Secure the connection
        server.ehlo()                               
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
      #  file1 = open("data.txt","w")  
       # number = file1.write(str(int(number)+1)) 
        #file1.close() 
    
    except Exception as e:
        print(e)

if __name__=="__main__":
    sendMail()
