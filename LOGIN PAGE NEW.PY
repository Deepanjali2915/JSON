import os.path
import json
import re
user=input("WHAT DO YOU WANT\nLOGIN AND SIGNUP")
existsfile=os.path.exists("new.json")
if user=="signup":
    name=input("Enter the name: ")
    
        
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    password = input("Enter a password: ")
    result = re.findall(pattern, password)
    listt=[]
    dictt={}

    if (result):
        # print ("Valid password")
        confirm=input("Re enter the password")


        if password==confirm:
            print("Your password will be create")
            print("NOW!!!!\n you give some detilas")
            gender=input("Enter the gender:female or male: ")
            state=input("Enter the state: ")
            number=int(input("Enter the Contact number: "))
            Qualifeacation=input("Enter the qualifacation: ")
            hobby=input("Wnat your Hobbies\n any TWO: ")
            A={"name":name,"Gender":gender,"Number":number,"Qualifeacation":Qualifeacation,"hobby":hobby}
            if existsfile==True:
                listt.append(A)
                dictt.update({password:listt})
                with open("new.json","a")as file:
                    json.dump(dictt,file,indent=4)
    else:
        print("Wrong password please try again")
# if user=="login":
#     login=input("Enter the user name: ")
#     if existsfile==True:
#         password=input ("Enter user pasword: ")
#         with open("new.json","r")as file:
#             a=file.read()
#             d=json.loads(a)
#             for i in range(len(d)):
#                 if d[i]["name"]==name:
#                     print("login successful")
#                 elif i==len(d)-1 and d[i]["name"]!=name:
#                     print("Opsss!! wrong password")
#     else:
#         print("oppss!! wrong details") 
# # else:
#     # print("Sorry!! Please try again: ")