import json
import re
import os.path
chosse=input("what you chosse\n login or signup: \n")
existsfile=os.path.exists("neww.json")
listt=[]
# dictt={}
if chosse=="signup":
    print("Now! we will ceate a strong password: ")
    name=input("Enter the name: ")
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    password = input("Enter a password: ")
    result = re.findall(pattern, password)
    repassword=input("Re Enter the password: ")
    if password==repassword:
        print("Your password will be create")
        print("NOW!!!!\n you give some detilas")
        gender=input("Enter the gender:female or male: ")
        state=input("Enter the state: ")
        number=int(input("Enter the Contact number: "))
        Qualifeacation=input("Enter the qualifacation: ")
        hobby=input("Wnat your Hobbies\n any TWO: ")
        A={"name":name,"Gender":gender,"Number":number,"Qualifeacation":Qualifeacation,"hobby":hobby}
        listt.append(A)
        # dictt.update(listt)
        if existsfile==True:
            with open("neww.json","r")as file:
                f=file.read()
                p=json.loads(f)
            with open("neww.json","a")as d:
                json.dump([listt],d,indent=2)
        else:
            with open("neww.json","w") as sign:
                json.dump([listt],sign,indent=4,)  
                
# elif chosse=="login":
#     fullname=input("Enter your full name with surname:  ")
    
#     pasword2=input("Enter your password: ")
#     if pasword2=="Deepu@123":

#         with open("signup.json","r")as read_file:
#             c=read_file.read()
# # print(c)
# # print(type(c))    
