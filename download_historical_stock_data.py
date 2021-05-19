# import time
# import datetime
# import pandas as pd
#
# company_names = 'PD'
# period1 = int(time.mktime(datetime.datetime(2019, 4, 11, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2021, 5, 16, 23, 59).timetuple()))
# interval = '1d'
#
# download_link_location = f'https://query1.finance.yahoo.com/v7/finance/download/{company_names}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
#
# df = pd.read_csv(download_link_location)
# print(df)
