# RENIEC Discord Bot

Bot de Discord desarrollado en Python para consultar información ciudadana mediante la API REST de RENIEC.

El bot permite realizar búsquedas por DNI utilizando comandos slash (`/dni`) y muestra los resultados mediante embeds con formato institucional.

Necesidad de python 3.13

# API Utilizada

Proveedor API:

https://decolecta.com/profile/

Documentación oficial:

https://decolecta.gitbook.io/docs

Endpoint utilizado:

```http
GET https://api.decolecta.com/v1/reniec/dni?numero=46027897
```

# Instalación

## 1. Clonar repositorio

```powershell
git clone https://github.com/KernelX-debug/reniec-api-gratuita.git
cd reniec-api-gratuita
```

## 2. Instalar dependencias

```powershell
py -3.13 -m pip install -r requirements.txt
```

## 3. Configurar variables de entorno

**Crear archivo .env**

```env
DISCORD_TOKEN=TU_TOKEN_DISCORD
RENIEC_TOKEN=TU_TOKEN_RENIEC
```

# Ejecución

```powershell
py -3.13 reniec.py
```

**Comando Disponible**

`/dni`

Consulta información asociada a un DNI.

Ejemplo:

`/dni 46027897`

Respuesta:

`Nombres: ERACLEO JUAN`

`Apellido paterno: HUAMANI`

`Apellido materno: MENDOZA`

`Nombre completo: HUAMANI MENDOZA ERACLEO JUAN`

`Número de documento: 46027897`
