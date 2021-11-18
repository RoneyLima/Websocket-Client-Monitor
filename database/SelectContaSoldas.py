import json
from sqlalchemy import select
from database.model.Core_Conta_Soldas import conta_soldas

def get_soldagens():


    try:
        sel = select([conta_soldas])

        retorno = sel.execute()

        

        return retorno
    except Exception as e:
        print("Erro ao selecionar dados", e)


