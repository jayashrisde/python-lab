tamil = int(input(f"enter Tamil mark:"))
english = int(input(f"enter English mark:"))
maths = int(input(f"enter Maths mark:"))
allied = int(input(f"enter allied mark:"))
python = int(input(f"enter Python mark:"))
Total = tamil + english + maths + allied + python
ave = Total / 5
print(f"Total =", Total)
print(f"average =", ave)
if ave >= 80:
    print("Grade A")
elif ave >= 70 and ave < 80:
    print("Grade B")
elif ave >= 60 and ave < 70:
    print("Grade C")
elif ave >= 40 and ave < 60:
    print("Grade E")
else:
    print("Grade E")
