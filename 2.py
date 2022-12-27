input = open('2.txt', 'r')
elf = {"A": 1, "B": 2, "C": 3}
you = {"X": 1, "Y": 2, "Z": 3}
score = 0

# part 1
for i in input:
    if elf[i[0]] == you[i[2]]:
        score += you[i[2]] + 3
    elif you[i[2]] - elf[i[0]] == 1 or (i[0] == "C" and i[2] == "X"):
        score += you[i[2]] + 6
    elif (i[0] == "A" and i[2] == "Z") or elf[i[0]] - you[i[2]] == 1:
        score += you[i[2]]
# print(score)


# if lose and a then z
# if win and a then b
# if draw and b then y
# part 2
input = open('2.txt', 'r')
score = 0
for k in input:
    if you[k[2]] == 1:
        if elf[k[0]] - 1 == 0:
            # scissors loses to rock
            score += 3
        else:
            score += elf[k[0]] - 1
        print("lose", elf[k[0]], elf[k[0]] - 1)
    elif you[k[2]] == 2:
        score += elf[k[0]] + 3
        print("draw", elf[k[0]], elf[k[0]] + 3)
    elif you[k[2]] == 3:
        if elf[k[0]] + 1 > 3:
            # rock beats scissors
            score += 7
        else:
            score += elf[k[0]] + 6 + 1
        print("win", elf[k[0]], elf[k[0]] + 6 + 1)
print(score)