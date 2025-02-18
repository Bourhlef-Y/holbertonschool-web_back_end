import re

def filter_datum(fields, redaction, message, separator):
    """Remplace les valeurs des champs spécifiés par une chaîne de redaction"""
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
