# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import binascii
import requests

# Configura la URL del servidor y la clave
server_url = 'https://172.23.0.2:8443/securedata'  # Cambia esto al URL adecuado
key = ''.join(chr(int('00112233445566778899aabbccddeeff'[i:i+2], 16)) for i in range(0, len('00112233445566778899aabbccddeeff'), 2))  # Cambia esto a la clave adecuada

# Verificar tamaño de la clave
def verify_key_size(key):
    if len(key) not in [16, 24, 32]:
        raise ValueError("Invalid AES key size: must be 16, 24, or 32 bytes")

# Función para desencriptar
def decrypt(key, ciphertext, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')
    except (ValueError, KeyError) as e:
        print("Decryption failed:", e)
        return None

# Función para realizar el ataque BEAST
def perform_beast_attack(server_url, key):
    try:
        # Realizar una solicitud para obtener el texto cifrado
        response = requests.get(server_url, verify=False)
        ciphertext_base64 = response.text.strip()
        print('Ciphertext from server:', ciphertext_base64)
        
        # Decodificar el texto cifrado desde Base64
        try:
            ciphertext = base64.b64decode(ciphertext_base64 + '=' * (-len(ciphertext_base64) % 4))  # Añadir padding si es necesario
        except (TypeError, binascii.Error) as e:
            print("Base64 decoding failed:", e)
            return
        
        iv = ciphertext[:16]  # Suponiendo que el IV es de 16 bytes
        ciphertext = ciphertext[16:]  # Resto del texto cifrado

        # Imprimir IV en formato hexadecimal
        print('IV:', binascii.hexlify(iv))

        # Verificar el tamaño de la clave
        verify_key_size(key)
        
        # Desencriptar el texto cifrado
        plaintext = decrypt(key, ciphertext, iv)
        if plaintext:
            print('Plaintext:', plaintext)
        else:
            print('Failed to guess plaintext.')
            
    except requests.RequestException as e:
        print('Request failed:', e)

if __name__ == "__main__":
    perform_beast_attack(server_url, key)
