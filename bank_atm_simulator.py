class InvalidPinError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def atm_simulator():
    pin = "1234"
    account_balance = 10000
    attempts = 3

    while attempts > 0:
        pin_input = input("Enter the pin: ")
        if pin_input == pin:
            print("Access granted. Welcome to the ATM.")
            break
        else:
            attempts -= 1
            print(f"Invalid pin. Attempts remaining: {attempts}")
            if attempts == 0:
                raise InvalidPinError("Your account is locked due to too many incorrect pin. Your account will be unlocked after 24 hours.")
    
    try:
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print(f"Your current balance is: ${account_balance}")

            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                else:
                    account_balance += amount
                    print(f"You have successfully deposited ${amount}. Your current balance is ${account_balance}")
            
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                elif amount > account_balance:
                    raise InsufficientFundsError("Insufficient funds in the account.")
                else:
                    account_balance -= amount
                    print(f"You have successfully withdrawn ${amount}. Your current balance is ${account_balance}")
            
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        
    except ValueError as val:
        print(val)
    except InsufficientFundsError as ife:
        print(ife)
    finally:
        print("Thank you for using the ATM. Have a great day")

try:
    atm_simulator()
except  InvalidPinError as ipe:
    print(ipe)
finally:
    print("ATM session terminated.")