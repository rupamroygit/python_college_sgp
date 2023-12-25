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
        else:
            continue
    
    return var


def lcm(numA,numB):
    numC=numA*numB//gcd(numA,numB)
    return numC


numA=int(input("Enter First Number\n: "))
numB=int(input("Enter Second Number\n: "))

gcd(numA,numB) 
lcm(numA,numB)

print("The GCD of ",numA," and ",numB," is : ",gcd(numA,numB))
print("The LCM of ",numA," and ",numB," is : ",lcm(numA,numB))