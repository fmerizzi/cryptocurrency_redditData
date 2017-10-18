import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
import Scrape_RedditMetrics as scrape
import Download_prices as price
import Constants as cons

#recall Downloads
scrape.Scrape_redditMetrics(cons.currencies);
price.download_price(cons.currencies);

## For declaration
for currency in cons.currencies :
    ## Constants

    reddit_file = cons.directory + currency + "_redditGrowth.csv"
    price_file =  cons.directory + currency + "price.csv"

    ## Plotting first Figure
    plt.figure(1,figsize=(20,10))

    ax1 = plt.subplot(211)
    y = np.loadtxt(reddit_file,unpack=True,delimiter = ",",usecols = 2,dtype = str,skiprows= 1)
    z = np.loadtxt(reddit_file,unpack=True,delimiter = ",",usecols = 1,dtype = float,skiprows= 1)
    x = [y for y in range(len(y))]
    for i in range(len(x)):
        x[i] = datetime.strptime(y[i], "b'%Y-%m-%d'")
    dates = matplotlib.dates.date2num(x)
    matplotlib.pyplot.plot_date(dates, z, ls='solid', marker=",",label=currency + " reddit growth")
    matplotlib.pyplot.legend()

    ## Plotting Second Figure


    l = np.loadtxt(price_file,unpack=True,delimiter = ",",usecols = 0,dtype = str,skiprows= 1)
    q = np.loadtxt(price_file,unpack=True,delimiter = ",",usecols = 1,dtype = float,skiprows= 1)
    n = [l for l in range(len(l))]
    for i in range(len(n)):
        n[i] = datetime.strptime(l[i], "b'%Y-%m-%d %H:%M:%S UTC'")
    dates3 = matplotlib.dates.date2num(n)
    plt.subplot(212, sharex = ax1)
    dates3 = matplotlib.dates.date2num(n)
    matplotlib.pyplot.plot_date(dates3, q, ls = 'solid',marker = ",", color = "red",label=currency + " price")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    matplotlib.pyplot.show()
