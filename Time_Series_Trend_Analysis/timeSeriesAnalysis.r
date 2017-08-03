# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

library(stringr)
set.seed(10)

getwd()
#Read the day-wise checkin data which we created as part of preprocessing step. 
#It contains list for [#checkins on Mon, #checkins on Tue....,  #checkins on Sun] for each business

checkins<-read.csv('CheckinDaywise.csv',header= TRUE)

#Read the grouped business data which was again created as part of preprocessing step.
#In this file we have grouped each business into 32 broad business categories like Food services, Hospitality services, Bars and Lounges, Sports services etc.
business<-read.csv('businessGrouped.csv',header= TRUE)

#As part of this project we will be finding out trending places for the state of North Carolina, however model is highly scalable. 
businessNC<-business[business$state=='NC',]

#Extract cities of the state of NC
NCcities<-unique(businessNC$city)

#Out of 32 categories, we will be predecting trending businesses for below listed Business categories as they occupy major chunk of customer base. We can add 
#more business categories if needed at any point of time.
businessCategories<-c('Food services','Medical services','Hospitality services','sports services','Grooming services','Bars and lounges','Entertainment services',
                      'Shops, stores and markets','IT services','Pet services','Automobile parts and supplies','Legal services','Health and fitness services',
                      'Construction services','Clothing','Automobile dealers','handyman services')


#function to check if vector is empty, used later in the code
vector.is.empty <- function(x) return(length(x) ==0 )


dir.create(file.path(getwd(), 'NC'), showWarnings = FALSE)
currdir<-getwd()
setwd(file.path(getwd(), 'NC'))

for (city in NCcities){                                                                           #for each city in state of NC
    cityTrend<-read.csv(text="BID,name,slope,type")                                               #create an empty dataframe to store trending businesses for this city
    for (businessType in businessCategories){                                                     #for select business category in business category list.
      businesses<-businessNC[businessNC$city==city & businessNC$businesscategory==businessType,]  #Subset businesses DF to filter value for city and business category in hand.
      if (is.data.frame(businesses) && nrow(businesses)==0){                                      #if city have no businesses in selected business category, skip
        next
      }
      businessTrendDF<-read.csv(text="BID,name,slope,type")                                       #create an empty dataframe to store data for each business in
      for (i in 1:nrow(businesses)){                                                              #given city and in given business category
        row <- businesses[i,]                                                                     #read data for current business in hand
        ID=as.character(row$business_id)                                                          #extract business ID of that business
        name=as.character(row$name)                                                               #extract name of that business
        daywisecheckins<-as.character(checkins[checkins$business_id==ID,3])                       #read day-wise checkin data for that business
        if (vector.is.empty(daywisecheckins)){                                                    #if check-in data is not available for that business, skip
          next
        }
        re <- gregexpr("[0-9]+", daywisecheckins)                                                 #checkin data is in string form of python list '[11,33,44,1,3,4,5]'
        checkinVector<-as.numeric(unlist(regmatches(daywisecheckins, re)))                        #use regular expression to extract the check-in information
        checkinTS<-ts(checkinVector,frequency = 2)                                                #create a time series on check-in data
        decomp<-stl(checkinTS,s.window=2)                                                         #decompose the time series using STL
        decompSummary<-summary(decomp)
        trendComponent<-as.numeric(decompSummary$time.series[,2])                                 #extract the trend component from stl decomposition
        index<-c(1:7)                                                                             
        trend<-data.frame(index,trendComponent)                                                   #create a dataframe for trend component
        Lmodel<-lm(trendComponent~index, data=trend)                                              #fit linear model on the trend component of the time series
        LmodelSummary<-summary(Lmodel)
        model_slope <- LmodelSummary$coefficients[2,1]                                            #extract the slope of the trend
        if (model_slope<0){                                                                       #if the slope is negative it cannot be trending business, hence ignore
          next                                                                                      
        }
        newrow<-data.frame(BID=ID,name=name, slope=model_slope, type=businessType)                #add the businessID, name , slope of trend , business category to the df
        businessTrendDF = rbind(businessTrendDF,newrow)
      }
      top3<-head(businessTrendDF[order(businessTrendDF$slope, decreasing=TRUE), ], 3)             #pick the rows with top 3 trend's slope value, i.e the top 3 trending businesses 
      cityTrend<-rbind(cityTrend,top3)                                                            #for the current business category and append result to city's DF declared above.
    }
    
    write.csv(cityTrend, paste0("NC_trend_", city,".csv"), row.names=F)                           #write the result for each city to csv file.
}

setwd(currdir)
