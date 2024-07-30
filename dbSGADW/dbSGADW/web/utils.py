# utils.py
import MySQLdb
from django.conf import settings

def obtener_tablas():
    db = MySQLdb.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        db=settings.DATABASES['default']['NAME']
    )
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]
    db.close()
    return tables

def extraer_numero_de_tabla(tabla):
    import re
    match = re.search(r'S(\d+)_0', tabla)
    return match.group(1) if match else tabla
