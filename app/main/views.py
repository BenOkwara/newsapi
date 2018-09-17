from flask import render_template, request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles, get_headlines


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''

    # Getting popular news from different categories
    general_news = get_sources('general')[0:5]

    headlines = get_headlines()[0:5]
    print(headlines)
    # headlines=headlines [0:10]

    business_news = get_sources('business')[0:5]
    entertainment_news = get_sources('entertainment')[0:5]
    technology_news = get_sources('technology')[0:5]
    sports_news = get_sources('general')[0:5]
    science_news = get_sources('science')[0:5]
    health_news = get_sources('health')[0:5]

    articles = get_articles('id')
    articles = articles[0:5]

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

@main.route('/general')
def general():
    general_news = get_sources('general')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('general.html', general=general_news)


# BUSINESS PAGE

@main.route('/<category>')
def business(category):
    business_news = get_sources(category)
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('business.html', business=business_news)


@main.route('/articles/<id>')
def articles(id):
    '''
       View  page function that returns the details page and its data
       '''
    name = "melissamalala"
    articles = get_articles(id)

    return render_template('article.html', articles=articles, name=name, name_source=id)


@main.route('/entertainment')
def entertainment():
    entertainment_news = get_sources('entertainment')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('entertainment.html', entertainment=entertainment_news)


# TECHNOLOGY PAGE

@main.route('/technology')
def technology():
    technology_news = get_sources('technology')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('technology.html', technology=technology_news)


# SPORTS

@main.route('/sports')
def sports():
    sports_news = get_sources('sports')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('sports.html', sports=sports_news)


# SCIENCE
@main.route('/science')
def science():
    science_news = get_sources('science')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('science.html', science=science_news)


# HEALTH

@main.route('/health')
def health():
    health_news = get_sources('health')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('health.html', health=health_news)

