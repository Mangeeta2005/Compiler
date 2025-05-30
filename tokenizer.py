import re

def tokenize(code):
    token_specification = [
        ('IF',       r'if'),
        ('ELSE',     r'else'),
        ('NUMBER',   r'\d+'),
        ('OPERATOR', r'[+\-*/><=]'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('COLON',    r':'),
        ('SKIP',     r'[ \t]+'),
        ('NEWLINE',  r'\n'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind not in ['SKIP', 'NEWLINE']:
            tokens.append((kind, value))
    return tokens
