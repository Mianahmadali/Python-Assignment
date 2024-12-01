#write a program that takes a temperature in celsius and checks if its freezing, moderate or hot.
tem=int(input("Enter temperature in celsius:"))
if tem<=0:
    print ("The temperature is freezing")
elif tem>0 and tem<=25:
    print("the temperature is moderate")
else:
    print("the temperture is hot")