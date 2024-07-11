from dotenv import load_dotenv
import pymssql
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def get_db_connection():
    return pymssql.connect(db_host, db_user, db_password, db_name)


def fetch_data_from_db(values):
    results = []
    with get_db_connection() as conn:
        with conn.cursor(as_dict=True) as cursor:
            query = """
              SELECT product_name, part_id, product_code, type, invoiced_lines
              FROM FMM_Odoo_Part_Audit
              WHERE part_id = %s
          """
            for value in values:
                cursor.execute(query, (value,))
                row = cursor.fetchone()
                if row:
                    results.append(row)

    return results
