# Heartbleed Attack Simulation

Este proyecto está diseñado para simular el ataque Heartbleed, un fallo de seguridad crítico en OpenSSL que permite a un atacante obtener información sensible de la memoria del servidor. Este simulador se utiliza con fines educativos para demostrar cómo funciona el ataque y no debe ser usado para actividades maliciosas.

## Descripción

El ataque Heartbleed se basa en un fallo en la implementación de la extensión de Heartbeat en OpenSSL. El fallo consiste en no verificar correctamente el tamaño especificado en el campo de Payload Length con respecto al tamaño real del Payload enviado. Esto permite a un atacante obtener datos adicionales almacenados en la memoria del servidor, que pueden incluir información sensible como claves privadas.

## Requisitos

- Docker
- Docker Compose

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/heartbleed-simulation.git
   cd heartbleed-simulation
