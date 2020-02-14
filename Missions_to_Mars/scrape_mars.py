#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dependencies

from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
from pprint import pprint
import pymongo
from flask import Flask, render_template
import time
import numpy as np
import json
from selenium import webdriver

# In[6]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[7]:



executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser("chrome", **executable_path, headless = False)


# In[8]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
#Assign the text to variables that you can reference later.

# news_title = "NASA's Treasure Map for Water Ice on Mars"
# news_p = "A new study identifies frozen water just below the Martian surface, where astronauts could easily dig it up."

url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[9]:


#Scrape Page Into Soup

html = browser.html
soup = bs(html, 'html.parser')


# In[10]:



# print(soup.prettify())


# # NASA Mars News

# In[11]:


#scrape the headlines and get rid of white spaces
news_titles = soup.find_all('div', class_= 'content_title')
print(news_titles)


# In[12]:


#scrape body from the website
body = soup.find_all('div', class_="rollover_description")
print(body)


# In[13]:


#Save all the articles from the page
results = soup.find_all('div', class_="slide")
for result in results:
    news_titles = result.find('div', class_="content_title")
    news_title = news_titles.find('a').text
    news_bodies = result.find('div', class_="rollover_description")
    news_body = news_bodies.find('div', class_="rollover_description_inner").text
    print('-------------')
    print(news_title)
    print(news_body)


# # JPL Mars Space Images - Featured Image

# In[14]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[15]:


# print(soup.prettify())


# In[16]:


#pull images from website
images = soup.find_all('a', class_="fancybox")


# In[17]:


#pull image link

img_src = []

for image in images:
    img = image['data-fancybox-href']
    img_src.append(img)

img_url = "https://www.jpl.nasa.gov" + img
img_url


# # Mars Weather

# In[18]:


url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[19]:


# print(soup.prettify())


# In[20]:


contents = soup.find_all("div", class_="content")


# In[21]:


weather_mars = []
for content in contents:
    tweet = content.find('div', class_= "js-tweet-text-container").text
    weather_mars.append(tweet)
    
print(weather_mars)


# In[22]:


mars_weather = weather_mars[8]
print(mars_weather)


# # Mars Facts

# In[23]:


mars_facts_url = 'https://space-facts.com/mars/'
table = pd.read_html(mars_facts_url)
table[0]


# In[24]:


df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


# In[25]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# # Mars Hemispheres

# In[26]:


hemisphere_img_urls = []


# In[35]:


#Cerberus Hemispheres

url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')





# In[36]:


response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[37]:


#print(soup.prettify())


# In[38]:


cerberus_img = soup.find_all('div', class_='wide-image-wrapper')
print(cerberus_img)


# In[40]:


for img in cerberus_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)


# In[41]:


cerberus_title = soup.find('h2', class_='title').text
print(cerberus_title)


# In[42]:


cerberus_hem = {"Title": cerberus_title, "url": full_img}
print(cerberus_hem)


# In[43]:


#Schiaparelli Hemisphere
url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')


# In[44]:


response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[45]:


schiaparelli_img = soup.find_all('div', class_="wide-image-wrapper")
print(schiaparelli_img)


# In[46]:


for img in schiaparelli_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)


# In[48]:


schiaparelli_title = soup.find('h2', class_="title").text
print(schiaparelli_title)


# In[49]:


schiaparelli_hem = {"Title": schiaparelli_title, "url": full_img}
print(schiaparelli_hem)


# In[50]:


#Syrtis Hemisphere
url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')


# In[51]:


response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[55]:


syrtris_img = soup.find_all('div', class_="wide-image-wrapper")
print(syrtris_img)


# In[56]:


for img in syrtris_img:
    pic= img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)


# In[57]:


syrtris_title = soup.find('h2', class_='title').text
print(syrtris_title)


# In[58]:


syrtris_hem = {"Title": syrtris_title, "url": full_img}
print(syrtris_hem)


# In[60]:


#Valles Marineris Hemisphere
url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

response = requests.get(url)
soup = bs(response.text, 'html.parser')


# In[61]:


valles_marineris_img = soup.find_all('div', class_="wide-image-wrapper")
print(valles_marineris_img)


# In[62]:


for img in valles_marineris_img:
    pic= img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)


# In[63]:


valles_marineris_title = soup.find('h2', class_='title').text
print(valles_marineris_title)


# In[64]:


valles_marineris_hem = {"Title": valles_marineris_title, "url": full_img}
print(valles_marineris_hem)


# In[ ]:




