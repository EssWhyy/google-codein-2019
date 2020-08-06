library(ggplot2)

events2018 <- 0
events2019 <- 0

df1 <- readRDS(file="/Users/SYTang/Desktop/CODE IN/events_past_year.rds") #Try to always specify the filepath if possible.
years <- format(as.Date(df1$local_date, format="%Y/%m/%d"),"%Y") #Formats the values in teh cells as a date and returns the years.

length(years) #4302 elements counted

#counts the number of events in 2018 and 2019.
for (i in 1:4302){
  if (years[i] == "2018"){
    events2018 = events2018 + 1
    
  }
  else{
    events2019 = events2019 + 1
    
  }
  
}
  
print(events2018) #1615
print(events2019) #2687

piechart.df <- data.frame(
year = c('2018', '2019'),
eventcount = c(1615, 2687)
 )

bp<- ggplot(piechart.df, aes(x="", y=eventcount, fill=year))+
  geom_bar(width = 1, stat = "identity") #Square shaped fill graph

eventpie <- bp + coord_polar("y", start=0) #Changes it into a pie
eventpie


#counts the number of events monthly, from Aug 2018, till present.
months <- as.data.frame(table(format(as.Date(df1$local_date, format="%Y/%m/%d"),"%Y/%m")))
print(months)
ggplot(months, aes(x=Var1, y=Freq)) + geom_bar(stat="identity")




