def prime_giv_range(low_Num,high_Num):

    flag=0
    for i in range(low_Num,high_Num+1):
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
            else:
                flag=0

        if(flag==0):
            print(i,end=',')

print("Enter Postive Numbers")
numA=int(input("Enter a Lower Number\n: "))
numB=int(input("Enter a Higher Number\n: "))
prime_giv_range(numA,numB)