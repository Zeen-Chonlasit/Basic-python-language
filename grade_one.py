# name (string)
name = input("Enter your name: ")
# score (float)
score = eval(input("Enter your score: "))

if score > 100:
    print("Please enter a new score again")
elif score >= 80 and score < 100:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
elif score < 50 and score >= 0:
    print("Grade F")
else:
    print("Please enter a new score again")
