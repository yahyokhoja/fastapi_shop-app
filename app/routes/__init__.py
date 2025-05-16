from .auth import router as auth_router
from .store import router as store_router
from .user import router as user_router
from .shop import router as shop_router
from .product import router as product_router
from .order import router as order_router





__all__ = [
    "auth_router",
    "store_router",
]
