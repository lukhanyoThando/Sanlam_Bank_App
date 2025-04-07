from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.AccountService import BankAccountService
from dto.Accountschema import WithdrawalRequest
from repositories.AccountRepository import get_account_repository, AccountRepository
from events.sns_publisher import publish_to_sns
from exceptions.exceptions import InsufficientFundsException, WithdrawalFailedException

router = APIRouter()
# Create the router instance without the prefix
router = APIRouter(
    tags=["Bank Account"]  
)

# Dependency provider for BankAccountService
def get_bank_account_service(
    account_repo: AccountRepository = Depends(get_account_repository),
):
    return BankAccountService(account_repo=account_repo, event_publisher=publish_to_sns)

@router.post("/bank/withdraw", response_model=None)
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")
