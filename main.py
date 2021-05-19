import requests
from bs4 import BeautifulSoup
import json

# Put a list of company names into a variable.
list_company_names = [
    'PD', 'ZUO', 'PINS', 'ZM',
    'PVTL', 'DOCU', 'CLDR', 'RUN']

# Create an empty list for adding data.
download_data = []


# Create a parsing function.
def get_financial_data(company_name):
    # Create custom headers.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/90.0.4430.212 Safari/537.36'}

    # Save in a variable the url of a specific page
    # from which we are going to parse information.
    # url_parsing_page = f'https://finance.yahoo.com/quote/{company_name}/history?p={company_name}'
    url_parsing_page = f'https://query1.finance.yahoo.com/v7/finance/download/{company_name}?period1=1554940800&period2=1621036800&interval=1d&events=history&includeAdjustedClose=true'

    # Save the method for obtaining information into a variable.
    receiving_information = requests.get(url_parsing_page)

    # Create a variable for parsing result.
    parsing_result = BeautifulSoup(receiving_information.text, 'html.parser')

    # Create a variable for data for the whole period.
    stock_data = {
        'company_name': company_name,
        'data_whole_period': parsing_result.find('').find_all('...').text
    }

    return stock_data


# We create a loop to process the data of all the necessary company names.
for name in list_company_names:
    download_data.append(get_financial_data(name))

# Create a file to save data to Json.
with open('download_data.json', 'w') as dj:
    json.dump(download_data, dj)
