setwd("~/Dropbox/AP_NIGHT/data")

library(plyr)
library(reshape)
head(data)
data <- read.csv('data.csv',header=T)
n <- cast(data,key~date)


## get the percentages
colnames(data)[3] <- 'total'
colnames(data)[4] <- 'value'
percent <- cast(data,key~date)
percent[is.na(percent)==T] <- 0

write.table(percent,'data_new.csv',col.names=T,row.names=F,sep=',')