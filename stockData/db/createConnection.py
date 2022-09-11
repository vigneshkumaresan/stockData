from sqlalchemy import create_engine
from constant import constants


def createEngine():
    db = create_engine('postgresql://'+constants.USERNAME+":"+constants.PASSWORD+"@"+constants.DB_URL+":"+constants.PORT+"/"+constants.DB_NAME)
    return db

def getConnection():
    db=createEngine()
    conn = db.connect()
    return conn


def closeConnection(conn):
    conn.close()



