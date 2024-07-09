from collections import Counter

class DataAnalyzer:
    def __init__(self, config):
        self.config = config

    def analyze(self, data):
        title_counts = Counter({item['bracketed_title']: item['count'] for item in data})
        return title_counts.most_common()