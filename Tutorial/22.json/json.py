import json

# some json
x = '{"name":"shakil","age":30,"city":"bogura"}'

# parse
y = json.loads(x)
print(y)



# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)