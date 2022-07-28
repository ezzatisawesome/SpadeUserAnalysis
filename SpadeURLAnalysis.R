# Load packages
pacman::p_load(pacman, mongolite)

sketch <- mongo(db='local', collection='sketches', url='mongodb://localhost:27017')
sketchData <- sketch$find('{}')

sketchData
