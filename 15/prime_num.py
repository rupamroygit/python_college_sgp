def prime_number(numa):
    if numa<0:
        print("Enter Number is Negative\n")
    elif numa%2==0 or numa%3==0 :
        print("Enter Number "+str(numa)+" is not Prime")
    else:
       print("The Number "+str(numa)+" is prime") 

prime=int(input("Enter a Number\n: "))
prime_number(prime)