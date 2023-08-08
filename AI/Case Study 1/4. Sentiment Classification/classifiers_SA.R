library(textcat)
library(tm)



inputFile <- "input.csv"
tweet <- read.csv(inputFile)

corpus = VCorpus(VectorSource(tweet$tweet))

#Remove infrequent terms
library(caTools)
frequencies = DocumentTermMatrix(corpus)
sparse = removeSparseTerms(frequencies, 0.99) 

#Function
convert_count <- function(x) {
  y <- ifelse(x > 0, 1,0)
  y <- factor(y, levels=c(0,1), labels=c("No", "Yes"))
  y
}


datasetNB <- apply(sparse, 2, convert_count)
dataset = as.data.frame(as.matrix(datasetNB))

dataset$Class = tweet$sentiment
str(dataset$Class)
prop.table(table(dataset$Class))
dataset_convert = dim(dataset)[2]

#data split
set.seed(724318)
split = sample(2,nrow(dataset),prob = c(2/3, 1/3),replace = TRUE)
train_set = dataset[split == 1,]
test_set = dataset[split == 2,] 

train_set$Class = as.factor(train_set$Class)
test_set$Class = as.factor(test_set$Class)

prop.table(table(train_set$Class))
prop.table(table(test_set$Class)) #skewed to positive




#Model Training

#Cross Validation
library(caret)
control <- trainControl(method="repeatedcv",  
                        number=10,
                        repeats=3)


#1. Naive Bayes Classifier Model
library(e1071)
system.time(classifier_nb <- naiveBayes(train_set, 
                                        train_set$Class, 
                                        laplace = 1,
                                        confusionMatrix(pr5, reference = Zoo_test$type),
                                        tuneLength = 5))
#Predictor + Confusion Matrix
nb_pred = predict(classifier_nb, type = 'class', newdata = test_set)
confusionMatrix(table(nb_pred, test_set$Class))


#2. SVM Model
svm_classifier <- svm(Class~.,
                      data=train_set,
                      kernel="linear")
#Predictor + Confusion Matrix
svm_pred = predict(svm_classifier, test_set)
confusionMatrix(table(svm_pred, test_set$Class))

#3. Random Forest Classifier Model
library(randomForest)
rf_classifier = randomForest(x = train_set[-dataset_convert],
                             y = train_set$Class,
                             trControl = control,
                             tuneLength = 5,
                             ntree = 300)
#Predictor + Confusion Matrix
rf_pred = predict(rf_classifier, newdata = test_set[-dataset_convert])
confusionMatrix(table(rf_pred, test_set$Class))



#4. Decision Tree Model using CART
#URL https://www.kaggle.com/code/suzanaiacob/sentiment-analysis-of-the-yelp-reviews-data#Exploratory-Data-Analysis
#Uses different data frame and splitting of data
library(rpart)
library(rpart.plot)
tweet$positive = as.factor(tweet$sentiment == "positive")
corpus = VCorpus(VectorSource(tweet$text))
cart_sparse = as.data.frame(as.matrix(sparse))
colnames(cart_sparse) = make.names(colnames(cart_sparse))
cart_sparse$positive = tweet$positive

#Splitting of data
set.seed(72141)
split = sample.split(cart_sparse$positive, SplitRatio = 2/3)
cart_sparse$split = split
train_set1 = subset(cart_sparse, split==TRUE)
test_set1 = subset(cart_sparse, split==FALSE)

#Decision Tree CART Improved Model
cpGrid = expand.grid(.cp=seq(0.001, 0.01, 0.001))

train(positive ~ ., 
      data = train_set1, 
      method = "rpart", 
      trControl = control, 
      tuneGrid = cpGrid)

cart_predictor = rpart(positive ~ ., 
                       data=train_set1, 
                       method="class", 
                       cp= 0.001)
prp(cart_predictor)

#Predictor + Confusion Matrix
cart_predictor = predict(cart_predictor, newdata=test_set1, type="class")
confusionMatrix(table(cart_predictor, test_set1$positive))

















