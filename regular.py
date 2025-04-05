import re
x = "The rain in Spain"
y = re.search("^The.*Spain$", x)
if y:
    print("YES! We have a match!")
else:
    print("No matching with pattern")
    
y = re.search("ai", x)
print(y)

z = re.split("\s", x)
print(z)

z1 = re.findall("ai", x)
print(z1)

z2 = re.sub("\s", "$", x)
print(z2)

# search is used to search for a pattern in a string.
# split is used to split a string into a list based on a pattern.
# findall is used to find all occurrences of a pattern in a string.
# sub is used to replace occurrences of a pattern in a string with another string.


pattern = r"\d+"
test = "There are 123 apples"
matchees = re.search(pattern, test)
if matchees:
    print("Found a match:", matchees.group())

print(pattern)

matches = re.findall(pattern, test)
print(matches)

pattern2 = r"(\d+)-(\d+)-(\d+)"
text = "2025-02-15"
matching = re.match(pattern2, text)
if matching:
    print("Found a match:", matching.group(3))
