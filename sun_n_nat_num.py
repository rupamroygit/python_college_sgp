numA=int(input("Enter a Natural Number\n: "))

def sum(numC):
    tem=0
    for i in range(0,numC+1):
        tem=tem+i
    tem=tem/numC ## store in floating point
    print("The Averge of "+str(numC)+" natural number is "+str(tem))

def compar(numb):
    if(numb<0):
        print("Ener a Negitive Number")
    else:
        sum(numb)

compar(numA)