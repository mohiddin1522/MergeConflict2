s = "mohiddin"
print(s[1])
print(s[-(len(s))])
print(s[::-1])

# output
# o
# m
# niddihom

a = [1,"2",[3,4,5]]
print(type(a))
print(a[2])
print(a[2][1])

a.append("mohiddin")
print(a)

#output
# <class 'list'>
# [3, 4, 5]
# 4
# [1, '2', [3, 4, 5], 'mohiddin']

print(len(a))

#output
# 4