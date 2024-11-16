n = int(input("enter a number: "))
total = 0
temp = n
while temp > 0:
    digit = temp % 10
    total += digit ** len(str(n))
    temp //= 10
if n == total:
    print(f"{n}, is an armstrong number")
else:
    print(f"{n} is not an armstrong number")




