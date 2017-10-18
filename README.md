# cryptocurrency_redditData
This Code is meant for automating the download of Crypto's subreddit growth data and Price, and also print a friendly comparison graph with matplotlib.

The data from reddit is retrieved with the request library from https://www.redditmetrics.com, downloaded and stored in a csv. 
The price csv is directly downloaded from https://www.coingecko.com/ for the desired currency.

For the program to run on other systems it is necessary to update the directories for saving the files, you can do that in the Constants.py file. 

For downloading other currencies you just have to add the name in the list of strings, also in the Constants.py file. For a currency to be added it has to be on coingecko and it must have a subreddit. You can use your own csv if you wish to. 

The Folder Data_Files contains examples of the downloaded csv

The Folder Print_Examples_jpg contains examples of the printed graphs, in jpg format 
