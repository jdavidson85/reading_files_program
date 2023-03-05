file1 = open("sales_totals.txt", "r")
values = file1.readlines()
total = 0

for i in values:
    a = float(i)
    total += a
    print(a)

total = round(float(total), 2)

print("Total: " + str(total))
print("Number of entries: " + str(len(values)))
print("Average: " + str(round(total / len(values), 2)))
