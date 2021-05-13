l = [1, 2, 2, 2, 3, 4, 5, 18, 2]

n = 0
for i in l:
    n += 1
    # n é o número total de items na lista

index = range(0, n)
for item in index:
    if l[item] == 2:
        print(item)
