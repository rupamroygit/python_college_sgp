def fibonaci_Number(num):
    numA=0
    numB=1
    numC=numA+numB
    print("Fibonaci Numbers Series is\n: ",end='')
    print(numA,",",numB,end=',')
    for i in range(1,num):
        print(numC,end=',')
        numA=numB
        numB=numC
        numC=numB+numA

number=int(input("Enter a positive Number\n: "))
fibonaci_Number(number)