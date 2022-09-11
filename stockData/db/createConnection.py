from sqlalchemy import create_engine
from constant import constants
import psycopg2

def createEngine():
    db = create_engine('postgresql://'+constants.USERNAME+":"+constants.PASSWORD+"@"+constants.DB_URL+":"+constants.PORT+"/"+constants.DB_NAME)
    return db

def getConnection():
    db=createEngine()
    conn = db.connect()
    return conn


def closeConnection(conn):
    conn.close()

def pgConnection():
    conn=psycopg2.connect('postgresql://'+constants.USERNAME+":"+constants.PASSWORD+"@"+constants.DB_URL+":"+constants.PORT+"/"+constants.DB_NAME)
    return conn


def pgCursor():
    connection_obj=pgConnection()
    cursor_obj=connection_obj.cursor()
    return connection_obj,cursor_obj


def pgClose(connection_obj,cursor_obj):
    connection_obj.commit()
    connection_obj.close()


