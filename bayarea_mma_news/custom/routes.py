import requests
import json
import datetime
from flask import Blueprint, render_template, request, redirect, url_for

from bs4 import BeautifulSoup

custom = Blueprint('custom', __name__)

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
headers = {'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': "14cbe34b16msh88adb496424ae59p178c08jsne132fa29607f"}

apple_params = {"region": "US", "symbol": "AAPL"}
cisco_params = {"region": "US", "symbol": "CSCO"}
google_params = {"region": "US", "symbol": "GOOGL"}
facebook_params = {"region": "US", "symbol": "FB"}
microsoft_params = {"region": "US", "symbol": "MSFT"}
panw_params = {"region": "US", "symbol": "PANW"}
snow_params = {"region": "US", "symbol": "NOW"}
ibm_params = {"region": "US", "symbol": "IBM"}
intel_params = {"region": "US", "symbol": "INTC"}
accenture_params ={"region": "US", "symbol": "ACN"}


apple_response = requests.request("GET", url, headers=headers, params=apple_params)
cisco_response = requests.request("GET", url, headers=headers, params=cisco_params)
google_response = requests.request("GET", url, headers=headers, params=google_params)
ibm_response = requests.request("GET", url, headers=headers, params=ibm_params)
intel_response = requests.request("GET", url, headers=headers, params=intel_params)
facebook_response = requests.request("GET", url, headers=headers, params=facebook_params)
microsoft_response = requests.request("GET", url, headers=headers, params=microsoft_params)
snow_response = requests.request("GET", url, headers=headers, params=snow_params)
panw_response = requests.request("GET", url, headers=headers, params=panw_params)    # PANW is the ticker for "Palo Alto Networks"
accenture_response = requests.request("GET", url, headers=headers, params=accenture_params) 


@custom.route("/stocks")

def get_price():
    apple_current_price = 'This is the current price $' + apple_response.json()['financialData']['currentPrice']['fmt']
    accenture_current_price = 'This is the current price $' + accenture_response.json()['financialData']['currentPrice']['fmt']
    cisco_current_price = 'This is the current price $' + cisco_response.json()['financialData']['currentPrice']['fmt']
    google_current_price = 'This is the current price $' + google_response.json()['financialData']['currentPrice']['fmt']
    facebook_current_price = 'This is the current price $' + facebook_response.json()['financialData']['currentPrice']['fmt']
    ibm_current_price = 'This is the current price $' + ibm_response.json()['financialData']['currentPrice']['fmt']
    intel_current_price = 'This is the current price $' + intel_response.json()['financialData']['currentPrice']['fmt']
    snow_current_price = 'This is the current price $' + snow_response.json()['financialData']['currentPrice']['fmt']
    microsoft_current_price = 'This is the current price $' + microsoft_response.json()['financialData']['currentPrice']['fmt']
    panw_current_price = 'This is the current price $' + panw_response.json()['financialData']['currentPrice']['fmt']

    return render_template('stocks.html',
                             apple_current_price = apple_current_price,
                             cisco_current_price = cisco_current_price,
                             google_current_price = google_current_price,
                             snow_current_price = snow_current_price,  
                             facebook_current_price = facebook_current_price,  
                             ibm_current_price = ibm_current_price,
                             intel_current_price = intel_current_price,
                             microsoft_current_price = microsoft_current_price,
                             panw_current_price = panw_current_price,
                             accenture_current_price = accenture_current_price              
                            )

# Mixed Martial Arts Rankings

@custom.route('/mma', methods=['GET'])

def get_rankings():


    mma_url = 'http://rankingmma.com/p4p'


    mma_rankings = requests.get(mma_url).text
    mma_soup = BeautifulSoup(mma_rankings, 'html.parser')
    mma_article = mma_soup.find('tbody', class_='row-hover')

    # 1

    first_name = mma_soup.find('tr', class_='row-2 even').a.text
    first_record = mma_soup.find('td', class_='column-6').text
    first_last_fight = mma_soup.find('td', class_='column-7').text.strip()
    first_link = mma_soup.find('td', class_='column-4')
    for link in first_link('a'):
        first_fighter_link = link.get('href')
        
    # 2

    second_name = mma_soup.find('tr', class_='row-3 odd').a.text
    second = mma_soup.find('tr', class_='row-3 odd')
    second_record = second.find('td', class_='column-6').text
    second_last_fight = second.find('td', class_='column-7').text
    second_link = second.find('td', class_='column-4')
    for link in second_link('a'):
        second_fighter_link = link.get('href')

    # 3

    third_name = mma_soup.find('tr', class_='row-4 even').a.text
    third = mma_soup.find('tr', class_='row-4 even')
    third_record = third.find('td', class_='column-6').text
    third_last_fight = third.find('td', class_='column-7').text
    third_link = third.find('td', class_='column-4')
    for link in third_link('a'):
        third_fighter_link = link.get('href')

    # 4

    fourth_name = mma_soup.find('tr', class_='row-5 odd').a.text
    fourth = mma_soup.find('tr', class_='row-5 odd')
    fourth_record = fourth.find('td', class_='column-6').text
    fourth_last_fight = fourth.find('td', class_='column-7').text
    fourth_link = fourth.find('td', class_='column-4')
    for link in fourth_link('a'):
        fourth_fighter_link = link.get('href')

    # 5

    fifth_name = mma_soup.find('tr', class_='row-6 even').a.text
    fifth = mma_soup.find('tr', class_='row-6 even')
    fifth_record = fifth.find('td', class_='column-6').text
    fifth_last_fight = fifth.find('td', class_='column-7').text
    fifth_link = fifth.find('td', class_='column-4')
    for link in fifth_link('a'):
        fifth_fighter_link = link.get('href')

    # 6

    sixth_name = mma_soup.find('tr', class_='row-7 odd').a.text
    sixth = mma_soup.find('tr', class_='row-7 odd')
    sixth_record = sixth.find('td', class_='column-6').text
    sixth_last_fight = sixth.find('td', class_='column-7').text
    sixth_link = sixth.find('td', class_='column-4')
    for link in sixth_link('a'):
        sixth_fighter_link = link.get('href')

    # 7

    seventh_name = mma_soup.find('tr', class_='row-8 even').a.text
    seventh = mma_soup.find('tr', class_='row-8 even')
    seventh_record = seventh.find('td', class_='column-6').text
    seventh_last_fight = seventh.find('td', class_='column-7').text
    seventh_link = seventh.find('td', class_='column-4')
    for link in seventh_link('a'):
        seventh_fighter_link = link.get('href')

    # 8

    eighth_name = mma_soup.find('tr', class_='row-9 odd').a.text
    eighth = mma_soup.find('tr', class_='row-9 odd')
    eighth_record = eighth.find('td', class_='column-6').text
    eighth_last_fight = eighth.find('td', class_='column-7').text
    eighth_link = eighth.find('td', class_='column-4')
    for link in eighth_link('a'):
        eighth_fighter_link = link.get('href')

    # 9

    ninth_name = mma_soup.find('tr', class_='row-10 even').a.text
    ninth = mma_soup.find('tr', class_='row-10 even')
    ninth_record = ninth.find('td', class_='column-6').text
    ninth_last_fight = ninth.find('td', class_='column-7').text
    ninth_link = ninth.find('td', class_='column-4')
    for link in ninth_link('a'):
        ninth_fighter_link = link.get('href')

    # 10

    tenth_name = mma_soup.find('tr', class_='row-11 odd').a.text
    tenth = mma_soup.find('tr', class_='row-11 odd')
    tenth_record = tenth.find('td', class_='column-6').text
    tenth_last_fight = tenth.find('td', class_='column-7').text
    tenth_link = tenth.find('td', class_='column-4')

    for link in tenth_link('a'):
        tenth_fighter_link = link.get('href')

    # MMA News

    # MMA Mania

    mma_mania_url = 'https://www.mmamania.com'
    source = requests.get(mma_mania_url).text
    soup = BeautifulSoup(source, 'html.parser')

    article = soup.find('div', class_='c-compact-river__entry')

    mma_mania_headline = article.h2.text
    mma_mania_description = article.p

    for link in article.h2:
        mma_mania_headline_link = link.get('href')

   # MMA Weekly

    mma_weekly_url = 'https://www.mmaweekly.com/'

    source = requests.get(mma_weekly_url).text
    soup = BeautifulSoup(source, 'html.parser')

    article = soup.find('div', class_='span4')

    mma_weekly_headline = article.h3.text
    mma_weekly_description = article.p.text

    for link in article.h3:
        mma_weekly_link = link.get('href')

    # Bloody Elbow

    bloody_elbow_url = 'https://www.bloodyelbow.com/'
    source = requests.get(bloody_elbow_url).text
    
    soup = BeautifulSoup(source, 'html.parser')
    article = soup.find('div', class_='c-entry-box--compact__body')

    bloody_elbow_headline = article.h2.text
    bloody_elbow_descrption = article.p.text

    for link in article.h2:
        bloody_elbow_link = link.get('href')


    return render_template('mma.html',
                            first_name = first_name,
                            first_record = first_record,
                            first_last_fight = fifth_last_fight,
                            first_fighter_link = first_fighter_link,
                            
                            second_name = second_name,
                            second_record = second_record,
                            second_last_fight = second_last_fight,
                            second_fighter_link = second_fighter_link,
                            
                            third_name = third_name,
                            third_record = third_record,
                            third_last_fight = third_last_fight,
                            third_fighter_link = third_fighter_link, 

                            fourth_name = fourth_name,
                            fourth_record = fourth_record,
                            fourth_last_fight = fourth_last_fight,
                            fourth_fighter_link = fourth_fighter_link,

                            fifth_name = fifth_name,
                            fifth_record = fifth_record,
                            fifth_last_fight = fifth_last_fight,
                            fifth_fighter_link = fifth_fighter_link,

                            sixth_name = sixth_name,
                            sixth_record = sixth_record,
                            sixth_last_fight = sixth_last_fight,
                            sixth_fighter_link = sixth_fighter_link,

                            seventh_name = seventh_name,
                            seventh_record = seventh_record,
                            seventh_last_fight = seventh_last_fight,
                            seventh_fighter_link = seventh_fighter_link,

                            eighth_name = eighth_name,
                            eighth_record = eighth_record,
                            eighth_last_fight = eighth_last_fight,
                            eighth_fighter_link = eighth_fighter_link,

                            ninth_name = ninth_name,
                            ninth_record = ninth_record,
                            ninth_last_fight = ninth_last_fight,
                            ninth_fighter_link = ninth_fighter_link,

                            tenth_name = tenth_name,
                            tenth_record = tenth_record,
                            tenth_last_fight = tenth_last_fight,
                            tenth_fighter_link = tenth_fighter_link,
                            
                            mma_mania_url = mma_mania_url,
                            mma_mania_headline = mma_mania_headline,
                            mma_mania_headline_link = mma_mania_headline_link,
                            mma_mania_description = mma_mania_description,
                            
                            mma_weekly_url = mma_weekly_url,
                            mma_weekly_headline = mma_weekly_headline,
                            mma_weekly_description = mma_weekly_description,
                            mma_weekly_link = mma_weekly_link,
                            
                            bloody_elbow_url = bloody_elbow_url,
                            bloody_elbow_headline = bloody_elbow_headline,
                            bloody_elbow_description = bloody_elbow_descrption,
                            bloody_elbow_link = bloody_elbow_link
                            )

