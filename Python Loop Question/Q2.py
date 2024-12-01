#Use a while loop to print even number from 1 to 50.
num=1  

while num <= 50:
    if(num%2!=0):
        num+=1
        continue
    print(num)
    num+= 2  
    