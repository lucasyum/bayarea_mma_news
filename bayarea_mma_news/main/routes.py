from flask import render_template, request, Blueprint, redirect, url_for
from bs4 import BeautifulSoup
import requests
import json
import datetime

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def get_news():

    # East Bay

    east_bay_url = 'https://www.eastbaytimes.com/'

    east_bay_news = requests.get(east_bay_url).text

    east_bay_soup = BeautifulSoup(east_bay_news, 'html.parser')

    east_bay_article = east_bay_soup.find('div', class_='article-info')

    east_bay_title = east_bay_article.a.text.strip()
    east_bay_description = east_bay_article.find('div', class_='excerpt').text.strip()

    for link in east_bay_article('a'):
        east_bay_url_link = east_bay_url + link.get('href')
    

    # North Bay

    north_bay_url = 'https://www.marinij.com/'
    north_bay_news = requests.get(north_bay_url).text

    north_bay_soup = BeautifulSoup(north_bay_news, 'html.parser')
    north_bay_article = north_bay_soup.find('div', class_='article-info')

    north_bay_title = north_bay_article.a.text.strip()
    north_bay_description = north_bay_article.find('div', class_='excerpt').text.strip()

    for link in north_bay_article('a'):
        north_bay_url_link = link.get('href')



    # SF News

    sf_url = 'https://abc7news.com/'
    sf_news = requests.get(sf_url).text

    sf_soup = BeautifulSoup(sf_news, 'html.parser')

    sf_title = sf_soup.find('div', class_="headline").text
    sf_description = sf_soup.find('div', class_="callout").text
    sf_article = sf_soup.find('div', class_='headline-list-item has-image')

    for link in sf_article('a'):
        sf_url_link = link.get('href')

    
    south_bay_url = 'https://www.mercurynews.com/location/san-jose/'
    south_bay_news = requests.get(south_bay_url).text

    south_bay_soup = BeautifulSoup(south_bay_news, 'html.parser')


    south_bay_article = south_bay_soup.find('div', class_='feature-top')
    south_bay_title = south_bay_article.find('a', class_='article-title').text.strip()
    south_bay_description = south_bay_article.find('div', class_='excerpt').text.strip()

    for link in south_bay_article('a'):
        south_bay_url_link = link.get('href')

    
    # Fremont Weather

    api_key = '271d1234d3f497eed5b1d80a07b3fcd1'

    fremont_city = 'fremont'
    fremont_url = f'http://api.openweathermap.org/data/2.5/weather?q={ fremont_city }&units=imperial&appid={ api_key }'
    

    fremont_response = requests.get(fremont_url)

    fremont_data = fremont_response.json()

    degree_sign = u"\N{DEGREE SIGN}"
    temperature = str((fremont_data['main']['temp'])) + " F" + degree_sign
    min_temperature = str((fremont_data['main']['temp_min'])) + " F" + degree_sign
    max_temperature = str((fremont_data['main']['temp_min'])) + " F" + degree_sign
    feels_like = str(fremont_data['main']['feels_like']) + " F" + degree_sign
    time_now = datetime.datetime.now().strftime("%X")

    fremont_weather = f"The weather in {fremont_city} at {time_now} is {temperature}, but it feels like {feels_like}. The minimum temperature today will be {min_temperature} with a maximum temperature of {max_temperature}."


    # San Francisco

    san_francisco_city = 'san francisco'
    san_francisco_url = f'http://api.openweathermap.org/data/2.5/weather?q={ san_francisco_city }&units=imperial&appid={ api_key }'
    

    san_francisco_response = requests.get(san_francisco_url)

    san_francisco_data = san_francisco_response.json()

    degree_sign = u"\N{DEGREE SIGN}"
    temperature = str((san_francisco_data['main']['temp'])) + " F" + degree_sign
    min_temperature = str((san_francisco_data['main']['temp_min'])) + " F" + degree_sign
    max_temperature = str((san_francisco_data['main']['temp_max'])) + " F" + degree_sign
    feels_like = str(san_francisco_data['main']['feels_like']) + " F" + degree_sign
    time_now = datetime.datetime.now().strftime("%X")

    san_francisco_weather = f"The weather in {san_francisco_city} at {time_now} is {temperature}, but feels like {feels_like}. The minimum temperature today will be {min_temperature} with a maximum temperatore of {max_temperature}."


    # San Jose

    san_jose_city = 'san jose'
    san_jose_url = f'http://api.openweathermap.org/data/2.5/weather?q={ san_jose_city }&units=imperial&appid={ api_key }'

    san_jose_response = requests.get(san_jose_url)

    san_jose_data = san_jose_response.json()

    degree_sign = u"\N{DEGREE SIGN}"
    temperature = str((san_jose_data['main']['temp'])) + " F" + degree_sign
    min_temperature = str((san_jose_data['main']['temp_min'])) + " F" + degree_sign
    max_temperature = str((san_jose_data['main']['temp_max'])) + " F" + degree_sign
    feels_like = str(san_jose_data['main']['feels_like']) + " F" + degree_sign
    time_now = datetime.datetime.now().strftime("%X")

    san_jose_weather = f"The weather in {san_jose_city} at {time_now} is {temperature}, but feels like {feels_like}. The minimum temperature today will be {min_temperature} with a maximum temperature of {max_temperature}."

    # Marin City

    marin_city = 'marin city'
    marin_city_url = f'http://api.openweathermap.org/data/2.5/weather?q={ marin_city }&units=imperial&appid={ api_key }'

    marin_city_response = requests.get(marin_city_url)

    marin_city_data = marin_city_response.json()

    degree_sign = u"\N{DEGREE SIGN}"
    temperature = str((marin_city_data['main']['temp'])) + " F" + degree_sign
    min_temperature = str((marin_city_data['main']['temp_min'])) + " F" + degree_sign
    max_temperature = str((marin_city_data['main']['temp_max'])) + " F" + degree_sign
    feels_like = str(marin_city_data['main']['feels_like']) + " F" + degree_sign
    time_now = datetime.datetime.now().strftime("%X")

    marin_city_weather = f"The weather in {marin_city} at {time_now} is {temperature}, but feels like {feels_like}. The minimum temperature today will be {min_temperature} with a maximum temperature of {max_temperature}."



    return render_template('home.html',
                                east_bay_title = east_bay_title,
                                east_bay_description = east_bay_description,
                                east_bay_url_link = east_bay_url_link,

                                north_bay_title = north_bay_title,
                                north_bay_description=north_bay_description,
                                north_bay_url_link=north_bay_url_link,

                                sf_title = sf_title,
                                sf_description = sf_description,
                                sf_url_link = sf_url_link,

                                south_bay_title = south_bay_title,
                                south_bay_description = south_bay_description,
                                south_bay_url_link = south_bay_url_link,

                                fremont_weather = fremont_weather,
                                san_francisco_weather = san_francisco_weather,
                                san_jose_weather = san_jose_weather,
                                marin_city_weather = marin_city_weather
                                )  


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/bbc")
def bbc():
    return redirect('https://www.bbc.com/news')


@main.route("/reuters")
def reuters():
    return redirect('https://www.reuters.com/')


@main.route("/bloodyelbow")
def bloodyelbow():
    return redirect('https://www.bloodyelbow.com/')


@main.route("/sherdog")
def sherdog():
    return redirect('https://forums.sherdog.com/')
