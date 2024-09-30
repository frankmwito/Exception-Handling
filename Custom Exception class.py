# custom exception class

class InsufficientFundsError(Exception):
    def __init__(self, message = "Insufficient funds to complete the transaction. "):
        self.message = message
        super().__init__(self.message)
        
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.balance = balance
        self.account_number = account_number

    def deposit(self):
        try:
            amount = float(input("Enter the amount you wish to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
            else:
                print("Invalid amount. Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you wish to withdraw: "))
            if amount <= 0:
                raise ValueError("Invalid amount. Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientFundsError(f"Insufficient funds. Your balance is ${self.balance:.2f}.")
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        except InsufficientFundsError as e:
            print(e)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")

# Test the BankAccount class and the custom exception
account = BankAccount(account_number="123456789", balance=500)

# Depositing money
account.deposit()

# Trying to withdraw more money than the balance
account.withdraw()
        
        