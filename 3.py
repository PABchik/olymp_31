counter = 0
for i in range(1, 21):
    for j in range(1, 21):
        if (i + j == 33):
            print("%d %d" % (i, j))
            counter += 1
print(counter)
