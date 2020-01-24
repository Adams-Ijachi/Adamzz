m= 8
k =0
for i in range(m):
    i = m - i
    if i % 2 == 0:
        i = i
        for l in range(k):
             print(end=" ")
        k +=1
        for n in range(i):
            print("#",end="")

        print("")