values = sorted([10,6,2,14,7,9,9,9])
print((9+9)/2)
med = 0
middle = 0
index = 0
if len(values) % 2 !=0:
     index = int((len(values) - 1) / 2)
     print("the median is:",values[index])
if len(values) % 2 == 0:
    index = int((len(values) / 2)- 1)
    middle = (values[index] + values[index + 1]) / 2
   # print("the median is:",middle)