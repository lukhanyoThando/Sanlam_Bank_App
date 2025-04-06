from repositories.AccountRepository import AccountRepository
from events.base import EventPublisher
from events.sns_publisher import publish_to_sns
from exceptions.exceptions import InsufficientFundsException, WithdrawalFailedException
from decimal import Decimal

class BankAccountService:
    def __init__(self, 
                 account_repo: AccountRepository = None, 
                 event_publisher: EventPublisher = None):
        self.account_repo = account_repo or AccountRepository()
        self.event_publisher = event_publisher or publish_to_sns()

    def withdraw(self, account_id: int, amount: Decimal):
        try:
            success = self.account_repo.decrease_balance(account_id, amount)
            if not success:
                self._publish_event(account_id, amount, "FAILED_INSUFFICIENT_FUNDS")
                raise InsufficientFundsException(account_id)

            self._publish_event(account_id, amount, "SUCCESSFUL")
        except Exception as e:
            self._publish_event(account_id, amount, "FAILED_UNKNOWN")
            raise WithdrawalFailedException(account_id)

    def _publish_event(self, account_id, amount, status):
        event = {
            "accountId": account_id,
            "amount": str(amount),
            "status": status
        }
        self.event_publisher.publish(event)
