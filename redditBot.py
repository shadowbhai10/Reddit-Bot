
try:
  import praw // First you have to install this library.
  subreddit_name = raw_input("Enter the subreddit name ")
  r = praw.Reddit('bot1')
  subreddit = r.subreddit(subreddit_name)
expect Exception as e:
  print(e)

for read in subreddit.hot(limit=5):   //You can choose .new() or .top() function also;
  print("Title: ",read.title)         //This will show title;
  print("Text: ",read.selftext)       //This will show the text; 
  print("Score: ",read.score)         //This will show current score or upvotes; 
  print("--------------------------------------------------------------------------------\n)
                                      //Since the output will be top 5 so we need a seperator;
        
        
