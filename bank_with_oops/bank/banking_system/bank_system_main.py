from bank_with_oops.bank.banking_system.account_types.account_types import SavingsAccount, CheckingAccount
from bank_with_oops.bank.banking_system.transact.make_transactions import perform_transaction

if __name__ == "__main__":
    # Create a SavingsAccount and CheckingAccount
    savings = SavingsAccount("Alice", 1000)
    checking = CheckingAccount("Bob", 500)

    # Apply interest to the savings account
    savings.apply_interest()
    print(savings)

    # Perform various transactions
    perform_transaction(savings, 'deposit', 100)
    perform_transaction(savings, 'withdraw', 200)

    perform_transaction(checking, 'withdraw', 700)
    perform_transaction(checking, 'withdraw', 500)
