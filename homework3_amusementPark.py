print("สวนสนุก")
print("--------โปรแกรมคำนวณค่าบัตร--------")
print("บัตรผ่านประตู(1) หรือบัตรรวมเครื่องเล่น(2)")
card = int(input("กรุณาเลือกประเภทบัตร(1 หรือ 2) :"))
if card == 1 :
    height = int(input("กรุณากรอกความสูง(cm) :"))
    if height >= 160:
        price = 250
        print("ราคาทั้งหมด", price)
    else: 
        price = 200
        print("ราคาทั้งหมด", price)
elif card == 2 :
    height = int(input("กรุณากรอกความสูง(cm) :"))
    if height >= 160:
        price = 500
        print("ราคาทั้งหมด", price)
    else: 
        price = 500
        print("ราคาทั้งหมด", price)
else:
    print("กรุณากรอกใหม่อีกครั้ง")


