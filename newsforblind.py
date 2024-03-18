#-------------------------------------------------------------------------------------#
# Author: Shama.T.S
# Project Name : Read news for blind person
# Version : 1.1
# Date : 15-03-2024
# To Do : install pyttsx3,newsapi : pip install pyttsx3 and  pip install newsapi-python
#-------------------------------------------------------------------------------------#

import pyttsx3  
from newsapi import NewsApiClient
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the News API client with your API key
newsapi = NewsApiClient(api_key='de835ef3b89f4c9e913c90732cec606d')

def read_news_headlines():
    # Get today's date
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # Fetch top headlines for today
    top_headlines = newsapi.get_top_headlines(language='en', country='in', page_size=5)

    # Read the headlines
    engine.say("Here are today's top news headlines:")
    engine.runAndWait()

    for article in top_headlines['articles']:
        title = article['title']
        engine.say(title)
        engine.runAndWait()

def main():
    read_news_headlines()


if __name__ == "__main__":
    main()