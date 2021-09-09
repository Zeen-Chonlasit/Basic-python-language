import random

a = random.randint(1, 10)
print(a)
b = random.randrange(1,10,2)
print(b)
mylist = ["ตุ๊กตา", "500 บาท", "หุ่นยนต์", "แฟลตไดร์ฟ", "พาวเวอร์แบงค์"]
c = random.choice(mylist)
print(c)