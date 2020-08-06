library(ggplot2)


df1 <- readRDS(file="/Users/SYTang/Desktop/CODE IN/events_past_year.rds") #Try to always specify the filepath if possible.

trim <- function (x) gsub("^\\s+|\\s+$", "", x) #gets rid of trailing whitespace to ensure no duplicate entries
df1$venue_city <- trim(df1$venue_city) 
df1$venue_country <- trim(df1$venue_country)

cities <- as.data.frame(table(tolower(df1$venue_city))) 
countries <- as.data.frame(table(tolower(df1$venue_country)))
groups <- as.data.frame(table(tolower(df1$group_name)))


cities
countries


groups2 <- head(groups[order(groups$Freq, decreasing= T),], n = 50)
groups2


graph1 <- ggplot(groups2, main = "Top 50 Most Frequent Groups" , aes(x=reorder(Var1, -Freq), y = Freq),las=2) + geom_bar(stat="identity") + theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5))
graph1 + xlab('Group Names') + ylab('Number of Events')




