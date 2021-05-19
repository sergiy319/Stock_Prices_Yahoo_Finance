import csv
import requests
import json

# Put a list of company names into a variable.
list_company_names = [
    'PD', 'ZUO', 'PINS', 'ZM',
    'PVTL', 'DOCU', 'CLDR', 'RUN']

# Create an empty list for adding data.
download_data = []


# Create a download function.
def get_financial_data(company_name):
    # Create custom headers.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/90.0.4430.212 Safari/537.36'}

    # Save in a variable the url of a CSV file
    # from which we are going to get information.
    Historical_data_CSV_URL = f'https://query1.finance.yahoo.com/v7/finance/download/{company_name}?period1=1589785628&period2=1621321628&interval=1d&events=history&includeAdjustedClose=true'

    # Download historical data CSV file.
    with requests.Session() as rS:
        download_historical_data = rS.get(Historical_data_CSV_URL)

    # Save decoded information to a variable.
    decoded_content = download_historical_data.content.decode('utf-8')

    # Save read information to variable.
    csv_read_info = csv.reader(decoded_content.splitlines(), delimiter=',')

    # Create list historical data.
    list_historical_data = list(csv_read_info)

    for row in list_historical_data:
        print(row)

    return list_historical_data


# We create a loop to process the data of all the necessary company names.
for name in list_company_names:
    download_data.append(get_financial_data(name))
