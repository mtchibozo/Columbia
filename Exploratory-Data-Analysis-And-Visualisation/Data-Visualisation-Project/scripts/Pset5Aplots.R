library(tidyverse)
df <- read.csv(file = 'Desktop/superhero_movie_dataframe.csv', sep = ",")
gross_year <- select(df, release_date, gross_usa)

years <- strsplit(as.character(gross_year$release_date),' ')
years <- do.call(rbind, years)
years <- years[,4]
years <- as.numeric(years)

gross_year <- data.frame(release_date = years, gross_usa = gross_year$gross_usa)
gross_year[55,]['release_date'] <- 1954
gross_year

results <- data.frame(gross_year %>%
  group_by(release_date) %>%
  summarise(total_gross_usa = sum(gross_usa, na.rm = TRUE)))

results <- results[order(results['release_date']),]

ggplot(results, aes(release_date, y=total_gross_usa)) + 
  geom_line() +
  geom_point() +
  ggtitle("Total gross in USA over the years") +
  xlab("Year") + 
  ylab("Gross in USA")

ggplot(gross_year, aes(release_date)) + 
  geom_bar() + 
  ggtitle("Volume of movies over the years") +
  xlab("Year") + 
  ylab("Volume of movies")
