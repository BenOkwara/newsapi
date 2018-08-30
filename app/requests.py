from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news source base url
base_url = app.config['SEARCH_API_BASE_URL']

# Getting TOP HEADLINES url - the most popular headlines of the day
headlines_url = app.config['HEADLINES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    This takes in a news category as an argument.
    We use the .format() method below on the base_url
    and pass in the news source category and the api_key.
    this will replace the {} curly brace placeholders in
    the base_url with the category and api_key respectively.
    This creates get_sources_url as the final URL for our API request.
    We then use with as our context manager to send a
     request using theurllib.request.urlopen() function
      that takes in the get_sources_url as an argument and
       sends a request as url
      We use the read() function to read the response and store
       it in a get_sources_data variable.
      We then convert the JSON response to a Python dictionary
      using json.loads function and pass in the get_sources_data variable.
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the
    news source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that
         contain news source details
    Returns :
        source_results: A list of news source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        print(id)
        name = source_item.get('name')
        print(name)
        description = source_item.get('description')
        print(description)
        url = source_item.get('url')
        print(url)
        category = source_item.get('category')
        print(category)
        country = source_item.get('country')
        print(country)

        if url:
            source_object = Source(id,
                                   name,
                                   description,
                                   url,
                                   category,
                                   country)
            source_results.append(source_object)

    return source_results


def get_articles(id):
    '''
    function to get json response from url
    '''

    get_articles_details_url = article_base_url.format(id, api_key)
    print(get_articles_details_url)
    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results = None

        if articles_details_response['articles']:
            article_results_list = articles_details_response['articles']
            articles_results = process_articles(article_results_list)

    return articles_results

def process_articles(articles_list):
    article_results = []
    for item in articles_list:
        print(item)
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        publish_time = item.get('publishedAt')

        articles_object = Article(author, title, description, url, image_url, publish_time)
        article_results.append(articles_object)

    return article_results
