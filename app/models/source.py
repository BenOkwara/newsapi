class Source:
    '''
        News Source class to define Source Objects
        '''

    def __init__(self, id, name, description, url, category, country ):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

    '''
    1. ID - The name of the news source according to its identification tag, e.g BBC-news, CNN, ABC
    2. Name - The actual name of the news company
    3. Description - A brief description of the new company
    4. URL - The URL link or website to the news company 
    5. Category - The category of news ,e.g entertainment, business, technology
    6. Country - The country that the news originates from, e.g ABC News is from USA
    '''