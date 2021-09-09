num_list = [10,20,30,40,50]
guess = int(input("ทายตัวเลข : "))
if guess in num_list :
    print("คุณทายถูก")
    print("แล้ว")
else:
    print("คุณทายผิด")
    print("ลองเล่นอีกครั้ง")
print("คุณจะได้รางวัลเมื่อคุณทายถูก")
firstPrize_num_list = [10, 20, 30, 40, 50]
secondPrize_num_list = [60, 70, 80, 90, 100]

guess = eval(input("กรุณาสุ่มตัวเลข: "))

if guess in firstPrize_num_list:
    print("คุณถูกรางวัลที่ 1 !!!")

elif guess in secondPrize_num_list:
    print("คุณถูกรางวัลที่ 2 !!!")

else:
    print("ขอโทษ, คุณเดาผิด...")

print("คุณจะได้รับรางวัลก็ต่อเมื่อทายตัวเลขได้ถูกต้องเท่านั้น")
