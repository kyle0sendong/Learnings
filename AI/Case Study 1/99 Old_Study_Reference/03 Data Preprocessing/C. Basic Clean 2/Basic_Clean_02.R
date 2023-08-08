library(tidyverse)    
library(stringi)

tweetCleaner <- function(tweet) {
    cleanTweet <- tweet
    
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
    
    return(cleanTweet)
}

#Only preserve 'tweet' attribute
createDataFrame <- function(cleanTweet) {
  newDataFrame <- data.frame(tweet = c(cleanTweet))
  return(newDataFrame)
}

#Enter file name for input and output
inputFile <- "sample.csv"
outputFile <- "sample.o.csv"

readFile <- read.csv(inputFile)
cleanTweet <- tweetCleaner(readFile$tweet)
newDataFrame <- createDataFrame(cleanTweet)
#Removing empty tweets and creating new clean data frame
newDataFrame <- newDataFrame[!(is.na(newDataFrame$tweet) | newDataFrame$tweet==""),]
newDataFrame <- createDataFrame(newDataFrame)
write.csv(newDataFrame, outputFile)

#there are better ways to code this part of removing empty tweets
#This is creating newDataFrame is taking too much resources





