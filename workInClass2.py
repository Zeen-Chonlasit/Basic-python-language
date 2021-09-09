print("----------โปรแกรมคำนวณค่าลงทะเบียน----------")

credit_describe = 0 
credit_practice = 0

# input หน่วยกิตบรรรยาย
credit_describe = int(input("กรุณากรอกหน่วยกิตบรรรยาย: "))
# input หน่วยกิตปฎิบัติ
credit_practice = int(input("กรุณากรอกหน่วยกิตปฎิบัติ: "))

# คิดค่าหน่วยกิตบรรรยาย
price_credit_describe = credit_describe * 60
# ค่าค่าหน่วยกิตปฎิบัติ
price_credit_practice = credit_practice * 120
# calculate
total = price_credit_describe + price_credit_practice
# output
print("ค่าลงทะเบียน: ", total)
