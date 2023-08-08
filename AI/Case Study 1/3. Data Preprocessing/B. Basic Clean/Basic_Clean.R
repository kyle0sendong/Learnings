library(tidyverse)    
library(stringi)


tweetCleaner <- function(tweet, sentiment) {
    
    cleanTweet <- tweet
    cleanSentiment <- sentiment
    
    #First Sequence of cleaning
    # Remove URLs
    cleanTweet <- str_remove_all(cleanTweet, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)")
    
    # Remove mentions
    cleanTweet <- str_remove_all(cleanTweet, "@[[:alnum:]_]{4,}")
    
    # Remove Hashtags
    cleanTweet <- str_remove_all(cleanTweet, "#[[:alnum:]_]+")
    
    # Remove punctuation
    cleanTweet <- str_remove_all(cleanTweet, "[[:punct:]]")
    
    # Remove Retweets RT:
    cleanTweet <- str_remove_all(cleanTweet, "^RT:? ")
    
    # Replace newline characters with a space
    cleanTweet <- str_replace_all(cleanTweet, "\\\n", " ")
    
    # Convert to Lowercase
    cleanTweet <- str_to_lower(cleanTweet)
    
    # Remove repeated Characters occuring more than 2 times
    cleanTweet <- gsub("(.)\\1{2,}", "\\1", cleanTweet)
    
    
    #Second Sequence of Cleaning
    #Remove unicode characters (emojis <U+*> pattern )
    cleanTweet <- gsub("[<].*[>]", "", cleanTweet)
    
    #Non-ascii text conversion to preserve text
    cleanTweet <- stri_trans_general(cleanTweet, "latin-ascii")
    
    #Remove any alphanumeric symbols left
    cleanTweet <- str_replace_all(cleanTweet, "[^[:alnum:]]", " ")
    
    #Remove leading and trailing white space
    cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
    
    #Remove extra white space
    cleanTweet <- gsub("\\s+", " ", cleanTweet)
    
    #Create new dataframe, tweet as header to remove empty rows
    cleanTweet <- data.frame(tweet = c(cleanTweet),
                             sentiment = c(cleanSentiment))
    #Remove empty rows
    cleanTweet <- cleanTweet[!(is.na(cleanTweet$tweet) | cleanTweet$tweet==""),]

    return(cleanTweet)
}


#Only preserve 'tweet' attribute
createDataFrame <- function(cleanTweet) {
  newDataFrame <- data.frame(tweet = c(cleanTweet))
  return(newDataFrame)
}

#Edit what file is to be cleaned
inputFile <- "whole.csv"
outputFile <- "asd.csv"

readFile <- read.csv(inputFile)
tweets <- readFile

tweet <- tweets$tweet
sentiment <- tweets$sentiment

cleanTweet <- tweetCleaner(tweet, sentiment)
newDataFrame <- createDataFrame(cleanTweet)

write.csv(newDataFrame, outputFile)









