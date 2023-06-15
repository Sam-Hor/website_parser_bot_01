

============================================
# Project Name: WebSite Parser Telegram Bot

## Purpose

This project was created to scrape data from websites and deliver the results via a Telegram bot. It can be particularly useful for individuals and organizations that want to monitor websites for updates and receive those updates in a convenient and timely manner via Telegram.

## Functionality

The Web Scraper Telegram Bot provides the following features:

1. **Web Scraping:** The ability to extract data from the websites.
2. **Data Processing:** The bot processes the scraped data and converts it into a user-friendly format.
3. **Telegram Integration:** All processed data is sent to a specified Telegram bot using the `aiogram` library. The bot can deliver updates immediately or on a schedule, depending on the user's preference.
4. **Customization:** Users can specify which websites to monitor and customize the scraping parameters to suit their needs.

## Installation

Here are the steps to install this bot:

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/webscraper-telegram-bot.git
    ```
2. Navigate to the cloned repository:
    ```
    cd webscraper-telegram-bot
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
    or use 
    python3 -m venv env
    source env/bin/activate
    pip install requests bs4 lxml
    pip install pandas
## Usage

To use this bot, follow these steps:

1. Open `config.py` and input your Telegram bot token and the URLs of the websites you wish to monitor.
2. Run the bot by executing the following command in your terminal:
    ```
    python bot.py
    ```
3. Go to your Telegram bot and start receiving updates.

Remember, the bot is highly customizable. Feel free to modify the scraping rules or the data processing functions to better suit your needs.

Please note: This bot is intended to respect the rules and policies of any websites it interacts with. Please ensure that your use of the bot adheres to these rules and to any relevant data protection and privacy laws.

## Contribution

Contributions, issues, and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

============================================
Additional files that just make sense (that's my learning process)

main_00.py - notes. main metods and combinations

main_10.py - python parser + telegram bot aiogram