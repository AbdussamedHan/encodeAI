# backend/app/endpoints/defillama.py

from fastapi import APIRouter, Path, Query
from backend.app.services.data_aggregation import (
    fetch_protocols,
    fetch_current_prices,
    fetch_coin_charts,
)

router = APIRouter()

@router.get("/protocols")
async def get_protocols():
    """
    Retrieve a list of protocols from the DeFi Llama API.
    """
    data = await fetch_protocols()
    return {"message": "Protocols fetched successfully", "data": data}


@router.get("/chart/{coins}")
async def get_coin_charts(
    coins: str = Path(..., description="Token identifier in the form {chain}:{address}")
):
    """
    Retrieve coin chart data from DeFi Llama for a specified token.
    Example: /defillama/chart/ethereum:0xABC... 
    """
    data = await fetch_coin_charts(coins=coins)
    return {"message": "Coin charts fetched successfully", "data": data}


@router.get("/prices/current/{coins}")
async def get_current_prices(
    coins: str = Path(..., description="Token identifier in the form {chain}:{address}"),
    search_width: str = Query("6h", description="Time range for price data, e.g., 6h, 12h")
):
    """
    Retrieve current pricing data from DeFi Llama for a specified token.
    Example: /defillama/prices/current/ethereum:0xABC...?search_width=6h
    """
    data = await fetch_current_prices(coins=coins, search_width=search_width)
    return {"message": "Prices fetched successfully", "data": data}
