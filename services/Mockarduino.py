import time

def arduinoMockup():
    contador = 0
    while contador <= 10:
        time.sleep(2)
        sio.emit('contagem', contador)
        print(contador)
        contador += 1
    