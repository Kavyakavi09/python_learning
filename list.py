# ordered, changable and allow duplicates

from pickle import TRUE


# list = ["car","bike","scooter",40,50,True,"car","bike"]
# print(list)
# print(len(list))
# print(list[0:5])
# print(list[:3])
# print(list[5:])
# list[2:3]=["pep"]
# print(list)
# list.append({"like":"audi"})
# list.insert(3,90)
# print(list)
# tuple

# ordered, unchangable and allow duplicates
tuple = ("car","bike","scooter",40,50,True,"car","bike")
li = list(tuple)
li[0] = "zray"
print(li)
