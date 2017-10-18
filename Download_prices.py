
## https://www.coingecko.com/price_charts/export/dash/usd.csv?locale=en


import requests

#Addresses of the csv on coingecko, must match with the string below
addresses = "https://www.coingecko.com/price_charts/export/bitcoin/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/monero/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/litecoin/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/ethereum/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/dash/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/neo/usd.csv?locale=en",\
            "https://www.coingecko.com/price_charts/export/nem/btc.csv?locale=en"

names = "bitcoin","monero","litecoin","ethereum","dashpay", "neo","nem"

def download_price():
    i = 0;
    for address in addresses:
        print("downloading price of " + names[i])
        url = address
        #Update with your local directory    
        fileName = "/home/fmerizzi/Desktop/scrapingBuffer/"+ names[i] + "price" ".csv"

        req = requests.get(url)
        file = open(fileName, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
        i = i+1;


##download_price()
