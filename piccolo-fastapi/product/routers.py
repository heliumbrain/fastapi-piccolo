from http.client import HTTPConnection
from typing import List

from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase
from product import piccolo_app
from starlette.authentication import AuthenticationError
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import HTTPConnection

from .models import PydanticProductIn, PydanticProductOut
from .tables import Product

# Create a product router that can later be included in FastAPI
product_router = APIRouter()

auth = AuthenticationMiddleware(
    piccolo_app,
    backend=SessionsAuthBackend(
        admin_only=True,
        cookie_name="id",
        auth_table=BaseUser,
        session_table=SessionsBase,
        active_only=False,
        superuser_only=False,
    ),
)

"""
Defining the routes for the product_router.
Note that the decorator calls the product_router and not the FastAPI app directly
"""


@product_router.get("/products/", response_model=List[PydanticProductOut])
async def get_products():
    return await Product.select().order_by(Product.id).run()


@product_router.post("/products/", response_model=PydanticProductOut)
async def create_product(product: PydanticProductIn, conn: HTTPConnection):
    try:
        await auth.backend.authenticate(conn)
        product = Product(**product.__dict__)
        await product.save().run()
        return PydanticProductOut(**product.__dict__)
    except AuthenticationError:
        return JSONResponse(status_code=401, content="401 - Unauthorized")


## TODO: Add routes for DELETE and PUT
