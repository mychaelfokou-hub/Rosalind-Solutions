sum = 0
x = 4254
y = 8870
for odd in range(x, y+1):
    if odd % 2 != 0:
        sum = sum+odd
print(sum)
