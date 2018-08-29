from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.

    If we want to display specific categorical news, then we would
     first create a variable and then use the get() method to call it.
    top_headlines = get_sources('us','business')
    We can also have a get_all() function that gets all the news
    Example call from views would be
    everything
    '''
     # My example is
    # typeof_category = get_sources('country','category')
    # print(typeof_category)

    # business_category = get_sources('uk', 'business')
    # print(business_category)
    #
    #
    # general_category = get_sources('uk', 'general')
    # print(general_category)
    #
    # technology_category = get_sources('uk', 'technology')
    # print(technology_category)
    #
    # sports_category = get_sources('uk', 'sports')
    # print(sports_category)
    #
    # health_category = get_sources('uk', 'health')
    # print(health_category)
    #
    # science_category = get_sources('uk', 'science')
    # print(science_category)
    #
    # entertainment_category = get_sources('uk', 'entertainment')
    # print(entertainment_category)
    #
    # test_args = 'The Print Is Actually Showing'

    top_headlines = get_sources('country', 'category')
    print(top_headlines)

    message = 'Welcome to News api room'
    title = 'Home - Welcome to The best News Review Website Online'

    return render_template('index.html',
                           # test_param=test_args,
                           message=message,
                           title=title,
                           top_headlines=top_headlines)
                           # general=general_category,
                           # business=business_category,
                           # technology=technology_category,
                           # sports=sports_category,
                           # health=health_category,
                           # science=science_category,
                           # entertainment=entertainment_category)

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

