# Bloque 1: lo primero que se realiza es importar los modelos creados

from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut

from models.transaction_models import TransactionIn,TransactionOut

#Bloque 2: se importan algunos paquetes adicionales y se crea la api (un herramienta que agrupará las operaciones):
import datetime
from fastapi import FastAPI
from fastapi import HTTPException


api = FastAPI()  # Crear la aplicación 


###############################################
from fastapi.middleware.cors import CORSMiddleware  #Validar los orígenes para verificar que se puedne comunicar

#Se escriben los hosts qeu va a acpetar
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com","http://127.0.0.1:8000",
    "http://localhost", "http://localhost:8080","https://cajero-app66.herokuapp.com"
]
api.add_middleware( #añade los arígenes a la api para permitir que desd eotras direcciones se puedan hacer peticiones.
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
####################################################################

#Bloque 3: se implementa la funcionalidad auth_user:

@api.post("/user/auth/")  #La url conm eñ método entra  ala función
async def auth_user(user_in: UserIn): #asincrónico (como hilo), permite tener varias cosas trabajando en paralelo
    user_in_db = get_user(user_in.username)
    if user_in_db == None:  # Identificar si el usuario existe en la base de datos
        raise HTTPException(status_code=404,detail="El usuario no existe") #Lanzo una excepción 
    if user_in_db.password != user_in.password:  #si el usuario está y la contraseña es igual se autentica, de lo  contrario no
        return {"Autenticado": False}
    return {"Autenticado": True}

#4: se implementa la funcionalidad get_balance:

@api.get("/user/balance/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out


#Bloque 5: se implementa la funcionalidad make_transaction:
# Parte1

@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None: 
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400, 
    detail="Sin fondos suficientes")
