"""Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered."""

diction = {
    "name":"kavya",
    "age":24,
    "vehicle":"car",
    "id":1809,
    "org":"Clar",
    "address":[1/25,"saravanampatti","coimbatore-641021"]
}
# name = diction["name"]
# address = diction["address"]
# print(f" Hi {name} , here is your address:{address}")
# print(len(diction))

# for item in diction:
#     print(f"{item}:{diction[item]}")
    
# print(diction.get("address"))
# diction["age"] =34
# print(diction.items())
diction.update({"org":"Clar Technologies","id":1810})
diction.pop("address")
print(diction)