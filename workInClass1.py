all_price = 0
discount = 0
total = 0
for i in range(3) :
    print("---------------------------------- สินค้าชิ้นที่", (i + 1), " ----------------------------------")
    price = int(input("กรุณากรอกราคาของสินค้า: "))
    all_price = all_price + price
    print("รวมราคาสินค้า :", all_price)

if all_price >= 1500 and all_price < 2500:
    # discount 5 %
    discount = all_price * 5 / 100
    total = all_price - discount
elif all_price >= 2500 and all_price < 5000:
    # discount 10 %
    discount = all_price * 10 / 100
    total = all_price - discount
elif all_price >= 5000 :
    # discount 10 %
    discount = all_price * 15 / 100
    total = all_price - discount
else :
    total = all_price

print("ราคาสินค้า :", all_price)
print("ราคาส่วนลด :", discount)
print("ราคาสุทธิ :", total)

