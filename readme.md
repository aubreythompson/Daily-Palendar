# Daily-Puzzle
A simple python script to run every 24hrs to send a mail containing a puzzle to recipients.
I have deployed the code on Heroku using Heroku CLI.


**Folder Structure:**
- run.py: This file contains the code that does web scraping and sending mail.
- data.txt: This file stores the number of the next puzzle to send.

**Steps to deploy using Heroku CLI**
- Go to the directory containing the files ( If not initialized as a git repo : git init --> git add . --> git commit -m "commit message" )
- Login to your Heroku Account
```
heroko login -i
```
- Connect to the App
```
heroku git:remote -a app_name
```
-Push to Heroku 
```
git push heroku master
```
------------------------------------------------Once Deployed the Script will run on its own-------------------------------------------
