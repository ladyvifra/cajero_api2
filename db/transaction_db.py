#Bloque 1: definición de TransactionInDB

from datetime import datetime
from pydantic import BaseModel

class TransactionInDB(BaseModel): #Clase y atributos 
    id_transaction: int = 0
    username: str
    date: datetime = datetime.now()
    value: int
    actual_balance: int

#Bloque 2: definición de la base de datos ficticia y una función

database_transactions = []  #Se define una lista vacia
generator = {"id":0}   # se define un diciconario, que arranca con id:0

def save_transaction(transaction_in_db: TransactionInDB): #Definimos una función para guardar un transacción en la base de datos ficticia.
    generator["id"] = generator["id"] + 1      #Se guardan cada una  delas transacciones, se guarda en el dicc un nuevo id
    transaction_in_db.id_transaction = generator["id"] 
    database_transactions.append(transaction_in_db)
    return transaction_in_db  #retorna toda la transacción