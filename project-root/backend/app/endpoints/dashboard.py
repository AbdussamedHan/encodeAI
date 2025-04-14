# backend/app/endpoints/dashboard.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard():
    return {"message": "Dashboard endpoint placeholder"}
