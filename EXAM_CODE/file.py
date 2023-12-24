var=open('my.txt',mode='r')
number_of_word=0
number_of_char=0
for line in var:
    line=line.strip('\n')
    number_of_char += len(line)
    word=line.split()
    number_of_word+=len(word)
print("Number of Chars: ",number_of_char)
print("Number of Words: ",number_of_word)