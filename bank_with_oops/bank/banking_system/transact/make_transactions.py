"""
    Perform Transactions  (Polymorphism)
"""
from bank_with_oops.bank.banking_system.account_types.account_types import SavingsAccount, CheckingAccount


def perform_transaction(account, transaction_type, amount):
    if transaction_type == 'deposit':
        account.deposit(amount)
    elif transaction_type == 'withdraw':
        account.withdraw(amount)
    else:
        print("Unknown transaction type.")

    print(account)


# Create instances of different account types
savings = SavingsAccount("Alice", 1000)
checking = CheckingAccount("Bob", 500)

# Perform transactions
perform_transaction(savings, 'deposit', 200)
perform_transaction(savings, 'withdraw', 50)
perform_transaction(savings, 'withdraw', 1500)  # Should print an error

perform_transaction(checking, 'deposit', 300)
perform_transaction(checking, 'withdraw', 700)
perform_transaction(checking, 'withdraw', 800)  # Should print an error
