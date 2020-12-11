from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):  #Definición  de clase en python En pyhton la herencia se hace class nombreclase(clasePadre)
    username: str           #Atributos de la clase
    password: str
    balance: int


#Bloque 2 :Definición de la base de datos ficticia por medio de directorios

database_users = Dict [str, UserInDB]  # Nos dice qeu es un diciconario que tendrá un string y un objeto de tipo UserInDB

database_users = {   #instancias creadas y guardadas en un diccionario
    "camilo24": UserInDB(**{"username":"camilo24", ## Los ** hacen un mapeo
                            "password": "root",
                            "balance":12000} ),

    "andres18": UserInDB(**{"username":"andres10",
                            "password": "hola",
                            "balance":34000} ),
    }

    #Definición de funciones sobr ela base de datos ficticia

def get_user(username:str):
    if username in database_users.keys():  #Busca el username en la base, si lo encuentra se retorna el valor
        return database_users[username]
    else:
        return None    #Si no lo encuentra, no retorna nada


def update_user(user_in_db: UserInDB): #Se recibe un dato userInDB 
    database_user[user_in_db.username] = user_in_db #Voy al diciconario y busco la llave
    return user_in_db
