library(tm)

removeStopWords <- function(tweet, sentiment) {
  
  cleanTweet <- tweet
  cleanSentiment <- sentiment
  
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
  
  cleanTweet
  #https://stackoverflow.com/questions/38710286/how-to-save-tm-map-output-to-csv-file
  #Convert vector corpus to data frame
  cleanTweet<-data.frame(text=unlist(sapply(cleanTweet, `[`, "content")), stringsAsFactors=F)
  cleanTweet$text
  #cop the sentiments
  cleanTweet <- data.frame(tweet = c(cleanTweet$text),
                           sentiment = c(cleanSentiment))
  return(cleanTweet)
}

#Final Cleaning 

tweetCleaner <- function(tweet, sentiment) {
  
  cleanTweet <- tweet
  cleanSentiment <- sentiment
  
  #remove single letters
  cleanTweet <- gsub(pattern="\\b[A-z]\\b{1}", replace=" ", cleanTweet)
  
  #Remove laughs such as Lololol or hahaha patterns
  cleanTweet <- gsub("\\b(?:a*(?:ha)+h?|(?:l+o+)+l+)\\b", " ", cleanTweet)
  cleanTweet <- gsub("\\b(a*ha+h[ha]*|o?l+o+l+[ol]*)\\b", " ", cleanTweet)
  
  #Remove extra white space
  cleanTweet <- gsub("\\s+", " ", cleanTweet)
  
  #Remove leading and trailing white space
  cleanTweet <- gsub("^\\s+|\\s+$", "", cleanTweet)
  
  #Create new dataframe, tweet as header to remove empty rows
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
inputFile <- "clean.csv"
outputFile <- "a.csv"

readFile <- read.csv(inputFile)


tweet <- readFile$tweet
sentiment <- readFile$sentiment

readFile <- removeStopWords(tweet, sentiment)

tweet <- readFile$tweet
sentiment <- readFile$sentiment


readFile <- tweetCleaner(tweet, sentiment)

tweet <- readFile$tweet
sentiment <- readFile$sentiment

newDataFrame <- createDataFrame(tweet, sentiment)

#Removing tweets containing single string/word
newDataFrame <- newDataFrame[which(sapply(strsplit(newDataFrame$tweet, split = " "), length)>=2), ]
colnames(newDataFrame) <- c('tweet','sentiment')

#Removing empty tweets
newDataFrame <- newDataFrame[!(is.na(newDataFrame$tweet) | newDataFrame$tweet==""),]
colnames(newDataFrame) <- c('tweet','sentiment')

newDataFrame
write.csv(newDataFrame, outputFile)






