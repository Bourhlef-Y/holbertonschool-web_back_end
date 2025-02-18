#!/usr/bin/env python3
"""
Module contenant des fonctions pour filtrer les données sensibles dans les logs
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Remplace les valeurs des champs sensibles par une valeur de redaction"""
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
