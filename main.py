from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import FancyURLopener
from gtts import gTTS
import sys 

article_links = sys.argv

class myOpener(FancyURLopener):
	version = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
openurl = myOpener().open

for article in range(1,len(article_links)):
    url = article_links[article]
    page = BeautifulSoup(openurl(url).read().decode('utf-8', 'ignore'), "lxml", parse_only=SoupStrainer('main'))
    article_text = []
    file_name = ""
    for title in page.find_all('h1', {'class': 'graf'}):
        article_title = 'Title: ' + str(title.text)
        file_name = title.text
        article_text.append(article_title)   
    for paragraphs in page.find_all('p', {'class': 'graf'}):
    	article_text.append(paragraphs.text)
    text_for_speech = '\n\n'.join(article_text)
    tts = gTTS(text=text_for_speech, lang='en')
    tts.save("articles/" + file_name + ".mp3")

