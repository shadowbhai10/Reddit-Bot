try:
  import praw 	#install this library to create bots in reddit
  subreddit_name = str(input("Enter the subreddit name "))
  r = praw.Reddit('bot1')
  subreddit = r.subreddit(subreddit_name)
  for read in subreddit.hot(limit=5): #you can choose any function .new() or .top()
    print("Title: ",read.title)         #This will show title;
    print("Text: ",read.selftext)       #This will show the text; 
    print("Score: ",read.score)         #This will show current score or upvotes;
    print("--------------------------------------------------------------------------------\n")      

except Exception as e:
  print(e)

        
