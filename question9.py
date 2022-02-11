# import json
# a={"shopping_list":{  "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",        }}
# item=input("Enter the item: ")
# qty=int(input("Enter the quantity: "))
# for i in a:
#     for j in a[i]:
#         if item in a[i]:
#             if item==j and int(a[i][j])>=qty:
#                 print(a[i][j])
#                 b=int(a[i][j])-qty
#                 a[i][j]=str(b)
#                 break
#             elif j!=qty:
#                 print("not valide")
#                 break

# with open("shopping.json","w")as shop:
#     json.dump(a,shop,indent=3)
# with open("shopping.json","r")as read_file:
#     c=read_file.read()
# print(c)
# print(type(c))    

def user(want):
    print(want)

a=input("enter the numa")
user(a)
