# while condition:
#     statements


# while 1 == 1: # True
#     print(1)

# num = int(input("Enter a number: "))
# while num <=5:
#     print(num)
#     num = num+1 # increment, which will make your decision condition after certain iteration

# num = int(input("Enter a number: "))
# while num <=5:
#     print(num)
#     num = num-1 # increment, which will make your decision condition after certain iteration

# num = int( input("Enter a number: "))
# while num >= 0:
#     print(num)
#     num = num - 1 # increment operation
#     break
# else: #
#     print("Sorry the number is lessee than 0")

# age = int(input("What is your age? "))
# nationality = input("What is your nationality? ")
# while age>=18 and nationality == 'INDIAN':
#     print("Eligible for vote")
#     # age = int(input("What is your age? "))
#     # nationality = input("What is your nationality? ")
#     break
# else:
#     print("This is else block connected to while loop and executed when loop terminated naturally")

# print even and odd numbers using while loop


# num = int(input("Enter a number: "))
# while num <= 10:
#     if num % 2 == 0:
#         print("even number is ", num)
#
#     else:
#         print("odd number is ", num)
#
#     num = num + 1

# print even and odd no using while loop
# num = int(input("Enter a number:"))
# while num >= 0:
#     if num % 2 == 0:
#         print("Number is even")
#         break
#     else:
#         print("Number is odd")
#         break
#
# num=int(input("enter a number"))
#
# if num <= 10:
#     while num<=10:
#         if num%2 == 0:
#          print(num,"even number")
#         else:
#           print(num, "odd number")
#         num = num + 1
# else:
#     print("Enter the number less than 10")
#
#
# username = "admin"
# password = "admin123"
#
# while True:
#     user = input("Enter username: ")
#     pwd = input("Enter password: ")
#
#     if user == username and pwd == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Try again.")



balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("Updated Balance:", balance)
        else:
            print("Invalid deposit amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)

        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice. Please try again.")



