data = [1,4,3,2,8]
lis = []
while data:
    minimum = data[0]
    for u in data:
        if u< minimum :
            minimum = u
    lis.append(minimum)
    data.remove(minimum)


print(
    minimum
)