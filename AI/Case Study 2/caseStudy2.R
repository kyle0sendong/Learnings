# Load libraries
library(tidyverse) 
library(arules)
library(arulesViz)

# Read the data
readFile <- read.csv("primary-tumor.csv", stringsAsFactors=TRUE)

# Visualization for Data Analysis
ggplot(readFile, aes(x=age)) +
  geom_bar(stat="count") +
  labs(x="Age Group", y="Count") +
  geom_text(stat="count", aes(label=..count..), vjust = -1)

ggplot(readFile, aes(x=sex)) +
  geom_bar(stat="count") +
  labs(x="Sex Group", y="Count") +
  geom_text(stat="count", aes(label=..count..), vjust = -1)

ggplot(readFile, aes(x=histologic_type)) +
  geom_bar(stat="count") +
  labs(x="Histologic Type", y="Count") +
  geom_text(stat="count", aes(label=..count..), vjust = -1)

ggplot(readFile, aes(x=degree_of_diffe)) +
  geom_bar(stat="count") +
  labs(x="Degree of Difference", y="Count") +
  geom_text(stat="count", aes(label=..count..), vjust = -1)

ggplot(readFile, aes(x=class)) +
  geom_bar(stat="count") +
  labs(x="Classes", y="Count") +
  geom_text(stat="count", aes(label=..count..), vjust = -1)



#Creating Transactions
trans <- transactions(readFile)
trans

#selecting the class attribute for the RHS for mining.
aprioriRule <- apriori(trans, parameter = list(support = 0.05, confidence = 0.8, minlen = 2, maxlen=17),
                 appearance = list(rhs = c("class=lung"),default="lhs"))


#Removing Redundant Rules (nothing really happened)
aprioriRule <- aprioriRule[!is.redundant(aprioriRule)]

#Removing Insignificant Rule using fisher's algorithm
aprioriRule <- aprioriRule[!is.significant(aprioriRule, 
                                        tData, 
                                        method = "fisher", 
                                        adjust = 'bonferroni')]

aprioriRule

#Graph method is the only method used because it is easier to interpret
#Use lift as sorting
plot(head(aprioriRule, by = "lift", n = 100), method = "graph")


