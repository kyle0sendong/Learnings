library(tm)
library(SnowballC)
stem <- function(tweet, sentiment) {
  
  cleanTweet <- tweet
  cleanSentiment <- sentiment

  cleanTweet <- VectorSource(cleanTweet)
  cleanTweet <- VCorpus(cleanTweet)
  
  #stem document using porter stem algorithm
  cleanTweet <- tm_map(cleanTweet, stemDocument)
  
  #https://stackoverflow.com/questions/38710286/how-to-save-tm-map-output-to-csv-file
  #Convert vector corpus to data frame
  cleanTweet<-data.frame(text=unlist(sapply(cleanTweet, `[`, "content")), stringsAsFactors=F)
  
  cleanTweet <- data.frame(tweet = c(cleanTweet$text),
                           sentiment = c(cleanSentiment))
  return(cleanTweet)
}

tweetCleaner <- function(tweet, sentiment) { #remove any extra noise after stemming
  
  cleanTweet <- tweet
  cleanSentiment <- sentiment
  
  #remove single letters
  cleanTweet <- gsub(pattern="\\b[A-z]\\b{1}", replace=" ", cleanTweet)
  
  #Remove extra white space
  cleanTweet <- gsub("\\s+", " ", cleanTweet)
  
  #Remove leading and trailing white space
  cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
  
  cleanTweet <- data.frame(tweet = c(cleanTweet),
                           sentiment = c(cleanSentiment))
  #Remove empty rows
  cleanTweet <- cleanTweet[!(is.na(cleanTweet$tweet) | cleanTweet$tweet==""),]
  cleanTweet
  return(cleanTweet)
}

createDataFrame <- function(tweet, sentiment) {
  newDataFrame <- data.frame(tweet = c(tweet),
                             sentiment = c(sentiment))
  return(newDataFrame)
}

#Enter file name for input and output
inputFile <- "input.csv"
outputFile <- "output.csv"

readFile <- read.csv(inputFile)

tweet <- readFile$tweet
sentiment <- readFile$sentiment

readFile <- stem(tweet,sentiment)

tweet <- readFile$tweet
sentiment <- readFile$sentiment

readFile <- tweetCleaner(tweet,sentiment)

tweet <- readFile$tweet
sentiment <- readFile$sentiment

newDataFrame <- createDataFrame(tweet, sentiment)
#Removing empty tweets and creating new clean data frame
newDataFrame <- newDataFrame[!(is.na(newDataFrame$tweet) | newDataFrame$tweet==""),]
colnames(newDataFrame) <- c('tweet','sentiment')
write.csv(newDataFrame, outputFile)




