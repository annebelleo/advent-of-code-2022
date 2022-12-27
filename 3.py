import string
input = open('3.txt', 'r').readlines()
priority = 0
current_value = 0
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
# part 1
for i in input:
    compartment1 = i[0:int(((len(i) - 1) / 2))]
    compartment2 = i[int(((len(i) - 1) / 2)):]
    for j in compartment2:
        if j in compartment1:
            current_value = alphabet.index(j) + 1
    priority += current_value
    # print(priority)
# part 2
current_value = 0
iterator = 0
for line in input:
    if iterator == 3:
        badge = set(list1) & set(list2) & set(list3)
        badge = badge.pop()
        current_value += alphabet.index(badge) + 1
        iterator = 1
    else:
        iterator += 1
    line = line.strip()
    globals()['list' + str(iterator)] = [z for z in line]
print(current_value)
# 2907 too high
# 2668 not correct