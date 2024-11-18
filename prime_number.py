n = int(input("enter number:"))
for i in range(2, n):
    flag = 1
    for j in range(2, i-1):
        if i % j == 0:
            flag = 0
    if flag == 1:
        print(i, "is a prime number")