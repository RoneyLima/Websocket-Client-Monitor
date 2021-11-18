from pyfirmata import Arduino, util
import time

Uno = Arduino('COM3')


it = util.Iterator(Uno)
it.start();

#DEFINICAO DE PORTAS 
golpeMaquina =  Uno.get_pin('d:7:i')


# Função leitura do acionamento com debounce time
def AcionamentoMaquina():
    estadoBotao = False
    estadoRet = False
    estadoAnterior = 0

    time.sleep(0.1)
    estadoBotao = golpeMaquina.read()
    
    if estadoBotao and (estadoBotao != estadoAnterior):
        estadoAnterior = estadoBotao
        estadoRet = True
        return estadoRet
    else:
        estadoAnterior = estadoAnterior
        estadoRet = False
        return 


def Funcionamento():

    print("Programa Iniciado.")

    quantidade_maxima_golpes = 10
    contador_de_golpes = 0

    while contador_de_golpes < quantidade_maxima_golpes: 

        if AcionamentoMaquina():
            contador_de_golpes += 1
            print("GOLPES: " + str(contador_de_golpes))


Funcionamento()