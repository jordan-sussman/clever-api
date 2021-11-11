import requests
from requests.structures import CaseInsensitiveDict

# Request variables
url = "https://api.clever.com/v3.0/sections"
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer DEMO_TOKEN"
# Request
resp = requests.get(url, headers=headers)
# Response as JSON
cleverData = resp.json()

# Iterating over section data (cleverData) to grab only a list of students from each section (students)
students = []
for x in cleverData['data']:
    students.append(x['data']['students'])

# Iterating over student section totals (students) to append them into one object (sectionTotals)
sectionTotals = []
for i in range(len(students)):
    bodyCount = len(students[i])
    sectionTotals.append(bodyCount)

# Takes the totals of each section (sectionTotals) and finds the rounded average of all (avg)
avg = round(sum(sectionTotals)/len(sectionTotals))
print("Student body average of all sections:", avg)
