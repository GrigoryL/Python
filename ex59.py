import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
m = 0
for i in range(M):
    for n in range(len(arr[i])):
        S = arr[i]
        if S[n] == " ":
            m += 1
    print("Количество пробелов в слове " + "\"" + str(arr[i]) + " \" " + " равно " + str(m))
