# Q.3 Python object ko json string mai convert karne ka program likho?
import json
a={"name":"David","class":"I","age": 6}
b=json.dumps(a)
print(b)
print(type(b))
