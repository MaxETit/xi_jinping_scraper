#Xi Jinping Quotifier
import os
import requests
import time
from bs4 import BeautifulSoup

def get_quote():
    print('Finding page...')
    page = requests.get('http://www.chinadaily.com.cn/china/xismoments')
    soup = BeautifulSoup(page.content, 'html.parser')
    print('Retrieving quote...')
    daily_quote = soup.find('div', {'txt'}).get_text()
    date = soup.find('div', {'calendar'}).get_text()
    quote_and_date = date + ': "' + daily_quote
    print('Adding quote to list...')
    with open ('xi_daily_quotes.txt', 'a') as f:
        f.write(quote_and_date + '\n')

while True:
    get_quote()
    print('Sleeping for one day...')
    time.sleep(86400)