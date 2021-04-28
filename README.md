# Reddit-Bot
This bot only reads the top 5 hot content from the subreddit

Step 1 -  Here i am using reddit API http://www.reddit.com/dev/api
          step 1 is to create an app from https://www.reddit.com/prefs/apps/
          and remember the client_id and client_secret 
          
Step 2 -  Now you have to install the praw library in python using pip command .Why? cuz praw library   
          is use to make bots in reddit.
          $pip install praw
          
Step 3 -  Update the praw.ini file in Lib\Site-Packages\praw\praw.ini
          add these values to create a bot
          
          ////Inside the praw.ini
          short_url=https://redd.it
          [bot1] 
          client_id =             //Enter client_id here
          client_secret=          //Enter client_secret key here
          
          //Leave these values blank if you want read only access.
          
          password=               //Enter your reddit password here 
          username=               //Enter your reddit username here 
          user_agent=PyEng Bot 0.1      //This is our bot name you can choose any name.
          
Now you all set.Run the file redditBot.py and see the result.
