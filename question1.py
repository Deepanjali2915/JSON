# Q.1 Json data ko python object main convert karne ka program likho?.

# some JSON:
# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y=json.loads(x)
# print(type(y))



# a=[1,2,3,4,5,6]
# b={}
# i=0
# while i<len(a):
#     for key,value in dict.items(a):
#         b.update({i,a[i]})
#         print(b)
        # i+=1

def want(user):
    if user=="login":
        print(user)
    elif user=="signup":
        print(user)  
a=input("WHAT DO YOU WANT\nLOGIN AND SIGNUP")
want(a)
