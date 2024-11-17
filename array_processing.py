x = []
n = int(input("how many numbers: "))
for i in range(1,n+1):
    x.append(int(input("enter a number:")))
print("given list")
print(x)
oc = 0
ec = 0
for i in range(n):
    if x[i] == 0:
        ec += 1
    else:
        oc += 1
print(f"Total odd numbers: {oc}")
print(f"Total even numbers: {ec}")

