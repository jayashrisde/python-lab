print(f" 1. Fahrenheit to Celsius")
print(f" 2. Celsius to Fahrenheit")
option = int(input('Enter an option "1" or "2":'))
if option == 1:
    f = float(input("enter fahrenheit:"))
    c = (f - 32) * 5.0/9.0
    print(f"celsius =", c)
if option == 2:
    c = float(input("enter celsius:"))
    f = (c * 9.0/5.0) + 32
    print(f"fahrenheit =", f)