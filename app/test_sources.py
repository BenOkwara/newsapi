import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
        Test Class to test the behaviour of the News Source class
        '''
    def setUp(self):
        '''
                Set up method that will run before every Test
                '''
        self.new_source = Source("abc-news",
                                 'ABC News',
                                 "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
                                  "http://abcnews.go.com",
                                 "general",
                                 "us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
            '''
            test_init to ensure objects are instantiated correctly
            :return:
            '''
            self.assertEqual(self.new_source.id, "al-jazeera-english")
            self.assertEqual(self.new_source.name, "Al Jazeera English")
            self.assertEqual(self.new_source.description, 'News, analysis from the Middle East'
                                                          ' and worldwide, multimedia'
                                                          ' and interactives,'
                                                          ' opinions, documentaries, podcasts, '
                                                          'long reads and broadcast schedule.')
            self.assertEqual(self.new_source.url, "http://www.aljazeera.com")
            self.assertEqual(self.new_source.category, "general")
            self.assertEqual(self.new_source.country, "us")

    if __name__ == '__main__':
        unittest.main()