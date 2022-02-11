# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
Text={"Name": "Abhishek","Designation":"CEO of navgurukul","Gender":"male" ,"Age" :29}
# # Python program to convert text
# # file to JSON


import json
out_file = open("new.json", "w")
json.dump(Text, out_file, indent = 4, sort_keys = False)
out_file.close()
# Python program to convert text
# file to JSON


# a=open ("new.txt","w")

# a.close()

# b=json.dumps("data.txt",Text,"w"