balance_record = {}

def check_balance(customer_id):
    try:
        if customer_id not in balance_record:
            balance_record[customer_id] = 0.0
        return balance_record[customer_id]
    except Exception as e:
        print(f"Error checking balance: {e}")
        return 0.0

def deposit(customer_id, amount):
    try:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if customer_id not in balance_record:
            balance_record[customer_id] = 0.0
        balance_record[customer_id] += amount
        print(f"Deposited ${amount:.2f}. New balance: ${balance_record[customer_id]:.2f}")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error during deposit: {e}")
        return False

def withdraw(customer_id, amount):
    try:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if customer_id not in balance_record:
            balance_record[customer_id] = 0.0
        if balance_record[customer_id] >= amount:
            balance_record[customer_id] -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${balance_record[customer_id]:.2f}")
            return True
        else:
            print("Insufficient balance")
            return False
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error during withdrawal: {e}")
        return False