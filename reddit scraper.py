import praw
import pandas as pd
from praw.models import MoreComments

reddit = praw.Reddit(client_id="4NE4coGocgiygH-SXeDYnA",client_secret="alOzqaczvU-8L7Kt4YY_RQ2Em9yFrA",user_agent="Bruh-plot_twist")

url = input("enter the url of the post: ")
submission = reddit.submission(url=url)

top = {"Comments": []}
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments): # ignores more comments
        continue
    top["Comments"].append(top_level_comment)
    
top_comments = pd.DataFrame(top)
top_comments
