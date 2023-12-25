num =int(input("Enter a Binary Digit\n : "))

counter =0
tem=0

while(num>0):
    store=num%10
    num=num//10
    c=(2**counter)*store
    tem=tem+c
    counter+=1
print("Decimal Value is : ",tem)