sumPrice = 0
noMoney = 0
count = 0
lst_price = []
lst_gender = []
lst_height = []

# number of people
number = int(input("Enter number of people: "))
for i in range(number) :
    print("----------------------------------No.", (i + 1), "----------------------------------")
    gender = input("Enter your gender(man or woman) :")
    height = float(input("Enter your height: "))
    lst_height.append(height)
    lst_gender.append(gender)
    if gender == "man" and height < 100:
        price = "Free"
        lst_price.append(price)
        sumPrice = sumPrice + 0
        count = count + 1
        noMoney = noMoney + 1
        print("price =", price)
    elif gender == "man" and height >= 100:
        price = 20
        lst_price.append(price)
        sumPrice = sumPrice + 20
        count = count + 1
        print("price =", price)
    elif gender == "woman" and height < 100:
        price = "Free"
        lst_price.append(price)
        sumPrice = sumPrice + 0
        count = count + 1
        noMoney = noMoney + 1
        print("price =", price)
    elif gender == "woman" and height >= 100:
        price = 25
        lst_price.append(price)
        sumPrice = sumPrice + 25
        count = count + 1
        print("price =", price)
    else :
        print("กรุณากรอกใหม่อีกครั้ง!!!")
print("ค่าผ่านทางที่ทางร้านได้รับทั้งหมด :", sumPrice)
print("จำนวนผู้เข้าชมทั้งหมดในวันนี้ :", count)
print("จำนวนผู้เข้าชมที่ไม่เสียค่าผ่านประตู :", noMoney)
print("ข้อมูลการซื้อขาย เพศ :", (lst_gender), "ส่วนสูง :", (lst_height), "ราคา :", (lst_price))
# print("ราคา :", (lst_price))
