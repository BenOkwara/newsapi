from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Welcome to News API'
    return render_template('index.html', message = message)

@app.route('/source/<movie_id>')
def source(source_id):

    '''
    In this project, I will use source to describe the "news company", in the LMS it's the movie page that has many movies.
     A user can then click on movies to see a specific movie, so in my project.
      A user will be able to click on specific news company to see the news articles written by the company.
      These articles will be displayed in a card format so I'll edit that in the bootstrap and HTML of the articles.html.
    View source page function that returns the source of the news e.g BBC, CNN details page and its data, the data being the specific articles posted by the specific news company or source
    '''
    return render_template('source.html',id = source_id)