s1 = "Hello good morning"
s2 = lambda x: x.upper()
print(s2(s1))


sq = lambda x: x**2
print(sq(5))


li = [lambda arg = x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
    


sq = lambda x : x*x
print(sq(5))

check = lambda x : "EVen" if x % 2 == 0 else "odd"
print(check(5))
print(check(4))


calc = lambda x,y : (x+y, x-y, x*y, x/y)
print(calc(10, 5)) #if you pass multiple arguments, it will return a tuple with all the results


n =[1,2,3,4,5]
even = filter(lambda x: x % 2 == 0, n) #filter function filters based on the condition provided in the lambda function
print(list(even)) # [2, 4]


a = [1,2,3,4]
b = map(lambda x: x * x, a) #map function applies the lambda function to each element in the list
print(list(b)) # [1, 4, 9, 16]


from functools import reduce #reduce function reduces the list to a single value by applying the lambda function cumulatively
a1 = [1,2,3,4]
b1 = reduce(lambda x, y: x + y, a1) #reduce function reduces the list to a single value by applying the lambda function cumulatively
print(b1) # 10