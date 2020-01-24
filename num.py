num =str(input())
position=1 
new= 0
new2=0
odd = []
k=0
even = []
for i in num:
    position+=1
    p = position -1
    y= int(i)
    
    
    if p%2!=0:
        odd.append(y)
    else:
        even.append(y)

if len(num)%2!=0:
    for values in even :
        k =str((values*2))
        for numbers in k:
            new = int(numbers) + new           
    for val in odd:
        new = val + new 
    if new % 10 == 0:
        new= str(new)
        print("the overall sum is " +new+ " and is divisible by 10")
    elif new%10!=0:
        new= str(new)
        print("the overall sum is " +new+ " and is not divisible by 10")
elif len(num)%2==0:
    for values in even:
        k =str((values*2))
        for numbers2 in k :
            new2 =int(numbers2) + new2
    for val in odd:
        new2 = val + new2
        
    if new2 % 10 ==0:
        new2=str(new2)
        print("the overall sum is " +new2+ " and is divisible by 10")
        
        
    else:
        new2 = str(new2)
        print("the overall sum is " +new2+ " and is not divisible by 10")
        
        
        
        
        

        
   
    



    

