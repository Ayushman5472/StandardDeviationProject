import csv
import math

with open('data.csv') as d:
    reader = csv.reader(d)
    ProjectData = list(reader)

Numbers = []

for i in range((len(ProjectData))):
    tempVar = ProjectData[i][0]
    Numbers.append(float(tempVar))

n = len(Numbers)
total = 0
for numbers in Numbers:
    total = total + numbers

mean = total/n

StandardDev = []
print(ProjectData)  
for i in range((len(ProjectData))):
    tempVar = (float(ProjectData[i][0])-mean) ** 2
    StandardDev.append(float(tempVar))
sum = 0
for t in StandardDev:
    sum = sum + t

result = sum/(n)
StandardDev = math.sqrt(result)
print(StandardDev)