#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dependencies

from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_collection = {}

    # Mars News 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')


    mars_collection["news_title"] = soup.find('div', class_= 'content_title').get_text()
    mars_collection["news_snip"] = soup.find_all('div', class_="rollover_description_inner").get_text()

    # Mars Feature Image

    url_feature_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_feature_image)
    response = browser.html
    soup2 = BeautifulSoup(response, 'html.parser')

    img_src = []

    for image in images:
        img = image['data-fancybox-href']
        img_src.append(img)

    mars_collection["featrued_image_url"] = "https://www.jpl.nasa.gov" + img_src[2]

    # Mars Weather
    
    url_weather = ('https://twitter.com/marswxreport?lang=en')
    browser.visit(url_weather)
    response = browser.html
    soup3 = BeautifulSoup(response, 'html.parser')
    weather = soup3.find_all("div",class_="js-tweet-text-container")
    weather_mars = []
    
    for content in weather:
        tweet = content.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        weather_mars.append(tweet)
    mars_collection["mars_weather"] = weather_mars[8]


    # Mars Facts

    url_facts = "https://space-facts.com/mars/"
    df_facts = pd.read_html(url_facts)[0]
    df_facts.columns = ["Facts","Values"]
    clean_table = df_facts.set_index(["Facts"])
    mars_table = clean_table.to_html()
    mars_table = mars_table.replace("\n", "")
    mars_collection["fact_table"] = mars_table

    # Mars Hemisphere 

    hemisphere_image_urls = []

    # Cerberus Hemisphere

    url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_cerberus)
    response_cerberus = browser.html
    soup4 = BeautifulSoup(response_cerberus, 'html.parser')
    cerberus_img = soup4.find_all('div', class_="wide-image-wrapper")

    for img in cerberus_img:
        pic_cerberus = img.find('li')
        cerberus_full_img = pic_cerberus.find('a')['href']
    cerberus_title = soup4.find('h2', class_='title').get_text()
    cerberus_hem = {"Title": cerberus_title, "url": cerberus_full_img}

    hemisphere_image_urls.append(cerberus_hem)

    # Schiaparelli Hemisphere 

    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_cerberus)
    response_schiaparelli = browser.html
    soup5 = BeautifulSoup(response_schiaparelli, 'html.parser')
    schiaparelli_img = soup5.find_all('div', class_="wide-image-wrapper")

    for img in schiaparelli_img:
        pic_schiaparelli = img.find('li')
        schiaparelli_full_img = pic_schiaparelli.find('a')['href']
    schiaparelli_title = soup5.find('h2', class_='title').get_text()
    schiaparelli_hem = {"Title": schiaparelli_title, "url": schiaparelli_full_img}
    
    hemisphere_image_urls.append(schiaparelli_hem)

    # Syrtis Hemisphere

    url_syrtis = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')
    browser.visit(url_syrtis)
    response_syrtis = browser.html
    soup6 = BeautifulSoup(response_syrtis, 'html.parser')
    syrtris_img = soup6.find_all('div', class_="wide-image-wrapper")

    for img in syrtris_img:
        pic_syrtris = img.find('li')
        syrtris_full_img = pic_syrtris.find('a')['href']
    syrtris_title = soup6.find('h2', class_='title').get_text()
    syrtris_hem = {"Title": syrtris_title, "url": syrtris_full_img}

    hemisphere_image_urls.append(syrtris_hem)

     # Valles Marineris Hemisphere

    url_valles = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')
    browser.visit(url_valles)
    response_valles = browser.html
    soup7 = BeautifulSoup(response_valles, 'html.parser')
    valles_img = soup7.find_all('div', class_="wide-image-wrapper")

    for img in valles_img:
        pic_valles = img.find('li')
        valles_full_img = pic_valles.find('a')['href']
    valles_title = soup7.find('h2', class_='title').get_text()
    valles_hem = {"Title": valles_title, "url": valles_full_img}
    
    hemisphere_image_urls.append(valles_hem)

    ## Collection of information
    mars_collection["hemisphere_image"] = hemisphere_image_urls

    return mars_collection