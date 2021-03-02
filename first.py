# print((2+10) * (10+3))
# mystring ="abcdef"
# print(mystring)

# my_list= [2,4,1,5, 3,9]
# my_list.sort()
# print(my_list)

s='django'

print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4:])


l=[3,7,[1,4,'hello']]
(l[2][2])= 'goodbye'

print(l)

d1 = {'simple_key': 'hello'}
d2= {'k1': {'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep', ['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

mylist =[1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,]
print(set(mylist))

age= 29
name= 'kaur'
print("my love's age is {a} and his name is {b}".format(a=name, b=age) )