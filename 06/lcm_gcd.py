"""def lakm(numA,numB):
    while(True):
        coun=2
        if(numA%coun==0 and numB%coun==0):
            print(coun,end="")
            numA=numA//coun
            numB=numB//coun
        elif(numA==0 or numB==0):
            break
        else:
            coun+=1"""

number = int(input("Enter the First Number "))
numbers = int(input("Enter the Second Number"))
cou = 2
"""while True :
    if(number%cou==0 and numbers%cou==0):
        print(cou,end="")
        number=number//cou
        numbers=numbers//cou
        continue
    elif(number==0 or numbers==0):
        break
    else:
        cou+=1"""
while 0 < number:
    if (number % cou == 0 and numbers % cou == 0):
        print(cou, end=",")
        number = number//cou
        numbers = numbers//cou
       # print(str(number)+","+str(numbers),end='')
        continue
    elif (number == 0 or numbers == 0):
        break
    else:
        cou += 1
