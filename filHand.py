file = open('fil1.txt', 'r')
# content = file.read()
# print(content)


content1 = file.readline()
content2 = file.readlines()
print(content1)
print(content2)
file.close()

file = open('fil1.txt', 'w')
file.write("Hello World ")
file.write("Hello chotu ")
file.close()

file = open('fil1.txt', 'a')
file.write("i am in chennai ")
file.write("i am taking training from revature")

file = open('fil1.txt', 'r')
content = file.read()
print(content)
file.close()