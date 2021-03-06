import time
import urllib.request
from urllib.request import urlopen

"""Retrieves public information from 'yahoo finance'
 to develop a quick value analysis of specified stocks. 
 Could be altered to narrow stock output based on desired criteria.
 
 Based on the youtube series 
 'Using programming for fundamental investing' by Sentdex. 
 Updated to Python3 and altered to include specific stocks and filters"""

sp500short = ['aapl','amd','amzn','atvi','baba','brk-b','cmg','dis','fb','goog','itw','ibm','jnj','msft','mo','nflx','nvs','nobl','slb','ts','tsla','ua','vig','vbr','wb','wmt']

def yahooKeyStats(stock):
    try:
        sourceCode = urllib.request.urlopen('http://finance.yahoo.com/q/ks?s='+stock).read()

        pbr = str(sourceCode).split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print('price to book ratio:', stock, pbr)

        PEG5 = str(sourceCode).split('PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print ('PEG5:', PEG5)

        PE12t = str(sourceCode).split('Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print ('Trailing P/E:', PE12t)

        DE= str(sourceCode).split('Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
        print ('Total Debt/Equity', DE)

        print('____________________')
                
    except Exception as e:
        print(e)

for eachStock in sp500short:
    yahooKeyStats(eachStock)
    time.sleep(3) 
