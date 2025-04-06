class AccountNotFoundException(Exception):
    def __init__(self, account_id):
        super().__init__(f"Account {account_id} not found")

class InsufficientFundsException(Exception):
    def __init__(self, account_id):
        super().__init__(f"Insufficient funds in account {account_id}")

class WithdrawalFailedException(Exception):
    def __init__(self, account_id):
        super().__init__(f"Withdrawal failed for account {account_id}")
