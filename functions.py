def addTwoNumbers(num1, num2):
    return num1 +num2

print(addTwoNumbers(3,5))

mylist= [1,2,3,4,5,6,7,8,9]

def even_bool(num):
    return num%2==0

# lambda num: num%2==0
# evens = filter(lambda num: num%2==0,mylist)
# print(list(evens))

evens = filter(even_bool,mylist)
print(list(evens))


