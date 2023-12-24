dnum=int(input("Enter a Decimal Number: "))
##input for decimal number

coun=0
tem=0

while(dnum>0):
      reminder=dnum%2
      dnum=dnum//2
      c=(10**coun)*reminder
      tem=tem+c
      coun+=1
print(tem)