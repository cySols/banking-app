branch_id = 2057
customer_count = 0
users_info = {}

def generate_customer_id():
    global customer_count
    customer_count += 1
    return f"{branch_id}-{customer_count}"

def create_account(name, password):
    try:
        if not name or not password:
            raise ValueError("Name and password cannot be empty")
        customer_id = generate_customer_id()
        users_info[customer_id] = {"name": name, "password": password}
        print(f"Account Created > Your Customer ID is: {customer_id}")
        return customer_id
    except ValueError as e:
        print(f"Error: {e}")
        return None

def login(customer_id, password):
    try:
        if customer_id in users_info and users_info[customer_id]["password"] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid login")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False