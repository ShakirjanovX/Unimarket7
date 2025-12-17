"""Настройка пути для импортов"""
import sys
from pathlib import Path

# Добавляем родительскую директорию в path для импортов
sys.path.insert(0, str(Path(__file__).parent.parent))
