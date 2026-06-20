import ply.lex as lex


# ============================================================
# === INICIO APORTE: Andie Barreno
# === Palabras reservadas e identificadores
# ============================================================

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'bool': 'BOOL',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'return': 'RETURN',
    'class': 'CLASS',
    'struct': 'STRUCT',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'include': 'INCLUDE',
    'using': 'USING',
    'namespace': 'NAMESPACE',
    'std': 'STD',
    'true': 'TRUE',
    'false': 'FALSE',
    'const': 'CONST',
    'static': 'STATIC',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'new': 'NEW',
    'delete': 'DELETE',
    'cout': 'COUT',
    'cin': 'CIN',
    'endl': 'ENDL',
}


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Si la palabra reconocida esta en el diccionario de reservadas,
    # se reclasifica el token (ej: 'int' deja de ser IDENTIFIER y pasa a ser INT)
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# ============================================================
# === FIN APORTE: Andie Barreno
# ============================================================


# ============================================================
# === INICIO APORTE: Gabriel Villao
# === Operadores aritmeticos, relacionales, logicos y de asignacion
# ============================================================

# Nota: PLY ordena las reglas tipo string por longitud de regex
# descendente, por eso '==' siempre se evalua antes que '=',
# '++' antes que '+', etc. No es necesario ordenarlas a mano.

t_INCREMENT      = r'\+\+'
t_DECREMENT      = r'--'
t_PLUS_ASSIGN    = r'\+='
t_MINUS_ASSIGN   = r'-='
t_TIMES_ASSIGN   = r'\*='
t_DIVIDE_ASSIGN  = r'/='
t_EQ             = r'=='
t_NEQ            = r'!='
t_LE             = r'<='
t_GE             = r'>='
t_AND            = r'&&'
t_OR             = r'\|\|'
t_STREAM_OUT     = r'<<'
t_STREAM_IN      = r'>>'
t_SCOPE          = r'::'

t_PLUS           = r'\+'
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_MOD            = r'%'
t_ASSIGN         = r'='
t_LT             = r'<'
t_GT             = r'>'
t_NOT            = r'!'
t_AMPERSAND      = r'&'

# ============================================================
# === FIN APORTE: Gabriel Villao
# ============================================================


# ============================================================
# === INICIO APORTE: Samuel Chichande
# === Literales (numeros, strings, chars) y delimitadores
# ============================================================

def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_NUMBER_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t


def t_CHAR_LITERAL(t):
    r"\'([^\\\n]|(\\.))?\'"
    return t


t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMICOLON  = r';'
t_COMMA      = r','
t_DOT        = r'\.'
t_HASH       = r'\#'
t_COLON      = r':'

# ============================================================
# === FIN APORTE: Samuel Chichande
# ============================================================


# ============================================================
# SECCION COMUN (comentarios, saltos de linea, ignorados, errores)
# Mantenida en conjunto por los 3 integrantes
# ============================================================

# Lista final de tokens: reservadas + el resto definido arriba
tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'NUMBER_INT', 'NUMBER_FLOAT', 'STRING_LITERAL', 'CHAR_LITERAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN',
    'EQ', 'NEQ', 'LT', 'GT', 'LE', 'GE',
    'AND', 'OR', 'NOT',
    'INCREMENT', 'DECREMENT',
    'STREAM_OUT', 'STREAM_IN', 'SCOPE', 'AMPERSAND',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'DOT', 'HASH', 'COLON',
]

# Caracteres que se ignoran (no generan token ni error)
t_ignore = ' \t'


def t_COMMENT_LINE(t):
    r'//.*'
    pass  # los comentarios no generan token, simplemente se descartan


def t_COMMENT_BLOCK(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Lista global donde se acumulan los errores de la ultima ejecucion
errores_lexicos = []


def t_error(t):
    msg = f"Error lexico: caracter ilegal '{t.value[0]}' en la linea {t.lexer.lineno}"
    errores_lexicos.append(msg)
    t.lexer.skip(1)


# Construccion del lexer
lexer = lex.lex()
