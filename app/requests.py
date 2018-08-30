from app import app
import urllib.request,json
from .models import source,articles

Source = source.Source
Article= articles.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news source base url
base_url = app.config['SEARCH_API_BASE_URL']

# Getting TOP HEADLINES url - the most popular headlines of the day
headlines_url = app.config['HEADLINES_API_BASE_URL']

# Getting the news articles url
articles_url = app.config['NEWS_ARTICLE_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    This takes in a news category as an argument.
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


def get_articles():
    '''
    function to get json response from url
    '''

    get_articles_details_url = articles_url.format('abc-news', api_key)
    print(get_articles_details_url)
    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results = None

        if articles_details_response['articles']:
            article_results_list = articles_details_response['articles']

            articles_results = process_articles(article_results_list)

            # print(articles_results)

    return articles_results

def process_articles(articles_list):
    article_results = []
    for item in articles_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')


        if url:

            articles_object = Article (id,
                                  author,
                                  title,
                                  description,
                                  url,
                                  urlToImage,
                                  publishedAt)
            article_results.append(articles_object)

    return article_results