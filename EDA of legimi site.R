#This file includes basic EDA of obtained results

setwd('C:\\Users\\maria\\Desktop\\projektLegimi')

# data <- read.csv('kryminały_result01.csv')
# 
# head(data)
# data <- data[,-c(6)]
# colnames(data)[10]<-'peopleInterested'
# 
# write.csv(data,"kryminały_result02.csv", row.names = FALSE)

data <- read.csv('kryminały_resultBS.csv', encoding = 'UTF-8')
data <- data[,-c(1)]

library(stringr)

data$score<-as.numeric(str_replace(data$score, ",", "."))
data$ebookPrice<-as.numeric(str_replace(data$ebookPrice, ",", "."))
data$audiobookPrice<-as.numeric(str_replace(data$audiobookPrice, ",", "."))
data$paperPrice<-as.numeric(str_replace(data$paperPrice, ",", "."))

data.sorted<-data[order(-data$peopleInterested),]
hist(data.sorted[1:20,])


data.sorted$author<-as.factor(data.sorted$author)

#library(ggplot2)
#ggplot(data.sorted[1:20,],aes(x=peopleInterested))+geom_histogram(binwidth = 5)+facet_grid(~author)+theme_bw()

data.sorted$X<-1 #temp for counting
t1<- aggregate(data.sorted[1:20,]$X, by=list(author=data.sorted[1:20,]$author), FUN=sum)
t1<-t1[order(-t1$x),]
library(RColorBrewer)
colis <- brewer.pal(8, "Spectral") 
pie(t1$x, t1$author, main = 'Authors of the 20 most popular books', 
    col = colis, clockwise = T, radius = 1.05)

plot(density(data$paperPrice, na.rm=T), xlim=c(0,105), ylim=c(0,0.15), 
     col = 'turquoise3', xlab = 'Price', lwd = 2,
     main = ('Price distribution for different book types'))
lines(density(data$audiobookPrice, na.rm=T), col = 'steelblue3', lwd = 2)
lines(density(data$ebookPrice, na.rm=T), col = 'thistle', lwd = 2)
legend('topright', legend=c("Paper book", "Audiobook", "Ebook"),
       col=c("turquoise3", "steelblue3", "thistle"), lty=1, lwd = 2, cex=0.8)

plot(density(data.sorted$peopleInterested, na.rm=T), xlim = c(0,600),
     main = 'Distribution of a book popularity', col = 'seagreen3', lwd=2,
     xlab = 'How many people are interested in a book')
