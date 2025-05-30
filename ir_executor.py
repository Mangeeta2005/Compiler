# ir_executor.py

def execute_ir(ir_code):
    stack = []
    i = 0

    while i < len(ir_code):
        instr = ir_code[i]

        if instr.startswith("PUSH"):
            _, num = instr.split()
            stack.append(int(num))

        elif instr in ('+', '-', '*', '/', '>', '<', '=='):
            b = stack.pop()
            a = stack.pop()
            if instr == '+':
                stack.append(a + b)
            elif instr == '-':
                stack.append(a - b)
            elif instr == '*':
                stack.append(a * b)
            elif instr == '/':
                stack.append(a // b)
            elif instr == '>':
                stack.append(int(a > b))
            elif instr == '<':
                stack.append(int(a < b))
            elif instr == '==':
                stack.append(int(a == b))

        elif instr == "IF":
            condition = stack.pop()
            i += 1
            true_branch = []
            while i < len(ir_code) and ir_code[i] != "ELSE":
                true_branch.append(ir_code[i])
                i += 1

            i += 1  # Skip 'ELSE'
            false_branch = []
            while i < len(ir_code):
                false_branch.append(ir_code[i])
                i += 1

            selected_branch = true_branch if condition else false_branch

            # Recursively execute the selected branch
            result = execute_ir(selected_branch)
            stack.append(result)

            break  # stop execution after if-else block

        i += 1

    return stack[-1] if stack else None
