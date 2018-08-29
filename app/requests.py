from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news source base url

base_url = app.config['NEWS_API_BASE_URL']

# Getting source url
source_url = app.config['NEWS_SOURCE_URL']


def get_sources(country, category):
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
    get_sources_url = base_url.format(country, category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results


# We need to create a function that will process the results
# and create news source objects from the elements that we need.


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
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if url:
            source_object = Source(id,
                                   name,
                                   description,
                                   url,
                                   category,
                                   country)
            source_results.append(source_object)

    return source_results