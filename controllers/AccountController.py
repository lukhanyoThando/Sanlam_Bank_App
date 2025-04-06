from fastapi import APIRouter, HTTPException, Depends
from services.AccountService import BankAccountService
from dto.Accountschema import WithdrawalRequest
from repositories.AccountRepository import get_account_repository, AccountRepository
from events.sns_publisher import publish_to_sns
from exceptions.exceptions import InsufficientFundsException, WithdrawalFailedException

# Create the router instance
router = APIRouter(
    prefix="/bank",
    tags=["Bank Account"]
)

# Dependency provider for BankAccountService
def get_bank_account_service(
    account_repo: AccountRepository = Depends(get_account_repository),
):
    return BankAccountService(account_repo=account_repo, event_publisher=publish_to_sns)

# This is the correct decorator to use inside controller files
@router.post("/withdraw")
def withdraw(
    req: WithdrawalRequest,
    service: BankAccountService = Depends(get_bank_account_service)
):
    try:
        service.withdraw(req.account_id, req.amount)
        return {"message": "Withdrawal successful"}
    except InsufficientFundsException:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    except WithdrawalFailedException:
        raise HTTPException(status_code=500, detail="Withdrawal failed due to an internal error")
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected error occurred")
