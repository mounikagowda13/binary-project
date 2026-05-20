print("1. Binary to Decimal")
print("2. Decimal to Binary")

choice = int(input("Enter Choice: "))

if choice == 1:
    binary = input("Enter Binary Number: ")
    decimal = int(binary, 2)
    print("Decimal Number is:", decimal)

elif choice == 2:
    decimal = int(input("Enter Decimal Number: "))
    binary = bin(decimal)[2:]
    print("Binary Number is:", binary)

else:
    print("Invalid Choice")