from typing import Dict

from piccolo.apps.user.tables import BaseUser
from piccolo.columns import JSON, ForeignKey, Integer, Numeric, Varchar
from piccolo.table import Table


class Product(Table):
    name: str = Varchar()
    quantity: int = Integer()
    price: int = Numeric(digits=(5, 2))
    details: Dict = JSON()
    author: BaseUser = ForeignKey(references=BaseUser)
