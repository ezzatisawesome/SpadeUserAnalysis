# Load packages
pacman::p_load(pacman, jsonlite)

# Main
data <- read_json(path = '~/Documents/SpadeUserAnalysis/classificationData.json', simplifyVector = TRUE)
cleanData <- data[!(data$domain$domain_url=="https://spade.tools/tutorial" | data$domain$domain_url=="https://spade.tools/"),]
categoryData <- cleanData$domain$categories

data2 <- read_json(path = '~/Documents/SpadeUserAnalysis/summary.json', simplifyVector = TRUE)
data2
