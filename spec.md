# BACKGROUND
Parents are hard workers and get home really late. They always seem to miss the news and are frustrated that they do not have the time to catch up on current affairs.I built  an application that will help them list and preview news articles from various sources.

# FEATURES AND FUNCTIONALITY
-Users  are able to see various news sources and select the ones they prefer
Users  are able to see all the news articles from that news source
Users  see the image description and time the news article was created.
 User is able to click on an article and read it fully from the news source.

# MAINTENANCE PLAN
You can also:
Keep secure: monitor for malware, viruses, hackers, and errors
Keep updated: Software
Keep updated: Content


##News Website desgined by Melissa Malala  through News API for News API. The app is live here :https://newsapibymelissa.herokuapp.com/
# Features
•	Built with Python and Flask
•	Shows News Sources, 'News Articles by Sources’
•	Styled using Bootstrap 4
##Installation
$ git clone <repository_url>

##Usage
NOTE: You need to have fully cloned it to run it locally.
$ ./start.sh 

# it will launch the web page from local server and fetch 
news using api provided
##API Object Reference
##Classes: Sources, Articles, Headlines
##Class: Sources
Each Sources has the following properties
•	name - news source name
•	id - news source unique id
•	description - info about the news source
•	url - official website link to news source
##Class: Article
Each Article has the following properties
•	id - unique id of the article
•	title - the title of the article itself
•	description - the article itself and what it is about
•	published time - time when it was submitted
•	image url - image url for image tags
•	url - url to website for full article
##Class: Headlines
Each Article has the following properties
•	id - unique id of the article
•	title - the title of the article itself
•	description - the article itself and what it is about
•	published time - time when it was submitted
•	image url - image url for image tags
•	url - url to website for full article
##Tests
To run the tests locally just do:
$ cd app
$ python3.7 classes_test.py
The tests are run on a local test server.
##Contribute
If you want to add any new features, or improve existing ones, feel free to send a pull request! Email me on melissamalala@gmail.com if you have any questions or discover any bugs. 
