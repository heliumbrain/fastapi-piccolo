from config import settings
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": settings.postgres_db,
        "user": settings.postgres_user,
        "password": settings.postgres_user,
        "host": settings.postgres_host,
        "port": settings.postgres_port,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "product.piccolo_app",
        "piccolo_admin.piccolo_app",
        "piccolo.apps.user.piccolo_app",
        "piccolo_api.session_auth.piccolo_app",
    ]
)
