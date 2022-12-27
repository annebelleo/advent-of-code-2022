input = open('4.txt', 'r').readlines()
sections = []
encompassing = 0
for i in input:
    sections.append(i.strip().split(','))
for list in range(len(sections)):
    first = sections[list][0].split('-')
    second = sections[list][1].split('-')
    if (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1])) or (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])):
        encompassing += 1
    elif int(first[0]) == int(second[1]) or int(first[1]) == int(second[0]):
        encompassing += 1
    elif int(first[1]) > int(second[0]) and int(first[0]) < int(second[0]):
        encompassing += 1
    elif int(second[1]) > int(first[0]) and int(second[0]) < int(first[0]):
        encompassing += 1
print(encompassing)
