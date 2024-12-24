from fastapi import FastAPI
import os
from importlib import import_module
from app.db.base import init_db

app = FastAPI(
    title="Library API",
    description="API для управления библиотекой",
    version="1.0.0"
)

init_db()

# Автоматическое подключение маршрутов из папки routes
for filename in os.listdir("app/api"):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # Убираем расширение .py
        module = import_module(f"app.api.{module_name}")
        app.include_router(module.router, prefix=f"/{module_name}", tags=[module_name.capitalize()])