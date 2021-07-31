snscrape
snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

The following services are currently supported:

Facebook: user profiles, groups, and communities (aka visitor posts)
Instagram: user profiles, hashtags, and locations
Reddit: users, subreddits, and searches (via Pushshift)
Telegram: channels
Twitter: users, user profiles, hashtags, searches, threads, and list posts
VKontakte: user profiles
Weibo (Sina Weibo): user profiles
Please note that some features listed here may only be available in the current development version of snscrape.

Requirements
snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.

Installation
pip3 install snscrape
If you want to use the development version:

pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
Usage
To get all tweets by Jason Scott (@textfiles):

snscrape twitter-user textfiles
It's usually useful to redirect the output to a file for further processing, e.g. in bash using the filename twitter-@textfiles:

snscrape twitter-user textfiles >twitter-@textfiles
To get the latest 100 tweets with the hashtag #archiveteam:

snscrape --max-results 100 twitter-hashtag archiveteam
Other noteworthy options are:

--format to customise the output format.
--jsonl to get output as JSONL. This includes all information extracted by snscrape (e.g. message content, datetime, images; details vary by the module and scraper).
--with-entity to get an item on the entity being scraped, e.g. the user or channel. This is not supported on all scrapers. (You can use this together with --max-results 0 to only fetch the entity info.)
snscrape --help or snscrape <module> --help provides details on the available options. snscrape --help also lists all available modules.

It is also possible to use snscrape as a library in Python, but this is currently undocumented.

i have been  added feature export output to a excel file


below command converts output tweets into excel


  
  snscrape --max-results 100 twitter-hashtag SBIN >tweets.json   

  
  
python3 json2excel.py
  
  
snscrape --max-results 100 twitter-user SBIN >tweets.json
  
 python3 json2excel.py
  
  
  
  
  similarly you can track and backup important tweets in excel file


ls
you can observe output1.csv  file which our tweets in excel
