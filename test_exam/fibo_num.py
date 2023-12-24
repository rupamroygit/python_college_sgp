num = int(input("Enter a Number\n: "))

num1 = 0
num2 = 1
print(num1, num2, end=',')
for i in range(0, num+1):
    var = num1+num2
    num1 = num2
    num2 = var
    print(var, end=' ,')
