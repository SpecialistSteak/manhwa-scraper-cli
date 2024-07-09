from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

class DataVisualizer:
    def __init__(self, config):
        self.config = config

    def create_wordcloud(self, data, output_path):
        word_freq = Counter({item['bracketed_title']: item['count'] for item in data})
        wordcloud = WordCloud(width=self.config.wordcloud_width, height=self.config.wordcloud_height, background_color='white').generate_from_frequencies(word_freq)
        plt.figure(figsize=(self.config.wordcloud_width/100, self.config.wordcloud_height/100), dpi=self.config.dpi)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Manhwa Title Word Cloud')
        plt.tight_layout(pad=0)
        plt.savefig(output_path, dpi=self.config.dpi)
        plt.close()

    def create_barchart(self, data, output_path):
        titles, counts = zip(*data)
        plt.figure(figsize=(20, 14), dpi=self.config.dpi)
        bars = plt.bar(range(len(titles)), counts)
        plt.xticks(range(len(titles)), titles, rotation=45, ha='right', fontsize=10)
        plt.xlabel('Titles', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.title(f'Top {len(titles)} Most Common Manhwa Titles', fontsize=16)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height}',
                     ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.config.dpi)
        plt.close()

    def create_pie_chart(self, data, output_path):
        titles, counts = zip(*data)
        plt.figure(figsize=(12, 8), dpi=self.config.dpi)
        plt.pie(counts, labels=titles, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Top 10 Manhwa Titles Distribution', fontsize=16)
        plt.tight_layout()
        plt.savefig(output_path, dpi=self.config.dpi)
        plt.close()

    def create_time_series(self, data, output_path):
        df = pd.DataFrame(data['data'])
        df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
        df.set_index('created_utc', inplace=True)
        df.sort_index(inplace=True)
        
        plt.figure(figsize=(15, 8), dpi=self.config.dpi)
        df['cumulative_posts'] = range(1, len(df) + 1)
        df['cumulative_posts'].plot()
        plt.title('Cumulative Posts Over Time', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Number of Posts', fontsize=12)
        plt.tight_layout()
        plt.savefig(output_path, dpi=self.config.dpi)
        plt.close()