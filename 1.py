input = open('1.txt', 'r')
sum = 0
sums = []
for i in input:
    if i == '\n':
        sums.append(sum)
        sum = 0
    else:
        sum += int(i)
sums_sorted = list(set(sums))
sums_sorted.sort()
print(sums_sorted[-1] + sums_sorted[-2] + sums_sorted[-3])

