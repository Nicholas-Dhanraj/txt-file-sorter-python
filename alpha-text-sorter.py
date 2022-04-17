import re

with open('ShortStory.txt', 'r') as file:
    filedata = file.read()
# filedata = filedata.replace('\"', '\'')

# regex cleaning
regex = re.compile(r'([\"\'\(]?[A-Z][^\.!?]*[\.!?][\"\'\)]?)')
regg = re.compile(r'(\'[a-z]*)')
# TO-DO: fully take out quoted sentences
# regex_apostrophe = re.compile(r'"(?:\\.|[^"\\])*"')
# print(re.sub(regex_apostrophe, '', filedata))

# take out apostrophes for plural words
# comment out if dont want to take out apostrophes on plural words
filedata = re.sub(regg, '', filedata)

# create list of sentences
match = re.findall(regex, filedata)
# sort list, if starts with "\"" then use idx at 1 (not 0)
extracted_sorted = sorted(match, key=lambda s: s if s[0].isalnum() else s[1:])
# print(match)
# write sorted result to file
result = open("sorted_story.txt", "w")
for element in extracted_sorted:
    result.write(element + "\n")
result.close()
