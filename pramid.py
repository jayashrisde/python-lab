rows = int(input("enter number of rows: "))
for i in range(1, rows+1):
    k = 0
    while k != (2*i-1):
        print("*", end = "")
        k += 1
    print()