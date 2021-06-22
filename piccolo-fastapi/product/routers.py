from http.client import HTTPConnection
from typing import List
from fastapi import Depends, Request

from fastapi.routing import APIRouter

from .models import PydanticProductIn, PydanticProductOut
from .tables import Product
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.middleware import SessionsAuthBackend

# Create a product router that can later be included in FastAPI
product_router = APIRouter()

session_auth = SessionsAuthBackend(admin_only=True)

async def session_admin():
    await session_auth.authenticate() # TODO: HOW TO FIX THIS SHIT?

"""
Defining the routes for the product_router.
Note that the decorator calls the product_router and not the FastAPI app directly
"""


@product_router.get("/products/", response_model=List[PydanticProductOut])
async def get_products():
    return await Product.select().order_by(Product.id).run()


@product_router.post("/products/", response_model=PydanticProductOut)
async def create_product(product: PydanticProductIn, user: BaseUser = Depends(session_admin)):

    product = Product(**product.__dict__)
    await product.save().run()
    return PydanticProductOut(**product.__dict__)


## TODO: Add routes for DELETE and PUT