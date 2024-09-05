# -*- coding: utf-8 -*-
from flask import Flask, Response
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

app = Flask(__name__)

def hex_to_bytes(hex_str):
    """Convierte una cadena hexadecimal en bytes."""
    return bytearray.fromhex(hex_str)

# Configura la clave y el IV
key = hex_to_bytes('00112233445566778899aabbccddeeff')  # Clave de 16 bytes (128 bits)
iv = os.urandom(16)  # IV de 16 bytes (128 bits)

@app.route('/securedata')
def secure_data():
    # Datos que deseas cifrar
    plaintext = 'FLAG=@AIDAMGL'

    # Cifra los datos
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

    # Combina IV y ciphertext, luego codifica en Base64
    iv_ciphertext = iv + ciphertext
    iv_ciphertext_base64 = base64.b64encode(iv_ciphertext).decode('utf-8')

    # Envía el ciphertext codificado en Base64 como respuesta
    return Response(iv_ciphertext_base64, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='172.23.0.2', port=8443, ssl_context=('server.crt', 'server.key'))
