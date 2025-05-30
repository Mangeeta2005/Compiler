# ir_generator.py

def generate_ir(ast):
    ir_code = []

    if ast is None:
        return ir_code

    if ast[0] == 'if':
        condition = ast[1]
        true_branch = generate_ir(ast[2])
        false_branch = generate_ir(ast[3])
        ir_code.extend(generate_ir(condition))
        ir_code.append("IF")
        ir_code.extend(true_branch)
        ir_code.append("ELSE")
        ir_code.extend(false_branch)
    elif ast[0] in ('+', '-', '*', '/', '>', '<', '=='):
        left = generate_ir(ast[1])
        right = generate_ir(ast[2])
        ir_code.extend(left)
        ir_code.extend(right)
        ir_code.append(ast[0])
    elif ast[0] == 'NUMBER':
        ir_code.append(f"PUSH {ast[1]}")

    return ir_code
