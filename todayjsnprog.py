import json
a = '{"name":"chotu"}'
b =json.loads(a)
print(b["name"])

x = {"name":"mohiddn","age":23}
z = json.dumps(x)
print(z)