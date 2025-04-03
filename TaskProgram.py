s = " Mohiddin Basha "
print(f" original string: {s}")
print(f"length of string: {len(s)}")
print(f"upper case: {s.upper()}")
print(f"lower case: {s.lower()}")
print(f"swap case: {s.swapcase()}")
print(f"slicing: {s[1:5]}")
print(s[1:8:2]) #slicing with step
print(s[2:]) #starting from 2nd index to end
print(s[:5]) #starting from beginning to 5th index
print(s[::-1]) #reverse string
print(s[-7:9]) #negative indexing
print(s.strip()) #removes leading and trailing spaces
print(s.replace("M","m")) #replace M with m
print(s.split(" ")) #splitting string with ,
a = "shaik"
b = "basha"
print(a+b) #concatenation
print(s.count("h")) #counting number of h in string


li = [3,6,9,12,15]
print(li)

b = bytes([65])
print(b)

c = None
print(c)
print(type(c))
# y
# print(type(y))
# print(y) y is not defined