from pydantic import BaseModel
from decimal import Decimal

class WithdrawalRequest(BaseModel):
    account_id: int
    amount: Decimal
