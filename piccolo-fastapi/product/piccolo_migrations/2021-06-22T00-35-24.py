from decimal import Decimal

from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.base import OnDelete, OnUpdate
from piccolo.columns.column_types import JSON, ForeignKey, Integer, Numeric, Varchar
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class BaseUser(Table, tablename="piccolo_user"):
    pass


ID = "2021-06-22T00:35:24"
VERSION = "0.21.1"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="product")

    manager.add_table("Product", tablename="product")

    manager.add_column(
        table_class_name="Product",
        tablename="product",
        column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    manager.add_column(
        table_class_name="Product",
        tablename="product",
        column_name="quantity",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 0,
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    manager.add_column(
        table_class_name="Product",
        tablename="product",
        column_name="price",
        column_class_name="Numeric",
        column_class=Numeric,
        params={
            "default": Decimal("0"),
            "digits": (5, 2),
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    manager.add_column(
        table_class_name="Product",
        tablename="product",
        column_name="details",
        column_class_name="JSON",
        column_class=JSON,
        params={
            "default": "{}",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    manager.add_column(
        table_class_name="Product",
        tablename="product",
        column_name="author",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": BaseUser,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "default": None,
            "null": True,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    return manager
