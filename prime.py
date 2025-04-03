num = int(input("Enter a number: "))
cnt = 0
for i in range(2, num):
    if( num % i == 0):
        cnt += 1
if (cnt == 0):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    