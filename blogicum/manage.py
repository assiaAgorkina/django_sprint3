#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def setup_environment():
    """Configure Python path for Django project"""
    # Получаем абсолютный путь к корню проекта
    project_root = Path(__file__).resolve().parent
    # Добавляем в PYTHONPATH:
    # 1. Корень проекта (где manage.py)
    # 2. Родительскую директорию (на случай нестандартной структуры)
    sys.path.extend([
        str(project_root),
        str(project_root.parent),
    ])
    # Для диагностики (можно удалить после проверки)
    if os.getenv('DJANGO_DEBUG_PATH'):
        print("\nPython paths:")
        for p in sys.path:
            print(f"→ {p}")
        print(f"\nWorking directory: {os.getcwd()}")
        print(f"Project root: {project_root}\n")


def main():
    """Run administrative tasks."""
    # Сначала настраиваем окружение
    setup_environment()
    # Затем запускаем Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc  
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
