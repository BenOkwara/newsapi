import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
    HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'
    SEARCH_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General
         configuration settings. We have added the debug= true which
         enables debug mode in our application.
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}