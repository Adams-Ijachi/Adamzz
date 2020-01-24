data = [1,4,3,2,8]
lis = []
while data:
    maximum = data[0]
    for u in data:
        if u< maximum :
            maximum = u
    lis.append(maximum)
    data.remove(maximum)


print(maximum)
