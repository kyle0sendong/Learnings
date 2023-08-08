library(tm)

stem <- function(tweet) {
  
  cleanTweet <- tweet
  cleanTweet <- VectorSource(cleanTweet)
  cleanTweet <- VCorpus(cleanTweet)
  
  #stem document using porter stem algorithm
  cleanTweet <- tm_map(cleanTweet, stemDocument)
  
  #https://stackoverflow.com/questions/38710286/how-to-save-tm-map-output-to-csv-file
  #Convert vector corpus to data frame
  cleanTweet<-data.frame(text=unlist(sapply(cleanTweet, `[`, "content")), stringsAsFactors=F)
  
  return(cleanTweet)
}

tweetCleaner <- function(tweet) { #remove any extra noise after stemming
  cleanTweet <- tweet
  
  #remove single letters
  cleanTweet <- gsub(pattern="\\b[A-z]\\b{1}", replace=" ", cleanTweet)
  
  #Remove extra white space
  cleanTweet <- gsub("\\s+", " ", cleanTweet)
  
  #Remove leading and trailing white space
  cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
  
  return(cleanTweet)
}

createDataFrame <- function(cleanTweet) {
  newDataFrame <- data.frame(tweet = c(cleanTweet))
  return(newDataFrame)
}

#Enter file name for input and output
inputFile <- "sample.csv"
outputFile <- "sample.o.csv"

readFile <- read.csv(inputFile)
readFile <- stem(readFile$tweet)
readFile <- tweetCleaner(readFile$text)
newDataFrame <- createDataFrame(readFile)
#Removing empty tweets and creating new clean data frame
newDataFrame <- newDataFrame[!(is.na(newDataFrame$tweet) | newDataFrame$tweet==""),]
newDataFrame <- createDataFrame(newDataFrame)
write.csv(newDataFrame, outputFile)

#there are better ways to code this part of removing empty tweets
#This is creating newDataFrame is taking too much resources






