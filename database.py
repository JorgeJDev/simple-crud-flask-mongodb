from os import environ
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()

URI_CONNECT = environ.get('URI_CONNECT')
ca = certifi.where()

def dbConnect():
    try:
        client = MongoClient.connect(URI_CONNECT, tlsCAFile=ca)
        db = client ["dbb_products_app"]
    except ConnectionError:
        print('Error de conexion con BBDD')
    return db