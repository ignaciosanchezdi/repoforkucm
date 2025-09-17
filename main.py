
import os

# Función que lista los archivos markdown en el directorio actual
def listar_archivos_markdown():
    archivos = os.listdir(".")
    markdowns = [archivo for archivo in archivos if archivo.endswith(".md")]
    print("\nLISTA DE ARCHIVOS MARKDOWN")
    print("-------------------------")
    for idx, archivo in enumerate(markdowns, 1):
        print(f"{idx}. {archivo}")
    print("-------------------------")
    return markdowns

# Función que muestra el contenido de un archivo markdown seleccionado por el usuario
def mostrar_contenido_archivo(markdowns):
    if not markdowns:
        print("No hay archivos markdown para mostrar.")
        return
    
    #markdowns válido
    num = int(input("\nIntroduce el número del archivo a mostrar: "))
    if 1 <= num <= len(markdowns):
        archivo = markdowns[num-1]
        print(f"\nContenido de {archivo}:")
        print("-------------------------")
        with open(archivo, "r", encoding="utf-8") as f:
            print(f.read())
        print("-------------------------")
    else:
        print("Número inválido.")

# Función principal que muestra el menú y gestiona la interacción con el usuario
def main():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("-------------------------")
        print("1. Lista de archivos markdown")
        print("2. Mostrar contenido de un archivo")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        print("-------------------------")
        if opcion == "1":
            listar_archivos_markdown()
        elif opcion == "2":
            markdowns = listar_archivos_markdown()
            mostrar_contenido_archivo(markdowns)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()