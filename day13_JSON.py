print("--- Recalling hashing ---")
print(hash("hello"))
print(hash(42))
print(hash((1, 2)))
try:
    print(hash([1, 2]))
except TypeError as e:
    print("Error:", e)

'''print("--- Set vs List: fixed timing test ---")
import time

customer_ids_set = set(range(1_000_000))
customer_ids_list = list(range(1_000_000))

start = time.time()
for _ in range(10_000):
    999_999 in customer_ids_set
end = time.time()
print(f"SET: {end - start:.6f} seconds for 10,000 lookups")

start = time.time()
for _ in range(10_000):
    999_999 in customer_ids_list
end = time.time()
print(f"LIST: {end - start:.6f} seconds for 10,000 lookups")'''



print("--- Writing and reading JSON files ---")
import json

data = {"name": "Priya", "age": 30, "skills": ["Python", "SQL"]}

with open("employee.json", "w") as file:
    json.dump(data, file)

with open("employee.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
print(type(loaded_data))

print("--- Nested JSON ---")
data = {
    "name": "Priya",
    "address": {"city": "Toronto", "postal_code": "M5V 1A1"},
    "skills": ["Python", "SQL", "AI"]
}
json_string = json.dumps(data, indent=2)
print(json_string)

print("--- Testing the real differences ---")
import json

# Single quotes - does this work in JSON?
try:
    json.loads("{'name': 'Priya'}")
except json.JSONDecodeError as e:
    print("Single quotes failed:", e)

# Double quotes - this should work
result = json.loads('{"name": "Priya"}')
print("Double quotes worked:", result)

try:
    json.loads('{"active": True}')
except json.JSONDecodeError as e:
    print("Python-style True failed:", e)

result = json.loads('{"active": true}')
print("lowercase true worked:", result)