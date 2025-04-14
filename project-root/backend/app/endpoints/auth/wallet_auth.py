# backend/app/endpoints/auth/wallet_auth.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from eth_account.messages import encode_defunct
from eth_account import Account

router = APIRouter()

class WalletLoginRequest(BaseModel):
    account: str
    signature: str
    message: str

@router.post("/login")
def wallet_login(login_data: WalletLoginRequest):
    """
    Verify the signature from the user's MetaMask wallet.
    """
    # Create an encoded message from the provided text
    encoded_message = encode_defunct(text=login_data.message)
    
    # Recover the address from the signature
    try:
        recovered_address = Account.recover_message(encoded_message, signature=login_data.signature)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not verify signature: {e}")

    # Ensure the recovered address matches the one provided by the client
    if recovered_address.lower() != login_data.account.lower():
        raise HTTPException(status_code=400, detail="Signature verification failed.")

    # If verification is successful, you might generate a session token or JWT.
    # For now, return a success response.
    return {"message": "Wallet authentication successful", "account": login_data.account}
