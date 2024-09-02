#!/usr/bin/env python3
# This line specifies that the script should be run using Python 3.

class Checkbook:
    def __init__(self):
        # Initialize the Checkbook with a balance of 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Add the deposit amount to the balance if it's positive
        if amount <= 0:
            print("Please enter a positive amount to deposit.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Subtract the withdrawal amount from the balance if it's positive and funds are sufficient
        if amount <= 0:
            print("Please enter a positive amount to withdraw.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Display the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Main function to handle user interaction
    cb = Checkbook()  # Create an instance of Checkbook
    while True:
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting. Have a great day!")
            break
        elif action == 'deposit':
            try:
                # Prompt user for deposit amount and attempt to process it
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                # Prompt user for withdrawal amount and attempt to process it
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            # Display the current balance
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Entry point for the script
    main()