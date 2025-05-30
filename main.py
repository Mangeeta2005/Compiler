import tokenizer
import parser
import ir_generator
import ir_executor

def main():
    while True:
        code = input("💻 Enter your code (or type 'exit' to quit): ")
        if code.strip().lower() == 'exit':
            break
        tokens = tokenizer.tokenize(code)
        print("Tokens:", tokens)
        ast = parser.parse(tokens)
        print("AST:", ast)
        ir_code = ir_generator.generate_ir(ast)
        print("IR Code:", ir_code)
        result = ir_executor.execute_ir(ir_code)
        print("✅ Output:", result)

if __name__ == '__main__':
    main()
