from pydantic_settings import BaseSettings
from typing import Optional
class Settings(BaseSettings):
 """Настройки приложения"""
 # Основные настройки
 PROJECT_NAME: str = "UniMarket"
 VERSION: str = "0.1.0"
 DEBUG: bool = True
 # API настройки
 API_PREFIX: str = "/api/v1"

 class Config:
    env_file = ".env"
    case_sensitive = True
# Создаем глобальный объект настроек
settings = Settings()
