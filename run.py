import smtplib, ssl
import bs4,webbrowser
import requests
import time

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
    sender_email = "sender-mail-id"               #sender's mail id
    receiver_email  = ['reciever-mail-id']        #list of reciever's mail ids
    #password = getpass.getpass(prompt="Type your password and press enter: ")
    password = "enter-your-password-here"

    print('Runnning\n')
    file1 = open("data.txt","r")  
    number = file1.read() 
    file1.close() 


    subject="Daily Puzzle {}".format(int(number))
    puzzle_link=getLink(number)
    text = 'Good morning! Here\'s your puzzle for today.\n '+puzzle_link[0]
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
        file1 = open("data.txt","w")  
        number = file1.write(str(int(number)+1)) 
        file1.close() 
    
    except Exception as e:
        print(e)

if __name__=="__main__":
    sendMail()
