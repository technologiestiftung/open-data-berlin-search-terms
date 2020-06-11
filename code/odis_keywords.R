# Load libraries
library(jsonlite)
library(dplyr)
library(magrittr) 
library(corpus)
library(purrr)
library(tidyr)
library(data.table)

# Import JSON dataset
json_file <- fromJSON("/Users/evelynebrie/Dropbox/CityLab/ODIS/daten_berlin_de.searchterms.json")

# Convert to list
list_json <- map_if(json_file, is.data.frame, list) 

# Extract search terms
searchTerms <- list_json$stats$months$`2020-05`$terms

# Unlist search terms
unl_searchTerms <- as.data.frame(unlist(searchTerms))

# Split search terms
split_searchTerms <-as.data.frame(split(unl_searchTerms, 1:4))

# Create a data frame
df <- tibble::rownames_to_column(split_searchTerms, "term")

# Remove unwanted characters
df$term <- gsub(".impressions","",df$term)

# Remname columns
colnames(df) <- c("term","impressions","visits","page_duration_avg","exit_rate")

# Remove unnecessary datasets
rm(json_file,list_json,searchTerms,split_searchTerms,unl_searchTerms)

# Remove punctuation and convert terms to lowercase
df$term <- gsub('[[:punct:] ]+',' ',df$term)
df$term <- tolower(df$term)

# Stem strings (Geman)
df$term_stem <- NA
df$term_stem <- text_tokens(df$term, stemmer = "de")  
df$term_stem <- as.character(df$term_stem)

# Unlist search terms
df$term_stem <- unlist(df$term_stem)

# Create a copy of the dataset
clean_df <- df

# Set DT
setDT(clean_df)

# Merge all identical terms (sum)
clean_df = clean_df[ , .(impressions = sum(impressions), visits=sum(visits)), by = .(term_stem)]

# Remove punctuation
clean_df$term_stem <- gsub("^c\\(|\\)$", "", clean_df$term_stem)
clean_df$term_stem <- gsub('[[:punct:] ]+',' ',clean_df$term_stem)

# Trim white space
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
clean_df$term_stem <- trim(clean_df$term_stem)

# Calculate number of merged terms
dim(df)[1]-dim(clean_df)[1]

# Export .csv file
write.csv(clean_df,"/Users/evelynebrie/Dropbox/CityLab/ODIS/clean_terms.csv")
