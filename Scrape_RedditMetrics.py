import demjson
import requests
import pandas as pd
import Constants as cons


def Scrape_redditMetrics(currencies):
    for currency in currencies :
        print("Waiting for the data of " + currency + "..")
        r = requests.get('http://www.redditmetrics.com/r/'+ currency)

        json_data = r.text.split('data: ')[1].split('pointSize')[0].strip()[:-1].replace('\n', '')
        growth = demjson.decode(json_data)
        growth_df = pd.DataFrame(growth)
        
        #Update this with your directory
        growth_df.to_csv(cons.directory + currency + "_redditGrowth.csv")

        json_data = r.text.split('data: ')[2].split('pointSize')[0].strip()[:-1].replace('\n', '')
        total = demjson.decode(json_data)
        total_df = pd.DataFrame(total)
        
         #Update this with your directory
        total_df.to_csv(cons.directory + currency + "_redditSubscriber.csv")
##Scrape_redditMetrics(currencies);
