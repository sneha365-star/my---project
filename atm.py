balance = 1000  # starting balance

def check_balance():
    print("\nYour current balance is:", balance)

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposited successfully!")
    else:
        print("Invalid deposit amount!")

def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid withdrawal amount!")
    else:
        balance -= amount
        print("Withdrawal successful!")

def atm_menu():
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# main program loop
while True:
    atm_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        withdraw_money()
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
