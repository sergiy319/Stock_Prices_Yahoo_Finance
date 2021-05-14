import requests
from bs4 import BeautifulSoup

# Create custom headers.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/90.0.4430.212 Safari/537.36'
}

# Save in a variable the url of a specific page
# from which we are going to parse information.
urls = ['https://finance.yahoo.com/quote/PD/history?p=PD',
        'https://finance.yahoo.com/quote/ZUO/history?p=ZUO',
        'https://finance.yahoo.com/quote/PINS/history?p=PINS',
        'https://finance.yahoo.com/quote/ZM/history?p=ZM',
        'https://finance.yahoo.com/quote/DOCU/history?p=DOCU',
        'https://finance.yahoo.com/quote/CLDR/history?p=CLDR',
        'https://finance.yahoo.com/quote/RUN/history?p=RUN']

# Save the method for obtaining information into a variable.
r = requests.get(urls)

# Create a variable for parsing.
soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

change = soup.find('span', {'class': 'C($primaryColor) Fz(24px) Fw(b)'}).text

print(price, change)
