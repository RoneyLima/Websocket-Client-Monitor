from flask import Flask, jsonify, request
from pyfirmata import Arduino, util
import time
from flask_socketio import SocketIO
# from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")
# CORS(app, resources={r"/*": {"origins": "*"}})

Uno = Arduino('COM4')

it = util.Iterator(Uno)
it.start();

    # millis = int(round(time.time()*1000))


#DEFINICAO DE PORTAS 
golpeMaquina =  Uno.get_pin('d:7:i')
luzFuncionamento =  Uno.get_pin('d:10:o')


# Função leitura do acionamento com debounce time
def AcionamentoMaquina():
    estadoBotao = False
    estadoRet = False
    estadoAnterior = 0

    time.sleep(0.05)
    estadoBotao = golpeMaquina.read()
    
    if estadoBotao and (estadoBotao != estadoAnterior):
        estadoAnterior = estadoBotao
        estadoRet = True
        return estadoRet
    else:
        estadoAnterior = estadoAnterior
        estadoRet = False
        return 


def PararMaquina():
    print("Acionada a parada para inspeção.")
    exit()

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on( 'connection')
def connectionMess():
    print("Conectado")

@app.route('/', methods = ['GET'])

def Funcionamento():
    
    print("Programa Iniciado.")

    quantidade_maxima_golpes = 10
    contador_de_golpes = 0

    while contador_de_golpes < quantidade_maxima_golpes:
       
        if AcionamentoMaquina():
            contador_de_golpes += 1
            # return jsonify(contador_de_golpes)
            return jsonify({"contagem de golpes: ": contador_de_golpes})




if __name__ == "__main__":
        socketio.run(app)

    


        


                

                
            




# def coisa():
#     for e in <= 2:
#     maquinaLigada = estadoMaquina.read()

#     while True:
#         time.sleep(1)
#         print(maquinaLigada)

# while maquinaLigada:
#     time.sleep(0.2)
    
#     acionamento = acionamentoGolpe.read()
#     if acionamento:
#         print(maquinaLigada) 
#     else:
#         print("Nada")
        


    # contador = 0

    # Btn = Uno.digital[7].read()

    # if Btn:
    #         contador += 1
    
    # print(contador)
