import typing as t

from fastapi import FastAPI
from piccolo.apps.user.tables import BaseUser
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase
from product.piccolo_app import APP_CONFIG
from product.routers import product_router
from product.tables import Product
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(tables=[Product], site_name="FastAPI + Piccolo - Admin"),
        ),
    ],
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Don't allow all in production, only for testing purposes!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


session_auth = (
    AuthenticationMiddleware(
        app,
        backend=SessionsAuthBackend(
            auth_table=BaseUser,
            session_table=SessionsBase,
            cookie_name="piccoloauth",
            admin_only=True,
            superuser_only=False,
            active_only=True,
        ),
    ),
)


app.include_router(product_router)


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
