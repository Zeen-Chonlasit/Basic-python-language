menu = ["สุกี้แห้ง","ราดหน้าหมู","ผัดไทย"]
print(type(menu))
address = [135, 9, "วังน้ำเขียว", "กำแพงแสน", "นครปฐม", 73140]
old_fashion_address = "135 9 ต.วังน้ำเขียว อ.กำแพงแสน จ.นครปฐม 73140"
print("จ.", address[4])
print(old_fashion_address[24])   #ไม่นิยมใช้
print(address[-1])
menu.append("บะหมี่เกี๊ยว")
print(menu) # print ทั้ง list เหามะกับนักพัฒนาโปรแกรมเอาไว้ดูข้อมูลใน list
            # แต่ไม่เหมาะกับการเป็ฯ output ของโปรแกรม เพราะมีสัญลักษณ์พิเศษติดอยู่
food = input("กรอกเมนูอาหารชนิดใหม่ : ")
menu.insert(0, food)
print(menu)
print(menu[0], menu[1], menu[2]) # เหมาะกับการเป็น output ของโปรแกรม
menu[3] = "หมด"
print(menu)
#menu.remove(0) ลบทีละ index
#menu.pop(1) ลบทีละ index
#del menu[1] ลบทีละหลายๆ index
#menu.clear() or menu[:] = [] ลบทั้งหมด
print("ยำวุ้นเส้น" in menu) # หาว่ามีอยู่ไหม
#menu.sort() # เรียงลำดับตัวอักษร ก-ฮ
#menu.reverse() # เรียงลำดับตัวอักษร ฮ-ก
print(menu.count("หมด")) #menu.count(element) # นับความจำนวนของสมาชิก
print(len(menu)) #len(menu) # นับทั้งหมด