def prime_print(numB):
    for i in range(1,numB+1):
        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            continue
        else:
            print("Prime Factor are "+str(i))
def compare(numA):
    if(numA<0):
       ## numA=numA*(-1)
       ## prime_print(numA)
        print("Enter Negative Number")
    else:
        prime_print(numA)

num=int(input("Enter a Number\n: "))
compare(num)