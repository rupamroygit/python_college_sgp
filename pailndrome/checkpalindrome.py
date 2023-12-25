def palinderome(str):
    flag=0
    if str==str[::-1]:
        flag=1
    else:
        flag=0
    return flag
text=input("Enter a String\n: ")
palinderome(text)

if(palinderome(text)==1):
    print('The String ',text,' is Palindrome')
else:
    print('The String ',text,' is not Palindrome')