# Verificador de Seguridad de Enlaces

Este programa es un verificador de seguridad de enlaces que utiliza la API de VirusTotal para analizar enlaces y proporcionar recomendaciones de seguridad. Está diseñado para ser fácil de usar, especialmente para adultos mayores, y cuenta con una interfaz gráfica amigable.

## Características

- Verifica enlaces a través de la API de VirusTotal.
- Proporciona recomendaciones de seguridad en caso de encontrar enlaces sospechosos.
- Opción para abrir una cuenta gratuita en Proton VPN.
- Menú contextual para pegar enlaces fácilmente.
- Interfaz gráfica amigable con botones de gran tamaño y texto legible.

## Requisitos

Para ejecutar este programa, necesitarás:

- Python 3.x
- Las siguientes bibliotecas de Python:
  - `requests`
  - `tkinter`

### Instalación

1. **Instalar Python**: Si no tienes Python instalado, descárgalo e instálalo desde [python.org](https://www.python.org/downloads/).

2. **Clonar el repositorio** (opcional): Si deseas obtener la última versión del código fuente, puedes clonar este repositorio usando Git:

   ```bash
   git clone https://github.com/S4mma3l/VPN.git
   cd verificador_enlaces

3. **Configurar la clave API de VirusTotal**:

    Regístrate en VirusTotal y obtén una clave API gratuita.

    Crea un archivo llamado key.py en el mismo directorio que tu script y agrega tu clave API:
    ```bash
    VIRUS_TOTAL = 'tu_clave_api_aqui'

**Uso**

    Ingresa el enlace que deseas verificar en el campo de entrada.
    Haz clic en el botón "Verificar Enlace".
    Si el enlace es sospechoso, se mostrarán recomendaciones de seguridad.
    Si deseas crear una cuenta en Proton VPN, haz clic en el botón correspondiente.