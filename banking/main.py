from bankcore import create_account, login
from accounts import check_balance, deposit, withdraw

def main():
    current_user = None
    
    while True:
        print(f"======================")
        print(f" Welcome to ABC Bank")
        print(f"======================")
        
        if current_user:
            print("\nSelect an option:")
            print("3. Deposit money")
            print("4. Withdraw money")
            print("5. Check balance")
            print("6. Exit")
        else:
            print("\nSelect an option:")
            print("1. Login to the account")
            print("2. Create an account")
            # print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1" and not current_user:
            customer_id = input("Enter customer ID: ")
            password = input("Enter password: ")
            if login(customer_id, password):
                current_user = customer_id
                
        elif choice == "2" and not current_user:
            name = input("Enter your name: ")
            password = input("Enter password: ")
            customer_id = create_account(name, password)
            if customer_id:
                print(f"Account created successfully! Your customer ID is: {customer_id}")
                
        elif choice == "3" and current_user:
            try:
                amount = float(input("Enter amount to deposit: "))
                deposit(current_user, amount)
            except ValueError:
                print("Invalid amount entered")
                
        elif choice == "4" and current_user:
            try:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(current_user, amount)
            except ValueError:
                print("Invalid amount entered")
                
        elif choice == "5" and current_user:
            balance = check_balance(current_user)
            print(f"Current balance: ${balance:.2f}")
                
        elif choice == "6":
            print("Thank you for using ABC Bank!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()