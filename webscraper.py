import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Create the driver with the link to the .exe file
driver = webdriver.Chrome(executable_path='/Users/brooklyndippo/Downloads/chromedriver')

#Choose a website to scrape
driver.get('https://www.washingtonpost.com/')

# Object is “results”, brackets make the object an empty list.
# We will be storing our data here.
headlines = []
journalists = []

# Add the page source to the variable `content`.
content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup 
# class, which analyzes the HTML as a nested data structure and allows to select
# its elements by using various selectors.
soup = BeautifulSoup(content)

# Loop over all elements returned by the `findAll` call. It has the filter `attrs` given
# to it in order to limit the data returned to those elements with a given class only.
for element in soup.findAll(attrs={'class': 'font--headline'}):
    story_link = element.find('a')
    if story_link is not None:
        #print (story_link.text)
        headlines.append(story_link.text)


for element in soup.findAll(attrs={'class': 'byline'}):
    byline = element.find('a')
    if byline is not None:
        #print(byline.text)
        journalists.append(byline.text)

#Create a dataframe with a Blog column and add in the results
series1 = pd.Series(headlines, name = 'Headlines')
series2 = pd.Series (journalists, name = 'Journalists')
df = pd.DataFrame({'Headlines': series1, 'Journalists': series2})
df.to_csv('WashingtonPost.csv', index=False, encoding='utf-8')