library(tidyverse)    

#First stage of cleaning

tweetCleaner <- function(tweet) {
    cleanTweet <- tweet
    
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

    return(cleanTweet)
}


#Only preserve 'tweet' attribute
createDataFrame <- function(cleanTweet) {
  newDataFrame <- data.frame(tweet = c(cleanTweet))
  return(newDataFrame)
}

#Edit what file is to be cleaned
inputFile <- "sample.csv"
outputFile <- "sameple_o.csv"

readFile <- read.csv(inputFile)
cleanTweet <- tweetCleaner(readFile$tweet)
newDataFrame <- createDataFrame(cleanTweet)
write.csv(newDataFrame, outputFile)









