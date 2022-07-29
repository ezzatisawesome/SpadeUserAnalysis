import json

# Import file
f = open('classificationData.json')
data = json.load(f)

cleanedData = []
for d in data:
    domain = d.get('domain')
    if domain is not None:
        domain_url = domain.get('domain_url')
        if domain_url != 'https://spade.tools/tutorial' and domain_url != 'https://spade.tools/':
            cleanedData.append(d)
    else:
        cleanedData.append(d)

categoriesData = {}
for c in cleanedData:
    domain = c.get('domain')
    if domain is not None:
        domainName = domain['categories'][0]['name']
        if categoriesData.get(domainName) is None:
            categoriesData[domainName] = 1
        else:
            categoriesData[domainName] += 1

print(categoriesData)

with open("summary.json", "w") as outfile:
    outfile.write(json.dumps(categoriesData))

# Closing file
f.close()