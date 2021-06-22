from typing import List

from fastapi.routing import APIRouter

from .models import PydanticProductIn, PydanticProductOut
from .tables import Product

# Create a product router that can later be included in FastAPI
product_router = APIRouter()


"""
Defining the routes for the product_router.
Note that the decorator calls the product_router and not the FastAPI app directly
"""


@product_router.get("/products/", response_model=List[PydanticProductOut])
async def get_products():
    return await Product.select().order_by(Product.id).run()


@product_router.post("/products/", response_model=PydanticProductOut)
async def create_product(product: PydanticProductIn):

    product = Product(**product.__dict__)
    await product.save().run()
    return PydanticProductOut(**product.__dict__)


## TODO: Add routes for DELETE and PUT
