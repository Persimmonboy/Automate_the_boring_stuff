import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = 'some random resume with lot of phone numbers'

phoneRegex.search(resume) # Return the first match
phoneRegex.findall(resume) # Return list of matches as string 

lyrics = '12 drummers drumming, 11 pipes piping, 10 lords a leaping, 9 ladies dancing'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))
