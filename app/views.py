from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.

    '''

    # Getting popular news from different categories
    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    technology_news = get_sources('technology')
    sports_news = get_sources('general')
    science_news = get_sources('science')
    health_news = get_sources('health')

    message = 'Welcome to News api room'
    title = 'Home - Welcome to The best News Review Website Online'

    return render_template('index.html',
                            message=message,
                            title=title,
                            general=general_news,
                           business=business_news,
                           entertainment=entertainment_news,
                           technology=technology_news,
                           sports=sports_news,
                           science=science_news,
                           health=health_news)

@app.route('/general')
def general():

    general_news = get_sources('general')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('general.html',general=general_news)

# BUSINESS PAGE

@app.route('/business')
def business():

    business_news = get_sources('business')
    title= 'Home Page - Get The latest News Online Across The World'
    return render_template('business.html',business=business_news)

@app.route('/entertainment')
def entertainment():

    entertainment_news = get_sources('entertainment')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('entertainment.html', entertainment=entertainment_news)

@app.route('/technology')
def technology():

    technology_news = get_sources('technology')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('technology.html',technology=technology_news)


@app.route('/sports')
def sports():

    sports_news = get_sources('general')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('sports.html',sports=sports_news)


@app.route('/science')
def science():

    science_news = get_sources('science')
    title = 'Home Page - Get The latest News Online Across The World'
    return render_template('science.html',science=science_news)

@app.route('/health')
def health():

    health_news = get_sources('health')
    title= 'Home Page - Get The latest News Online Across The World'
    return render_template('health.html',health=health_news)


@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View source page function that returns the news company page and its data.
    In this project, I will use source to describe the "news company", in the
    LMS it's the movie page that has many movies.
    A user can then click on movies to see a specific movie, so in my project.
    A user will be able to click on specific news company
    to see the news articles written by the company.
    These articles will be displayed in a card format
    so I'll edit that in the bootstrap and HTML of the articles.html.
    View source page function that returns the source of the news
     e.g BBC, CNN details page and its data, the data being the specific
     articles posted by the specific news company or source.
    These articles will be displayed in a card format so I'll edit that
    in the bootstrap and HTML of the articles.html.
    View source page function that returns the source of the
    news e.g BBC, CNN details page and its data, the data being the specific articles
    posted by the specific news company or source.
    '''

    return render_template('sources.html',id=source_id)