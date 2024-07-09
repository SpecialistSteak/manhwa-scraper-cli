import argparse
import os
import json
from scraper import RedditScraper
from processor import DataProcessor
from analyzer import DataAnalyzer
from visualizer import DataVisualizer
from config import Config
from utils import load_word_banlist

def main():
    parser = argparse.ArgumentParser(description="Manhwa Analyzer CLI")
    parser.add_argument("-n", "--num_posts", type=int, default=500, help="Number of posts to scrape")
    parser.add_argument("-s", "--subreddit", type=str, default="manhwa", help="Subreddit to scrape")
    parser.add_argument("-o", "--output", type=str, default="output", help="Output directory")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for output images")
    parser.add_argument("--bar_count", type=int, default=25, help="Number of items in bar chart")
    parser.add_argument("--fuzzy_threshold", type=int, default=80, help="Fuzzy matching threshold")
    parser.add_argument("--exclude", nargs='+', default=[], help="Words to exclude from titles")
    parser.add_argument("--input", type=str, help="Input JSON file (if not scraping fresh)")
    parser.add_argument("--regex", type=str, default=r'\[(.*?)\]', help="Regex pattern for title extraction")
    parser.add_argument("--time_filter", type=str, choices=['all', 'day', 'hour', 'month', 'week', 'year'], default='all', help="Time filter for Reddit scraping")
    parser.add_argument("--sort", type=str, choices=['new', 'hot', 'top', 'rising'], default='new', help="Sorting method for Reddit scraping")
    parser.add_argument("--wordcloud_width", type=int, default=800, help="Width of wordcloud image")
    parser.add_argument("--wordcloud_height", type=int, default=400, help="Height of wordcloud image")
    parser.add_argument("--banlist", type=str, default="input/word_banlist.txt", help="Path to word banlist file")
    args = parser.parse_args()

    # Load word banlist
    word_banlist = load_word_banlist(args.banlist)

    config = Config(args, word_banlist)

    # Create output directory if it doesn't exist
    os.makedirs(config.output, exist_ok=True)

    if args.input:
        with open(args.input, 'r') as f:
            raw_data = json.load(f)
    else:
        # Scrape data
        scraper = RedditScraper(config)
        raw_data = scraper.scrape()

    # Save raw data
    with open(os.path.join(config.output, "raw_data.json"), "w") as f:
        json.dump(raw_data, f, indent=2)

    # Process data
    processor = DataProcessor(config)
    processed_data = processor.process(raw_data)

    # Save processed data
    with open(os.path.join(config.output, "processed_data.json"), "w") as f:
        json.dump(processed_data, f, indent=2)

    # Analyze data
    analyzer = DataAnalyzer(config)
    analysis_results = analyzer.analyze(processed_data)

    # Visualize data
    visualizer = DataVisualizer(config)
    visualizer.create_wordcloud(processed_data, os.path.join(config.output, "wordcloud.png"))
    visualizer.create_barchart(analysis_results[:config.bar_count], os.path.join(config.output, "barchart.png"))
    visualizer.create_pie_chart(analysis_results[:10], os.path.join(config.output, "piechart.png"))
    visualizer.create_time_series(raw_data, os.path.join(config.output, "timeseries.png"))

    print(f"Analysis complete. Results saved in {config.output} directory.")

if __name__ == "__main__":
    main()