problemSize = 1000

print("%15s%14s" %("Problem Size", "Iterations"))

for count in range(5):
    number = 0
    work = 1
    for i in range(problemSize):
        for j in range(problemSize):
            number += 1
            work += 1
        work -= 1
    print("%12d%16d" %(problemSize, number))
    problemSize *= 2