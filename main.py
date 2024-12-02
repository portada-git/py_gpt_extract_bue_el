from extractor import ShipInfoExtractor
import json
import os

def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo de texto
    Args:
        nombre_archivo (str): Ruta al archivo a leer
    Returns:
        str: Contenido del archivo o None si hay error
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return None

def main():
    # Verificar que existe la API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: No se encontró la API key de OpenAI en las variables de entorno")
        return
    
    # Crear instancia del extractor
    extractor = ShipInfoExtractor()
    
    # Leer el archivo de texto
    texto = leer_archivo(nombre_archivo)
    
    if texto is None:
        return
    
    # Extraer información
    resultado = extractor.extraer_informacion(texto)
    
    # Imprimir resultado
    if resultado:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    else:
        print("No se pudo procesar la nota")

if __name__ == "__main__":
    nombre_archivo = 'txts/bue_en_08.txt'
    main()
