library(tidyverse)    

clean_tweets <- function(dataFrame) {
    cleanTweet <- dataFrame$tweet
    # Remove URLs
    cleanTweet <- str_remove_all(cleanTweet, " ?(f|ht)(tp)(s?)(://)(.*)[.|/](.*)")
    
    # Remove mentions
    cleanTweet <- str_remove_all(cleanTweet, "@[[:alnum:]_]{4,}")
    
    # Remove hashtags
    cleanTweet <- str_remove_all(cleanTweet, "#[[:alnum:]_]+")
    
    # Remove punctuation
    cleanTweet <- str_remove_all(cleanTweet, "[[:punct:]]")
    
    # Remove RT: 
    cleanTweet <- str_remove_all(cleanTweet, "^RT:? ")
    
    # Replace newline characters with a space
    cleanTweet <- str_replace_all(cleanTweet, "\\\n", " ")
    
    # convert to Lowercase
    cleanTweet <- str_to_lower(cleanTweet)
    
    # Remove any trailing whitespace around the text
    #str_trim(tweet$tweet, "both")
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
write.csv(newLeni,"leni.csv")

newBBM <- newDataFrame(bbm, clean_tweets(bbm))
write.csv(newBBM,"bbm.csv")

newIsko <- newDataFrame(isko, clean_tweets(isko))
write.csv(newIsko,"isko.csv")

newLacson <- newDataFrame(lacson, clean_tweets(lacson))
write.csv(newLacson,"lacson.csv")

newManny <- newDataFrame(manny, clean_tweets(manny))
write.csv(newManny,"manny.csv")



