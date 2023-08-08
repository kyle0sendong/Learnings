library(tm)

removeStopWords <- function(tweet) {
  
  cleanTweet <- tweet
  
  cleanTweet <- VectorSource(cleanTweet)
  cleanTweet <- VCorpus(cleanTweet)
  
  #remove extra numbers before stop words removal
  cleanTweet <- tm_map(cleanTweet, removeNumbers)
  
  #remove english stop words
  cleanTweet <- tm_map(cleanTweet, removeWords, stopwords("english"))
  
  #Read custom filipino stop words
  stopwords <- read.csv("Stopwords.csv", header = FALSE)
  stopwords <- as.character(stopwords$V1)
  stopwords <- c(stopwords, stopwords())
  
  #remove custom filipino stop words
  cleanTweet <- tm_map(cleanTweet, removeWords, stopwords)
  
  #https://stackoverflow.com/questions/38710286/how-to-save-tm-map-output-to-csv-file
  #Convert vector corpus to data frame
  cleanTweet<-data.frame(text=unlist(sapply(cleanTweet, `[`, "content")), stringsAsFactors=F)
  
  return(cleanTweet)
}

tweetCleaner <- function(tweet) { #remove any extra noise after stop words removal
  cleanTweet <- tweet
  
  #remove single letters
  cleanTweet <- gsub(pattern="\\b[A-z]\\b{1}", replace=" ", cleanTweet)
  
  #Remove laughs such as Lololol or hahaha patterns
  cleanTweet <- gsub("\\b(?:a*(?:ha)+h?|(?:l+o+)+l+)\\b", " ", cleanTweet)
  cleanTweet <- gsub("\\b(a*ha+h[ha]*|o?l+o+l+[ol]*)\\b", " ", cleanTweet)
  
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
inputFile <- "isko.csv"
outputFile <- "isko.csv"

readFile <- read.csv(inputFile)
readFile <- removeStopWords(readFile$tweet)
readFile <- tweetCleaner(readFile$text)
newDataFrame <- createDataFrame(readFile)

#Removing tweets containing single string/word
newDataFrame <- newDataFrame[which(sapply(strsplit(newDataFrame$tweet, split = " "), length)>=2), ]
newDataFrame <- createDataFrame(newDataFrame)

#Removing empty tweets and creating new clean data frame
newDataFrame <- newDataFrame[!(is.na(newDataFrame$tweet) | newDataFrame$tweet==""),]
newDataFrame <- createDataFrame(newDataFrame)
write.csv(newDataFrame, outputFile)

#there are better ways to code this part of removing empty tweets
#This is creating newDataFrame is taking too much resources






