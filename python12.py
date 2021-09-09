from datetime import date

a = date.today()
print("วันที่ : ", a)

b = a.year
c = b + 543
print("พ.ศ.", c)
d = a.month
mylist = ["มกราคม", "", "", "", "", "", "", "", "กันยายน", "", "" ,""]
print("เดือน", mylist[d-1])
e = a.day
print("วัน ", e)
print(c, d, e)
f = a.strftime("%a %d %m %Y")
print(f)
