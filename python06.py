for i in range(1, 101):
    print(i)

#for(i=0;i<=100;i++)
#   print(i)

start = 1
stop = 11

for i in range(20): # 0 1 2 3 4 5 ... 19
    print("hello")

week = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
print(week[0], week[1], week[2], week[3] , week[4]) #สังเกตว่ามีการทำซ้ำควรใช้ลูป for
for i in week:
    print("วัน", i)

user_input = ''
while user_input != "unlock": 
    user_input= input("กรุณาใส่ข้อมูลรหัสผ่าน")

week = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
for i in week:
    if i == "จันทร์" :
        continue
    else:
        print(i)



