from typing import Counter


def arrayCheck (nums):
    for i in range(len(nums)-2):
        if nums[i] ==1 and nums[i+1] ==2 and nums[i+2]==3:
            return True
    return False

#print one letter after skip

def stringBits(mystring):
    result= ""
    for i in range(len(mystring)):
        if i%2== 0:
            result = result +mystring[i]
    return result

print(stringBits('mynameismamta'))

#if second part ends with the last of first
def endOther(a, b):
    a=a.lower()
    b=b.lower()

    return (b.endswith(a) or a.endswith(b))

print (endOther('hiabc', 'abc'))


def doubleChar(anyword):
    myresult=""
    for char in anyword:
        myresult +=char*2
        return myresult

print(doubleChar('mamta'))

def no_teen_sum(a, b, c ):
    return fix_teen(a)+ fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n[13,14,17,18,19]:
        return 0
    return n


def count_evens():
    count = 0
    for i in range(10):
        if i % 2 == 0:
            count += 1

    return count

print(count_evens())

# def count_evens(nums):
#     count = 0
#     for i in range(nums):
#         if i % 2 == 0:
#             count += 1

#     return count

# print(list(count_evens(10)))