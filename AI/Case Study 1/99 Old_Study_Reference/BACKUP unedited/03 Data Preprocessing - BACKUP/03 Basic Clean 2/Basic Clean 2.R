library(tidyverse)    
library(stringi)

clean_tweets <- function(dataFrame) {
    cleanTweet <- dataFrame$tweet


    #Remove extra white space
    cleanTweet <- gsub("\\s+", " ", cleanTweet)
    
    #Remove unicode characters (emoji)
    cleanTweet <- gsub("[<].*[>]", "", cleanTweet)
    
    #Remove any symbols left
    cleanTweet <- str_replace_all(cleanTweet, "[^[:alnum:]]", " ")
    
    #Remove leading and trailing white space
    cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
    
    #Non-ascii text conversion to preserve text
    cleanTweet <- stri_trans_general(cleanTweet, "latin-ascii")
    
    return(cleanTweet)
}


newDataFrame <- function(dataFrame, cleanTweet) {
  newDataFrame <- data.frame(date = c(dataFrame$date),
                             username = c(dataFrame$username),
                             tweet = c(cleanTweet),
                             hashtags = c(dataFrame$hashtags),
                             link = c(dataFrame$link))
  return(newDataFrame)
}

leni <- read.csv("leni.csv")
bbm <- read.csv("bbm.csv")
isko <- read.csv("isko.csv")
lacson <- read.csv("lacson.csv")
manny <- read.csv("manny.csv")


newLeni <- newDataFrame(leni, clean_tweets(leni))
newLeni <- newLeni[!(is.na(newLeni$tweet) | newLeni$tweet==""), ] #Removing empty tweets
write.csv(newLeni,"leni.csv")

newBBM <- newDataFrame(bbm, clean_tweets(bbm))
newBBM <- newBBM[!(is.na(newBBM$tweet) | newBBM$tweet==""), ] #Removing empty tweets
write.csv(newBBM,"bbm.csv")

newIsko <- newDataFrame(isko, clean_tweets(isko))
newIsko <- newIsko[!(is.na(newIsko$tweet) | newIsko$tweet==""), ] #Removing empty tweets
write.csv(newIsko,"isko.csv")

newLacson <- newDataFrame(lacson, clean_tweets(lacson))
newLacson <- newLacson[!(is.na(newLacson$tweet) | newLacson$tweet==""), ] #Removing empty tweets
write.csv(newLacson,"lacson.csv")

newManny <- newDataFrame(manny, clean_tweets(manny))
newManny <- newManny[!(is.na(newManny$tweet) | newManny$tweet==""), ] #Removing empty tweets
write.csv(newManny,"manny.csv")



