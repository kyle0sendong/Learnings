library(tm)
library(tidytext)

#set directory
getwd()

#import csv file
tweets <- read.csv(file.choose(), stringsAsFactors = FALSE)
review <- as.character(tweets$tweet)

#build corpus
corpus <- iconv(tweets$tweet, to = "utf-8")
corpus <- Corpus(VectorSource(corpus))

custom_lexicon <- read.csv("custom_dictionary.csv")
dictionary <- get_sentiments("bing")
dictionary %>% inner_join(custom_lexicon)

dictionary %>% 
  filter(sentiment %in% c("positive", "negative")) %>% 
  count(sentiment)

#Sentiment Analysis 
#Lexicon-based Approach
#obtain sentiment scores
s <- get_nrc_sentiment(review)

#combine text and sentiment column
review_sentiment<-cbind(tweets$tweet,s)
table(review_sentiment["positive"])
table(review_sentiment["negative"])

#Analyze sentiments using the syuzhet package based on the NRC sentiment dictionary
emotions <- get_nrc_sentiment(tweets$tweet)
emo_bar <- colSums(emotions)
emo_sum <- data.frame(count=emo_bar, emotions=names(emo_bar))

#Plot the count of words associated with 8 emotions, expressed as a percentage
barplot(
  sort(colSums(prop.table(s[, 1:8]))), 
  horiz = TRUE, 
  cex.names = 0.7, 
  las = 1, 
  main = "Emotion in Text (Leni)", xlab="Percentage"
)

#Plot the count of words associated with each sentiment, expressed as a percentage
barplot(
  sort(colSums(prop.table(s[, 9:10]))),
  horiz = TRUE, 
  cex.names = 0.7, 
  las = 1, 
  col = rainbow(5),
  main ="Leni", xlab="Percentage")



