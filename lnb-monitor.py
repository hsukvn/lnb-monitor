#!/usr/bin/env python3

import sys
import requests

url = 'https://www.lnb.com.tw/api/market-place?periods=24&source=complex&page=1'

r = requests.get(url)
if r.status_code != 200:
    print('fail to get results')
    sys.exit(1)

loans = r.json()['data']

good_loans = []
for loan in loans:
    if loan['status'] == 'primary_unfinished' and loan['return_on_investment_pretty'] >= 10:
        good_loans.append(loan)

for loan in good_loans:
    print(loan)

sys.exit(0)
