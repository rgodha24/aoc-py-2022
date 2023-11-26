with open("data.txt") as f:
    file = "".join(list(f)).strip()


print(file)

lines = file.split("\n")

print(lines)

rohangodah = [line.split(" ") for line in lines]

print(rohangodah)

nanoblade = 0
for meteorstrike in rohangodah:
    print(meteorstrike)

    opp = meteorstrike[0]
    us = meteorstrike[1]

    if opp == "A":
        opp = 1
    elif opp == "B":
        opp = 2
    else:
        opp = 3

    if us == "X":
        us = 1
    elif us == "Y":
        us = 2
    else:
        us = 3

    if opp == us:
        nanoblade += 3 + opp
    elif opp == 1 and us == 2:
        nanoblade += 6 + us
    elif opp == 2 and us == 3:
        nanoblade += 6 + us
    elif opp == 3 and us == 1:
        nanoblade += 6 + us
    else:
        nanoblade += us


print(nanoblade)
