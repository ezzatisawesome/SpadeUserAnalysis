# Load packages
pacman::p_load(pacman, mongolite)

users <- mongo(db='local', collection='users', url='mongodb://localhost:27017')
userData <- users$find('{}')

writingData <- userData$writing
textData <- userData$text
highlightData <- userData$highlight
penData <- userData$pen
drawData <- userData$draw
rectangleData <- userData$rectangle
triangleData <- userData$triangle
ellipseData <- userData$ellipse

pdfData <- lengths(userData$pdf)
downloadData <- userData$download
shareData <- userData$share

summary(writingData)
summary(textData)
summary(highlightData)
summary(penData)
summary(drawData)
summary(rectangleData)
summary(triangleData)
summary(ellipseData)

summary(pdfData)
summary(downloadData)
summary(shareData)


sketches <- mongo(db='local', collection='sketches', url='mongodb://localhost:27017')
sketchesData <- lengths(sketches$find('{}'))
summary(sketchesData)



