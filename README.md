# Manhwa Analyzer

## Table of Contents
- [Manhwa Analyzer](#manhwa-analyzer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Installing Prerequisites](#installing-prerequisites)
    - [Installing Manhwa Analyzer](#installing-manhwa-analyzer)
  - [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Advanced Usage](#advanced-usage)
  - [Configuration](#configuration)
  - [Output](#output)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Manhwa Analyzer is a powerful command-line tool designed to scrape, process, and analyze data from the r/manhwa subreddit. It provides insights into popular manhwa titles, trends, and discussions within the Reddit community.

## Features

- Scrape recent posts from r/manhwa
- Extract manhwa titles from post titles
- Analyze frequency of mentioned titles
- Generate visualizations:
  - Word cloud of manhwa titles
  - Bar chart of most mentioned titles
  - Pie chart of top titles
  - Time series of post frequency
- Customizable data processing and analysis options

## Prerequisites

Before installing Manhwa Analyzer, ensure you have the following installed on your system:

- Python 3.11 or higher
- Git
- Poetry (Python package manager)

## Installation

### Installing Prerequisites

1. **Python 3.11+**:
   - Download and install from [python.org](https://www.python.org/downloads/)
   - Verify installation by running `python --version` in your terminal

2. **Git**:
   - Download and install from [git-scm.com](https://git-scm.com/downloads)
   - Verify installation by running `git --version` in your terminal

3. **Poetry**:
   - Install by following instructions at [python-poetry.org](https://python-poetry.org/docs/#installation)
   - Verify installation by running `poetry --version` in your terminal

### Installing Manhwa Analyzer

We provide an install script that automates the installation process. Follow these steps:

1. Download the install script:
   - For Unix-like systems (Linux, macOS):
     ```
     curl -O https://raw.githubusercontent.com/SpecialistSteak/manhwa-scraper-cli/main/install.sh
     chmod +x install.sh
     ```
   - For Windows:
     ```
     curl -O https://raw.githubusercontent.com/SpecialistSteak/manhwa-scraper-cli/main/install.bat
     ```

2. Run the install script:
   - For Unix-like systems:
     ```
     ./install.sh
     ```
   - For Windows:
     ```
     install.bat
     ```

3. The script will:
   - Check if required dependencies are already installed
   - Install the URS (Universal Reddit Scraper)
   - Clone the Manhwa Analyzer repository
   - Install dependencies using Poetry
   - Add Manhwa Analyzer to your system PATH

4. After installation, restart your terminal or run:
   - For Unix-like systems:
     ```
     source ~/.bashrc
     ```
   - For Windows: restart your command prompt

5. Set up your Reddit API credentials:
   - Open the `.env` file in your `/URS/` folder
   - Add your Reddit API credentials:
     ```
     CLIENT_ID=your_client_id
     CLIENT_SECRET=your_client_secret
     USER_AGENT=your_user_agent
     REDDIT_USERNAME=SpecialistSteak
     REDDIT_PASSWORD=your_password
     ```

## Usage

### Basic Usage

To run Manhwa Analyzer with default settings:

```
manhwa-analyzer
```

This will scrape the latest 500 posts from r/manhwa, process the data, and generate visualizations in the `output` directory.

### Advanced Usage

Customize the analysis with command-line options:

```
manhwa-analyzer -n 1000 -s manhwa -o ./custom_output --dpi 300 --bar_count 50 --fuzzy_threshold 85 --exclude source sauce --banlist input/custom_banlist.txt --regex "\[(.*?)\]" --time_filter week --sort hot
```

- `-n 1000`: Scrape 1000 posts
- `-s manhwa`: Specify the subreddit (default is 'manhwa')
- `-o ./custom_output`: Set custom output directory
- `--dpi 300`: Set image resolution to 300 DPI
- `--bar_count 50`: Show top 50 titles in bar chart
- `--fuzzy_threshold 85`: Set fuzzy matching threshold to 85%
- `--exclude source sauce`: Exclude posts with 'source' or 'sauce' in the title
- `--banlist input/custom_banlist.txt`: Use a custom word banlist file
- `--regex "\[(.*?)\]"`: Use custom regex for title extraction
- `--time_filter week`: Analyze posts from the past week
- `--sort hot`: Sort posts by 'hot' instead of 'new'

## Configuration

Create a custom word banlist by adding one word per line in `input/word_banlist.txt`:

```
source
sauce
recommendation
...
```

## Output

Manhwa Analyzer generates the following files in the output directory:

- `raw_data.json`: Raw scraped data
- `processed_data.json`: Processed manhwa title data
- `wordcloud.png`: Word cloud visualization of manhwa titles
- `barchart.png`: Bar chart of top manhwa titles
- `piechart.png`: Pie chart of top 10 manhwa titles
- `timeseries.png`: Time series graph of post frequency

## Troubleshooting

1. **Installation script fails**:
   - Ensure you have the necessary permissions to execute the script
   - Check that Python 3.11+, Git, and Poetry are correctly installed
   - Try running the installation steps manually if the script continues to fail

2. **"ModuleNotFoundError" when running the tool**:
   - Ensure you've activated the Poetry virtual environment with `poetry shell`
   - Try reinstalling dependencies with `poetry install`

3. **"Praw_HttpException" when scraping data**:
   - Check your `.env` file and ensure all Reddit API credentials are correct
   - Verify your internet connection

4. **No data in output files**:
   - Check if the subreddit exists and has recent posts
   - Try increasing the number of posts to scrape with the `-n` option

5. **Visualization files not generated**:
   - Ensure you have write permissions in the output directory
   - Check if you have enough disk space

For more issues, please open an issue on the GitHub repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.