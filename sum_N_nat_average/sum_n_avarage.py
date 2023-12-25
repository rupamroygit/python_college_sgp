def sum_n_number(num_sum):
    numA=0
    for i in range(1,num_sum+1):
        numA+=i

    return numA
def avarage(n_num):
    return sum_n_number(n_num)//n_num

num=int(input('Enter a N Natural positive Number:'))

print("The sum of ",num," Natural number is : ",sum_n_number(num))
print("The avarage of ",num," Natural number is : ",avarage(num))