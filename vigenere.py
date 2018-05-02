from __future__ import print_function
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    mensaje = input('Ingrese mensaje: ')
    key = input('Ingresa key [alphanumerica]: ')
    modo = input('Encriptar/Desencriptar [e/d]: ')

    if modo.lower().startswith('e'):
        modo = 'encripta'
        mensajet = encriptarMensaje(key, mensaje)
    elif modo.lower().startswith('d'):
        modo = 'desencripta'
        mensajet = desencriptarMensaje(key, mensaje)

    print('\nMensaje %sdo :' % modo.title())
    print(mensajet)

def encriptarMensaje(key, mensaje):
    return proceso(key, mensaje, 'encripta')

def desencriptarMensaje(key, mensaje):
    return proceso(key, mensaje, 'desencripta')

def proceso(key, mensaje, modo):
    mensajet = []
    keyIndex = 0
    key = key.upper()

    for x in mensaje:
        num = LETRAS.find(x.upper())
        if num != -1:
            if modo == 'encripta':
                num += LETRAS.find(key[keyIndex])
            elif modo == 'desencripta':
                num -= LETRAS.find(key[keyIndex])

            num %= len(LETRAS)

            if x.isupper():
                mensajet.append(LETRAS[num])
            elif x.islower():
                mensajet.append(LETRAS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            mensajet.append(symbol)
    return ''.join(mensajet)

if __name__ == '__main__':
    main()
