def gcd(numA,numB):
    var=1
    numC=0
    if(numA>numB):
        numC=numB
    else:
        numC=numA
    for i in range(1,numC):
        if(numA%i==0 and numB%i==0):
            var*=i
            print(var)
        else:
            continue
    
    print(var)


numA=int(input("Enter First Number\n: "))
numB=int(input("Enter Second Number\n: "))

gcd(numA,numB)
