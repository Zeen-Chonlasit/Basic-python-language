print("โปรแกรมคำนวณค่าใช้จ่ายทั้งหมดสำหรับการท่องเที่ยวของสมาชิกกลุ่มหนึ่ง")

# expense
expense = eval(input("กรุณากรอกอัตราค่าใช้จ่าย : "))
# total number of members
number_member = eval(input("กรุณากรอกจำนวนสมาชิกทั้งหมด : "))
if number_member > 10:
    number_member_discount = number_member - 10
    discount = (expense * 5)/100
    expense_discount = expense - discount
    price = number_member_discount * expense_discount

    total = (10 * expense) + price

    print("ค่าใช้จ่ายทั้งหมด :", (total))
else :
    total = (number_member * expense)

    print("ค่าใช้จ่ายทั้งหมด :", (total))

