class Config:
    def __init__(self, args, word_banlist):
        self.num_posts = args.num_posts
        self.subreddit = args.subreddit
        self.output = args.output
        self.dpi = args.dpi
        self.bar_count = args.bar_count
        self.fuzzy_threshold = args.fuzzy_threshold
        self.exclude = args.exclude + word_banlist  # Combine CLI excludes and word banlist
        self.regex = args.regex
        self.time_filter = args.time_filter
        self.sort = args.sort
        self.wordcloud_width = args.wordcloud_width
        self.wordcloud_height = args.wordcloud_height
        self.banlist_file = args.banlist