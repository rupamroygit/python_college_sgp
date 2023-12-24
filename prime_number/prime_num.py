def prime(num):
    flage=0
    for i in range(2,num):
        if num%2==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print('Number is Not prime: ',num)
    else:
        print('Number is prime: ',num)

number=int(input("Enter a positive Number\n: "))
prime(number)