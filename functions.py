

import psycopg2
from config import *

con = psycopg2.connect(
    database=db_name,
    user=user,
    password=password,
    host=host,
    port=port,

)
con.set_client_encoding('UNICODE')
cur = con.cursor()

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


def import_all_from_client():
    result = {}
    namespace = []
    with con.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT * FROM "Client"
            ORDER BY "ID" ASC;
            """
        )
        df = get_unique_numbers(cursor.description)
        for i in df:
            namespace.append(i[0])
        length = len(namespace)
        for data in cursor.fetchall():
            result[data[0]] = {
                namespace[1]: data[1],
                namespace[2]: data[2],
                namespace[3]: data[3],
                namespace[4]: data[4],
                namespace[5]: data[5],
                namespace[6]: data[6]}

    return result

def import_all_from_store():
    result = {}
    namespace = []
    with con.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT * FROM "Store"
            ORDER BY "ID" ASC;
            """
        )
        df = get_unique_numbers(cursor.description)
        for i in df:
            namespace.append(i[0])
        length = len(namespace)
        for data in cursor.fetchall():
            result[data[0]] = {
                namespace[1]: data[1],
                namespace[2]: data[2],
                namespace[3]: data[3],
                namespace[4]: data[4],
                }

    return result


def import_all_from_rent():
    result = {}
    namespace = []
    with con.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT *, 
            TO_CHAR("Rent"."Startdate",'YY Mon DD ') AS start,
            TO_CHAR("Rent"."Enddate",'YY Mon DD ') AS "end" FROM "Rent"
            
            ORDER BY "ID" ASC;
            """
        )
        df = get_unique_numbers(cursor.description)
        for i in df:
            namespace.append(i[0])
        length = len(namespace)
        for data in cursor.fetchall():
            result[data[0]] = {
                namespace[1]: data[1],
                namespace[2]: data[2],
                namespace[5]:   data[5],
                namespace[6]: data[6],
                }

    return result

def insert_into_client(ID, name, adress, phonenumber, requisities, contact, Worktime):
    message=''
    try:
        with con.cursor() as cursor:
            postgres_insert_query = """ INSERT INTO "Client" ("ID", "Name", "Adress", "Phonenumber", "Requisites", "Contact", "Worktime")
                                                   VALUES (%s,%s,%s, %s,%s,%s,%s)"""
            record_to_insert = (ID, name, adress, phonenumber, requisities, contact, Worktime)
            cursor.execute(postgres_insert_query,record_to_insert)
            con.commit()
            message = 'DONE'
            return message
    except:
        message = 'ERROR'
        return message



