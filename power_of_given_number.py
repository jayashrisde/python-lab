base = int(input("enter base number: "))
exponent = int(input("enter exponent number: "))
rev = 1
for exp in range(0,exponent):
    rev *= base
print(f"power of given number: {rev}")