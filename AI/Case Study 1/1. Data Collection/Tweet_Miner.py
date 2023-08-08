#Must install Twint and its dependencies. Instructions found in https://github.com/twintproject/twint

import twint

def scrapeTweet(searchTerms, limit, startDate, endDate, outputFile):
    for i in range(len(searchTerms)):
        c = twint.Config()
        c.Search = searchTerms[i]
        c.Limit = limit  #set limit
        c.Lang = "en"
        c.Since = startDate
        c.Until = endDate
        c.Store_csv = True
        c.Output = outputFile

        twint.run.Search(c)

searchTerms = ['sample']   #can include other filters -person -politician for annotated tweet 
outputFile = 'sample.csv' 
limit = 2000 #set limit per search term.
startDate = '2022-03-22 00:00:00' #set start date
endDate = '2022-03-25 23:59:59' #set end date

#Scraping tweet older than 2 weeks result to fewer scraped tweets.
scrapeTweet(searchTerms, limit, startDate, endDate, outputFile)
