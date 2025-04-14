# backend/app/services/data_aggregation.py

import httpx
from fastapi import HTTPException

BASE_URL = "https://api.llama.fi"
COINS_BASE_URL = "https://coins.llama.fi"  # Use this for coin-related endpoints

async def fetch_protocols():
    """
    Fetch a list of protocols from DeFi Llama along with their TVL.
    Endpoint: GET /protocols (no parameters required).
    """
    url = f"{BASE_URL}/protocols"
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=10.0)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error fetching protocols from DeFi Llama: {response.text}",
        )
    
    return response.json()

async def fetch_coin_charts(coins: str):
    """
    Fetch coin charts from DeFi Llama.
    Endpoint: GET /chart/{coins}.
    """
    # Use COINS_BASE_URL for coin-related endpoints
    url = f"{COINS_BASE_URL}/chart/{coins}"
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=10.0)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error fetching coin charts from DeFi Llama: {response.text}",
        )
    
    return response.json()

async def fetch_current_prices(coins: str, search_width: str):
    """
    Fetch current pricing data from the DeFi Llama coins endpoint for the specified token.
    """
    url = f"{COINS_BASE_URL}/prices/current/{coins}"
    params = {"searchWidth": search_width}
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers, timeout=10.0)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error fetching current prices from DeFi Llama: {response.text}"
        )
    
    return response.json()
