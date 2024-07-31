# Bank Management System
import random

def main():
    Data = {}
    while True:
        print("Bank Management System")
        operation = int(input("""How Can I Help You?:
                              1.Create a Account
                              2.Deposit a Money
                              3.Withdraw a Money
                              4.Check Balance
                              5.Exit
                              """))
        
        if (operation == 1):
            name = input("Enter Your Name: ")
            account_type = input("Enter Account Type(Saving/Current): ")
            Balance = float(input("Enter Initial amount that must be more than 500Rs. : "))
            if(Balance<500):
                print("Initial amount must be more than 500RS.")
                continue
            
            account_number = random.randint(100000, 999999)
            Data[account_number] = {"Name":name, "Type":account_type, "Balance":Balance}
            print(f"Account Created Successfully your Account Number is {account_number}")
        
        elif(operation == 2):
            account_number = float(input("Enter your Account Number: "))
            if account_number in Data:
                amount = float(input("Enter Deposit Amount: "))
                Data[account_number]['Balance'] += amount
                print(f"Amount Deposit Successfully! New Balance is: {Data[account_number]['Balance']}")
            else:
                print("Account Not Found.")

        elif (operation == 3):
            account_number = float(input("Enter your Account Number: "))
            if account_number in Data:
                amount = float(input("Enter Withdraw Amount: "))
                if amount > Data[account_number]['Balance']:
                    print("Insufficient Balance")
                else:
                    Data[account_number]['Balance'] -= amount
                    print(f"Amount withdrawn successfully! New balance is {Data[account_number]['Balance']}")
            else:
                print("Account not found.")
       

        elif(operation == 4):
            account_number = int(input("Enter your Account Number: "))
            if account_number in Data:
                print(f"Account Balance: {Data[account_number]['Balance']}")
            else:
                print("Account not found.")


        elif(operation == 5):
            print("Thank you for using the Bank Management System.")
            break;

main()


