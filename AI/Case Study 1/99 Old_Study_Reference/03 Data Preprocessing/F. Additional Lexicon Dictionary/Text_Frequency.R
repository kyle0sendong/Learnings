library(dplyr)

#Enter file name for input and output
inputFile <- "SAMPLE.csv"

readFile <- read.csv(inputFile)

#Combine unnest tweets into single document
readFile <- readFile %>% unnest_tokens(word, tweet)

#Count words and arrange based on number of frequency
frequency_dataframe = readFile %>% count(word) %>% arrange(desc(n))
options(max.print=7000)#Increase amount of result printed
frequency_dataframe #Print result

  