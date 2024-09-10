# Ataque BEAST

Esta implementación es una simulación del ataque BEAST (Browser Exploit Against SSL/TLS), diseñada para demostrar cómo se podría realizar un ataque de descifrado en un entorno vulnerable que utilice el modo de cifrado AES-CBC.

## Descripción del Proyecto

El objetivo de este proyecto es simular el ataque BEAST, mostrando cómo un atacante podría explotar la vulnerabilidad en el cifrado CBC (Cipher Block Chaining) en SSL/TLS para descifrar datos de un servidor vulnerable.

El servidor simulado envía un mensaje cifrado, denominado `FLAG`, que debe ser descifrado por el atacante aprovechando la vulnerabilidad del modo CBC. 

El resultado exitoso del ataque se muestra en las imágenes incluidas en el repositorio.

## Requisitos

- **Docker**: Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
- **Python 2.7**: El ataque y el servidor están implementados en Python 2.7, por lo que es necesario tener esta versión instalada en el entorno.

## Instrucciones para la Implementación

### 1. Clona el repositorio

```bash
git clone https://github.com/aidamgl/Ataque-Beast.git
cd Ataque-Beast
```
### 2. Inicia los servicios con Docker Compose
Para iniciar el servidor y el atacante en contenedores separados, ejecuta:
```bash
docker-compose up
```
### 3. Ejecuta los contenedores
Una vez que los servicios están corriendo, abre dos terminales separadas:

- En la primera terminal, ejecuta el servidor:
 ```bash
docker exec -it server bash
python2.7 server.py
```
- En la segunda terminal, ejecuta el ataque:
```bash
docker exec -it attack bash
python2.7 beast-attack.py
```
### 4. Resultados

Si todo ha sido implementado correctamente, el atacante debería poder descifrar el mensaje `FLAG` enviado por el servidor, demostrando el éxito del ataque BEAST. 

## Archivos Principales

- **server.py**: Define una aplicación web utilizando Flask que cifra los datos y los envía como una respuesta HTTP.
- **beast-attack.py**: Código que realiza el ataque BEAST para intentar descifrar los datos cifrados que se obtienen del servidor.

## Notas Importantes

- Esta implementación no representa un escenario real, sino una simulación para fines académicos y de demostración.
- El ataque implementado no compromete servidores reales, sino un entorno controlado diseñado para mostrar cómo funciona teroria de la vulnerabilidad.

## Referencias

Este trabajo se basa en el código original del repositorio [Beast-PoC](https://github.com/mpgn/BEAST-PoC/tree/master).


