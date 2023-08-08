library("tm")

removeStopWords <- function(tweet) {
  
    cleanTweet <- tweet
    
    cleanTweet <- VectorSource(cleanTweet)
    cleanTweet <- VCorpus(cleanTweet)

    stopwords <- read.csv("stopwords.csv", header = FALSE)
    stopwords <- as.character(stopwords$V1)
    stopwords <- c(stopwords, stopwords())
    
    #remove numbers
    cleanTweet <- tm_map(cleanTweet, removeNumbers)
    
    #remove stop words
    cleanTweet <- tm_map(cleanTweet, removeWords, stopwords("english"))
    
    #remove filipino stop words
    cleanTweet <- tm_map(cleanTweet, removeWords, stopwords)
    
    #https://stackoverflow.com/questions/38710286/how-to-save-tm-map-output-to-csv-file
    cleanTweet<-data.frame(text=unlist(sapply(cleanTweet, `[`, "content")), stringsAsFactors=F)
    
    return(cleanTweet)
}

clean_tweets <- function(tweet) {
  cleanTweet <- tweet
  
  #remove single letters
  cleanTweet <- gsub(pattern="\\b[A-z]\\b{1}", replace=" ", cleanTweet)
  
  #Remove extra white space
  cleanTweet <- gsub("\\s+", " ", cleanTweet)
  
  #Remove leading and trailing white space
  cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
  
  return(cleanTweet)
}

newDataFrame <- function(dataFrame, cleanTweet) {
  newDataFrame <- data.frame(tweet = c(cleanTweet))
  return(newDataFrame)
}


leni <- read.csv("leni.csv")
bbm <- read.csv("bbm.csv")
isko <- read.csv("isko.csv")
lacson <- read.csv("lacson.csv")
manny <- read.csv("manny.csv")

leni <- newDataFrame(leni, removeStopWords(leni$tweet))
newLeni <- newDataFrame(leni, clean_tweets(leni$text))
newLeni <- newLeni[!(is.na(newLeni$tweet) | newLeni$tweet==""), ] #Removing empty tweets
write.csv(newLeni,"leni.csv")

bbm <- newDataFrame(bbm, removeStopWords(bbm$tweet))
newBBM <- newDataFrame(bbm, clean_tweets(bbm$text))
newBBM <- newBBM[!(is.na(newBBM$tweet) | newBBM$tweet==""), ] #Removing empty tweets
write.csv(newBBM,"bbm.csv")

lacson <- newDataFrame(lacson, removeStopWords(lacson$tweet))
newLacson <- newDataFrame(lacson, clean_tweets(lacson$text))
newLacson <- newLacson[!(is.na(newLacson$tweet) | newLacson$tweet==""), ] #Removing empty tweets
write.csv(newLacson,"lacson.csv")

isko <- newDataFrame(isko, removeStopWords(isko$tweet))
newIsko <- newDataFrame(isko, clean_tweets(isko$text))
newIsko <- newIsko[!(is.na(newIsko$tweet) | newIsko$tweet==""), ] #Removing empty tweets
write.csv(newIsko,"isko.csv")

manny <- newDataFrame(manny, removeStopWords(manny$tweet))
newManny <- newDataFrame(manny, clean_tweets(manny$text))
newManny <- newManny[!(is.na(newManny$tweet) | newManny$tweet==""), ] #Removing empty tweets
write.csv(newManny,"manny.csv")



