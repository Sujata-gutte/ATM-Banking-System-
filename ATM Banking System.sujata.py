PIN = "1234"
balance = 1000.0


def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")

def deposit():
    global balance
    try:
        amount = float(input("\nEnter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ₹{amount:.2f}")
        else:
            print("Invalid amount!")
    except:
        print("Please enter a valid number!")

def withdraw():
    global balance
    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"Successfully withdrawn ₹{amount:.2f}")
        else:
            print("Insufficient balance or invalid amount!")
    except:
        print("Please enter a valid number!")

def atm():
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == PIN:
            print("\nLogin Successful!")

            while True:
                print("\n===== ATM MENU =====")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    check_balance()
                elif choice == "2":
                    deposit()
                elif choice == "3":
                    withdraw()
                elif choice == "4":
                    print("\nThank you for using ATM!")
                    break
                else:
                    print("Invalid choice! Please try again.")

            break
        else:
            attempts -= 1
            print(f"Incorrect PIN! Attempts left: {attempts}")

    if attempts == 0:
        print("\nToo many incorrect attempts. Card blocked!")

atm()