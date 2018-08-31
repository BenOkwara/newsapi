from flask import render_template
from app import app
from .requests import get_sources, get_articles, get_headlines

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''

    # Getting popular news from different categories
    general_news = get_sources('general')[0:10]

    headlines=get_headlines()[0:10]
    print(headlines)
    # headlines=headlines [0:10]

    business_news = get_sources('business')[0:10]
    entertainment_news = get_sources('entertainment')[0:10]
    technology_news = get_sources('technology')[0:10]
    sports_news = get_sources('general')[0:10]
    science_news = get_sources('science')[0:10]
    health_news = get_sources('health')[0:10]

    articles = get_articles('id')
    articles=articles[0:10]


    message = 'Welcome to News api room'
    title = 'Home - Welcome to The best News Review Website Online'

    return render_template('index.html',
                           articles=articles,
                           headlines=headlines,
                           general=general_news,
                           business=business_news,
                           entertainment=entertainment_news,
                           technology=technology_news,
                           science=science_news,
                           health=health_news,
                           sports=sports_news)
#
# def article(id):
#     '''
#     returns the articles
#     '''
#     article_news = get_articles('id')
#     description_news=get_articles('description')
#     publishedAt_news=get_articles('publishedAt')
#     author_news=get_articles('author')
#     name_news=get_articles('name')
#     url_news=get_articles('url')
#     urlToImage_news=get_articles('urlToImage')
#
#     title = f'{id}'
#     return render_template('article.html',
#                            title=title,
#                            article=article_news,
#                            author=author_news,
#                            description=description_news,
#                            publishedAt=publishedAt_news,
#                            name=name_news,
#                            url=url_news,
#                            urlToImage=urlToImage_news,
#                            )
#
#
# def headlines(id):
#     '''
#     returns the articles
#     '''
#     article_news = get_headlines('id')
#     description_news=get_headlines('description')
#     publishedAt_news=get_headlines('publishedAt')
#     author_news=get_headlines('author')
#     name_news=get_headlines('name')
#     url_news=get_headlines('url')
#     urlToImage_news=get_headlines('urlToImage')
#
#     title = f'{id}'
#     return render_template('article.html',
#                            title=title,
#                            article=article_news,
#                            author=author_news,
#                            description=description_news,
#                            publishedAt=publishedAt_news,
#                            name=name_news,
#                            url=url_news,
#                            urlToImage=urlToImage_news,
#                            )
#

@app.route('/general')
def general():

    general_news = get_sources('general')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('general.html',general=general_news)

# BUSINESS PAGE

@app.route('/<category>')
def business(category):

    business_news = get_sources(category)
    title= 'Home Page - Get The latest News Online Across The World'
    return render_template('business.html',business=business_news)

# ENTERTAINMENT PAGE

@app.route('/entertainment')
def entertainment():

    entertainment_news = get_sources('entertainment')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('entertainment.html', entertainment=entertainment_news)

# TECHNOLOGY PAGE

@app.route('/technology')
def technology():

    technology_news = get_sources('technology')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('technology.html',technology=technology_news)

# SPORTS

@app.route('/sports')
def sports():

    sports_news = get_sources('general')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('sports.html',sports=sports_news)

# SCIENCE
@app.route('/science')
def science():

    science_news = get_sources('science')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('science.html',science=science_news)

# HEALTH

@app.route('/health')
def health():

    health_news = get_sources('health')
    title= 'Home Page - Get The latest News Online Across The World'
    return render_template('health.html',health=health_news)


@app.route('/source/<id>')
def source(source_id):
    '''

    Display news companies e.g BBC, CNN details page and data being specific articles
    posted by news sources.
    '''
    return render_template('sources.html',id=id)




app.route('/source/<article_id>')
def source(article_id):
    return