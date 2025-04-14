# backend/app/main.py

from fastapi import FastAPI
from backend.app.endpoints import portfolio, dashboard, defillama
from backend.app.endpoints.auth.wallet_auth import router as wallet_auth_router

app = FastAPI(title="DeFi Advisory Platform API", version="0.1")

# Register routers for different endpoints
app.include_router(dashboard.router, prefix="/dashboard")
# app.include_router(portfolio.router, prefix="/portfolio")
app.include_router(defillama.router, prefix="/defillama")

# Optionally, add authentication endpoints:
# from backend.app.endpoints.auth import wallet_auth, exchange_auth
app.include_router(wallet_auth_router, prefix="/auth/wallet")
# app.include_router(exchange_auth.router, prefix="/auth/exchange")

@app.get("/")
def read_root():
    return {"message": "Welcome to the DeFi Advisory Platform API"}

# Run the app using Uvicorn if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
