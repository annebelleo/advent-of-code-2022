input = open('5.txt', 'r').readlines()
crates = []
movements = []
for i in range(9):
    crates.append(input[i].strip().split('[]'))
for j in range(10, len(input)):
    movements.append(input[j].strip().split(' '))
for move in movements:
    print(move[1], move[3], move[5])
