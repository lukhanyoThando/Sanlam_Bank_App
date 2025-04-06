from sqlalchemy.orm import Session
from models.Account import Account
from sqlalchemy import update
from exceptions.exceptions import AccountNotFoundException

# Dependency injection for session
def get_account_repository(db: Session):
    return AccountRepository(db)

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_account(self, account_id: int):
        account = self.db.query(Account).filter(Account.id == account_id).first()
        if not account:
            raise AccountNotFoundException(account_id)
        return account

    def decrease_balance(self, account_id: int, amount):
        account = self.get_account(account_id)
        if account.balance < amount:
            return False
        account.balance -= amount
        self.db.commit()
        return True
