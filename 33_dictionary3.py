my_dict = {"name": "Alice", "age": 25}

print(my_dict.get("name"))         # Output: Alice
print(my_dict.get("city", "N/A"))  # Output: N/A

my_dict.update({"city": "Pune"})
print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'Pune'}

print(my_dict.keys())    # dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # dict_values(['Alice', 25, 'Pune'])
print(my_dict.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Pune')])

my_dict.pop("age")
print(my_dict)  # {'name': 'Alice', 'city': 'Pune'}

my_dict.clear()
print(my_dict)  