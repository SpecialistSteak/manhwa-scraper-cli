import praw
import os
from dotenv import load_dotenv

class RedditScraper:
    def __init__(self, config):
        load_dotenv()
        self.reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            user_agent=os.getenv("USER_AGENT"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
        )
        self.config = config

    def scrape(self):
        subreddit = self.reddit.subreddit(self.config.subreddit)
        if self.config.sort == 'new':
            posts = subreddit.new(limit=self.config.num_posts)
        elif self.config.sort == 'hot':
            posts = subreddit.hot(limit=self.config.num_posts)
        elif self.config.sort == 'top':
            posts = subreddit.top(time_filter=self.config.time_filter, limit=self.config.num_posts)
        elif self.config.sort == 'rising':
            posts = subreddit.rising(limit=self.config.num_posts)

        data = []
        for post in posts:
            data.append({
                "author": str(post.author),
                "created_utc": post.created_utc,
                "distinguished": post.distinguished,
                "edited": post.edited,
                "id": post.id,
                "is_original_content": post.is_original_content,
                "is_self": post.is_self,
                "link_flair_text": post.link_flair_text,
                "locked": post.locked,
                "name": post.name,
                "nsfw": post.over_18,
                "num_comments": post.num_comments,
                "permalink": post.permalink,
                "score": post.score,
                "selftext": post.selftext,
                "spoiler": post.spoiler,
                "stickied": post.stickied,
                "title": post.title,
                "upvote_ratio": post.upvote_ratio,
                "url": post.url
            })
        return {"scrape_settings": {"subreddit": subreddit.display_name, "category": self.config.sort, "n_results_or_keywords": str(self.config.num_posts), "time_filter": self.config.time_filter}, "data": data}