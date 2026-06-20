# Analizador Léxico C++ — PLY (1er Avance)

**Proyecto:** Implementación de un Analizador Léxico, Sintáctico y Semántico en C++
**Integrantes:** Andie Barreno · Gabriel Villao · Samuel Chichande
**Herramienta:** PLY (Python Lex-Yacc) — módulo `lex`

## Archivos

| Archivo | Contenido |
|---|---|
| `lexer.py` | Analizador léxico (reglas PLY), dividido en 3 secciones según el aporte de cada integrante |
| `main.py` | Script que ejecuta el lexer sobre un `.cpp` y genera el log de tokens/errores |
| `algoritmo1.cpp`, `algoritmo2.cpp`, `algoritmo3.cpp` | Algoritmos de prueba en C++, uno por integrante |

## Reparto de aportes

- **Andie Barreno**: palabras reservadas e identificadores
- **Gabriel Villao**: operadores aritméticos, relacionales, lógicos y de asignación
- **Samuel Chichande**: literales (números, strings, chars) y delimitadores

## Requisito

```bash
pip install ply
```

## Cobertura del lexer

Tipos básicos (`int`, `float`, `double`, `char`, `bool`, `void`), control de flujo (`if/else`, `while`, `for`, `do`, `switch/case`), POO básica (`class`, `struct`, `public/private/protected`), entrada/salida (`cout`, `cin`, `<<`, `>>`), comentarios de línea y bloque, y los operadores/delimitadores más comunes de C++.
