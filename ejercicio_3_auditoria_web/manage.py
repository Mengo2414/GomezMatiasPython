#!/usr/bin/env python3
"""Utilidad de línea de comandos para el proyecto Django."""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sustentabilidad.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se encontró Django. Instalalo con: python -m pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
