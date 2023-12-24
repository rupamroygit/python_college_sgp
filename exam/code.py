# Python program to illustrate
# Append vs write mode

filepath='myfiles.pdf'

file1 = open(filepath,"w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()

file1=open(filepath,'r')
print("Default: ")
print(file1.readlines())
print()

# Append-adds at last
file1 = open(filepath,"a") #append mode
file1.write("Today \n")
file1.close()

file1 = open(filepath,"r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open(filepath,"w") #write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open(filepath,"r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()
