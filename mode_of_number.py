ARR = list(input("enter number to find mode: "))
new = set(ARR)
g = len(new)
i = 0
u = 0
mode = []
for t in new:
    for AR in ARR :
        if t == AR :
                i+=1
    if i > u:
        u = i
        mode.append(t)
    i=0
print("the mode is:",mode[-1])


           
           
   
       

            
           
           
 
