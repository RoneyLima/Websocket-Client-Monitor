from sqlalchemy import update
from sqlalchemy.sql.expression import bindparam
from database.model.Core_Conta_Soldas import conta_soldas, engine
from database.SelectContaSoldas import *

conn = engine.connect()


def update_eletrodo(e1, s1):


    up = update(conta_soldas).where(conta_soldas.c.eletrodo == (f'{e1}')).values(soldagens=(f'{s1}'))

    result = conn.execute(up)

    return result.rowcount


def update_contagem(nova_contagem):
    contagem_armazenada = get_soldagens()

    for eletrodo in contagem_armazenada:
        s = eletrodo[2]
        s += nova_contagem
        e = eletrodo[1]
        # print('Vai alterar ', e, s)
        try:
            update_eletrodo(e, s)

        except Exception as e:
            print(e)

