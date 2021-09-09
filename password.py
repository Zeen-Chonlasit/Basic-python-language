password = ["123456", "1111"]
pw = input("รหัสผ่านคือ>>>")
for data in password:
    if data != pw:
        pass
    else:
        print("พบข้อมูลรหัสผ่านนี้")
print("แล้วเจอกันใหม่")
