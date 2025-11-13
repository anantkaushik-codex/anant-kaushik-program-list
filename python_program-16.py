n = int(input("Enter number: "))
s = sum(int(d)**3 for d in str(n))
print("Armstrong" if s == n else "Not Armstrong")