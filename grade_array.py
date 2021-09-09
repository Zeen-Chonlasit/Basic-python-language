# creating an empty list (name, score, grade)
lst_n = []
lst_s = []
lst_g = []

# number of people
n = int(input("Enter number of people: "))

# iterating till the range
for i in range(0, n):
    # name[array] (string)
    name = input("Enter your name: ")
    # adding name
    lst_n.append(name)

    # score[array] (float)
    score = eval(input("Enter your score: "))
    # adding score
    lst_s.append(score)

for i in range(0,n):
    if lst_s[i] > 100:
        lst_g.append("Please enter a new score again")
    elif lst_s[i] >= 80 and lst_s[i] < 100:
        lst_g.append("Grade A")
    elif lst_s[i] >= 70:
        lst_g.append("Grade B")
    elif lst_s[i] >= 60:
        lst_g.append("Grade C")
    elif lst_s[i] >= 50:
        lst_g.append("Grade D")
    elif lst_s[i] < 50 and lst_s[i] >= 0:
        lst_g.append("Grade F")
    else:
        lst_g.append("Please enter a new score again")

for i in range(0,n):
    print(lst_n[i])
    print(lst_s[i])
    print(lst_g[i])
