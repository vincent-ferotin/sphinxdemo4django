"""
Utilitaires dédiés à la base de données.
"""
from django.db import connection


def is_sqlite_empty():
    """
    Vérifie si la base de données SQLite est vide d'une quelconque table (`bool`).
    """
    with connection.cursor() as cursor:
        cursor.execute((""
            "SELECT name FROM sqlite_schema "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%'"))
        table_names = cursor.fetchall()

    return len(table_names) == 0
