# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
import json
a={"name"+6:3,"class":10,"age": 6}
b=json.dumps(a)
print(b)
print(type(b))
