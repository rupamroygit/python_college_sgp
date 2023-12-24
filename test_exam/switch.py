def num_convert(num):
    match num:

        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case default:
            print("Enter Worng input")


num = int(input("Enter a number\n: "))
num_convert(num)
