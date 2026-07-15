a = []

print("Enter 9 elements:")
for i in range(9):
    a.append(int(input()))

a.sort()

a.remove(0)
a.append(0)

print("Output:")
for i in range(0, 9, 3):
    print(a[i], a[i+1], a[i+2])
