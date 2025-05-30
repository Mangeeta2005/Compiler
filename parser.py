def parse(tokens):
    def get_precedence(op):
        return {'+': 1, '-': 1, '*': 2, '/': 2, '>': 0, '<': 0, '==': 0}.get(op, -1)

    def parse_primary(index):
        if index >= len(tokens):
            return None, index
        token = tokens[index]
        if token[0] == 'NUMBER':
            return token, index + 1
        return None, index

    def parse_expression(index=0, min_prec=0):
        lhs, index = parse_primary(index)

        while index < len(tokens):
            token = tokens[index]
            if token[0] != 'OPERATOR':
                break
            op = token[1]
            prec = get_precedence(op)
            if prec < min_prec:
                break
            index += 1
            rhs, index = parse_expression(index, prec + 1)
            lhs = (op, lhs, rhs)

        return lhs, index

    if tokens and tokens[0][0] == 'IF':
        # if <cond1> <op> <cond2> : <true_expr> else <false_expr>
        _, index = tokens[0], 1
        cond_lhs = tokens[index]
        cond_op = tokens[index + 1]
        cond_rhs = tokens[index + 2]
        if tokens[index + 3][0] != 'COLON':
            return None
        true_expr, next_index = parse_expression(index + 4)
        if tokens[next_index][0] != 'ELSE':
            return None
        false_expr, _ = parse_expression(next_index + 1)
        return ('if', (cond_op[1], cond_lhs, cond_rhs), true_expr, false_expr)

    ast, _ = parse_expression()
    return ast
