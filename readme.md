# Daily-Puzzle
A simple python script to run every 24hrs to send a mail containing a puzzle to recipients.
I have deployed the code on heroku using heroku CLI.


**Folder Structure:**
- run.py: This file contains the code that does web scraping and sending mail.
- data.txt: This file stores the number of the next puzzle to send.

**To deploy using heroku CLI : **
- Go to directory ( If not initialized as a git repo : git init --> git add . --> git commit -m "commit message" )
- Login to heroku Account
```
heroko login -i
```
- Connect to heroku
```
heroku git:remote -a app_name
```
-push to heroku 
```
git push heroku master
```
------------------------------------------------Once Deployed the script will run on its own---------------------------------------------
