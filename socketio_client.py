import socketio
import time
import json
import sys
import math
from database.SelectContaSoldas import get_soldagens
from database.UpdateContaSoldas import update_contagem, update_eletrodo

# TODO: chegar no limite do eletrodo
# maquina desliga e indicar qual eletrodo chegou no limite
# fazer o controle de substituição do Eletrodo

sio = socketio.Client()

sio.connect('http://127.0.0.1:5000/')


@sio.on('front_iniciado')
def get_dados_front():
    soldas_json = json_contagem()
    sio.emit('contagem_inicial', json.dumps(soldas_json))


@sio.on('iniciar_contagem')
def iniciando_contagem_golpes(limite_recebido):
    print('Contando soldas até o limite de : ', limite_recebido)
    contador = 1
    global programa
    programa = 0
    print(type(limite_recebido))
    lim = int(limite_recebido)
    while contador <= lim:
        if programa < 1:
            time.sleep(1)
            sio.emit('emit_contagem', contador)
            print(contador)
            contador += 1
        else:
            update_contagem(contador)
            contador = 1
    else:
        print("Atingido limite de golpes")
        update_contagem(contador)
    novo_limite = math.ceil(lim * 0.2)
    sio.emit('limite_atingido', novo_limite)
    contador = 1


@sio.on('maquina_desligada')
def maquina_desligada():
    print("Recebido Maquina Desligada")
    global programa
    programa = 1


@sio.event
def eletrodo_substituido(eletrodo):
    print(eletrodo)
    update_eletrodo(eletrodo, 0)


def json_contagem():
    
    soldas_cont_inicial = get_soldagens()
    eletrodos_obj = []

    for linha in soldas_cont_inicial:

        unico = (linha['soldagens'])
        print(unico)
        eletrodos_obj.append(unico)

    return eletrodos_obj
