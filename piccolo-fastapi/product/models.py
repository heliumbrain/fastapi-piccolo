from pydantic import BaseModel

"""
Pydantic model used for validation of the request data in
POST:/products endpoint
"""


class PydanticProductIn(BaseModel):
    name: str
    quantity: int
    price: float


"""
Pydantic model defining the data Product data to be returned in the
response of POST:/products and GET:/products
"""


class PydanticProductOut(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
