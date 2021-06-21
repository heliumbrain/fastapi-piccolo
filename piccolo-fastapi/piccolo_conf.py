from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry

from config import settings


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
    apps=["home.piccolo_app", "piccolo_admin.piccolo_app"]
)
