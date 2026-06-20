import sys
import os
import datetime
from lexer import lexer, errores_lexicos


def analizar(codigo):
    errores_lexicos.clear()
    lexer.lineno = 1
    lexer.input(codigo)

    resultados = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        resultados.append((tok.type, tok.value, tok.lineno))

    return resultados, list(errores_lexicos)


def generar_log(nombre_apellido, codigo_fuente, resultados, errores, carpeta_salida="."):
    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%d-%m-%Y-%Hh%M")
    nombre_archivo = f"lexico-{nombre_apellido}-{fecha_hora}.txt"
    ruta = os.path.join(carpeta_salida, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("ANALIZADOR LEXICO - C++\n")
        f.write(f"Estudiante: {nombre_apellido}\n")
        f.write(f"Fecha y hora: {ahora.strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        f.write("CODIGO FUENTE ANALIZADO:\n")
        f.write("-" * 60 + "\n")
        f.write(codigo_fuente.rstrip() + "\n")
        f.write("-" * 60 + "\n\n")

        f.write(f"TOKENS RECONOCIDOS ({len(resultados)}):\n")
        f.write("-" * 60 + "\n")
        f.write(f"{'LINEA':<8}{'TOKEN':<18}{'VALOR'}\n")
        f.write("-" * 60 + "\n")
        for tipo, valor, linea in resultados:
            f.write(f"{linea:<8}{tipo:<18}{valor}\n")

        f.write("\n")
        f.write(f"ERRORES LEXICOS ({len(errores)}):\n")
        f.write("-" * 60 + "\n")
        if errores:
            for err in errores:
                f.write(err + "\n")
        else:
            f.write("Ningun error lexico detectado.\n")

    return ruta


def main():
    if len(sys.argv) >= 3:
        # Modo terminal: ya vinieron los datos en el comando
        origen = sys.argv[1]
        nombre_apellido = sys.argv[2]
    else:
        # Modo interactivo: no se pasaron argumentos (ej. doble clic o boton Run)
        # entonces se piden los datos por pantalla.
        print("=== Analizador Lexico C++ ===")
        print("(Sugerencia: tambien puedes correr 'python main.py archivo.cpp TuNombre' por terminal)\n")
        origen = input("Nombre del archivo .cpp a analizar (ej. algoritmo1.cpp): ").strip()
        nombre_apellido = input("Tu nombre y apellido sin espacios (ej. AndieBarreno): ").strip()

    if origen == "--texto":
        print("Pega tu codigo y presiona Ctrl+D (Linux/Mac) o Ctrl+Z+Enter (Windows) al terminar:")
        codigo = sys.stdin.read()
    else:
        if not os.path.isfile(origen):
            print(f"Error: no se encontro el archivo '{origen}'")
            sys.exit(1)
        with open(origen, "r", encoding="utf-8") as f:
            codigo = f.read()

    resultados, errores = analizar(codigo)

    print(f"\nSe reconocieron {len(resultados)} tokens y {len(errores)} errores.\n")
    for tipo, valor, linea in resultados:
        print(f"L{linea}: {tipo:<15} -> {valor}")
    if errores:
        print("\nErrores:")
        for e in errores:
            print(" -", e)

    ruta_log = generar_log(nombre_apellido, codigo, resultados, errores)
    print(f"\nLog generado en: {ruta_log}")


if __name__ == "__main__":
    main()
