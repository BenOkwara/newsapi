class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'



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