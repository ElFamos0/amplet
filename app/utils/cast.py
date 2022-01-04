# On définis un convertisseur pour éviter des erreurs 404
def conversion(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default