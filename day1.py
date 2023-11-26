with open("data.txt") as f:
    file = "".join(list(f))

print(file)

elf = file.split("\n\n")

print(elf)

elfs = []

for i in elf:
    cals = i.strip().split("\n")
    new = []

    for j in cals:
        new.append(int(j))

    elfs.append(new)

print(elfs)

calories = []

for elf in elfs:
    sum = 0
    for cal in elf:
        sum = sum + cal

    calories.append(sum)

print(calories)

max = 0
for i in calories:
    if i > max:
        max = i

print(max)
