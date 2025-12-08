a = 0
result = 0
while a < 5:
    a += 1
    if a % 2 == 0:
        result += a
    if a == 2:
        continue
    if a == 4:
        break
    print(a)

print("-----")
print(a)
print(result)
