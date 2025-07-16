from fastapi import APIRouter
from app.schemas.product_schema import Product

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[Product])
async def list_products():
    return []
