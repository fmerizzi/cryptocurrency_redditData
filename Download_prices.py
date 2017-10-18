import requests
import Constants as cons
def download_price(currencies):
    for currency in currencies:
        print("downloading price of " + currency)
        url = "https://www.coingecko.com/price_charts/export/" + currency + "/usd.csv?locale=en"

        #Update with your local directory    
        fileName = cons.directory + currency + "price" ".csv"

        req = requests.get(url)
        file = open(fileName, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()


##download_price()
