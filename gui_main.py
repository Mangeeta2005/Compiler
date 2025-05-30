import tkinter as tk
from tkinter import scrolledtext, messagebox
import tokenizer
import parser as parser_module
import ir_generator
import ir_executor

# Function to run the interpreter
def run_interpreter():
    code_input = input_text.get("1.0", tk.END).strip()
    output_box.delete("1.0", tk.END)

    if not code_input:
        messagebox.showwarning("Input Missing", "Please enter some code to run.")
        return

    try:
        # Tokenization
        tokens = tokenizer.tokenize(code_input)
        output_box.insert(tk.END, "🔹 Tokens:\n", "header")
        output_box.insert(tk.END, f"{tokens}\n\n", "code")

        # Parsing
        ast = parser_module.parse(tokens)
        output_box.insert(tk.END, "🔸 Abstract Syntax Tree (AST):\n", "header")
        output_box.insert(tk.END, f"{ast}\n\n", "code")

        # IR Generation
        ir_code = ir_generator.generate_ir(ast)
        output_box.insert(tk.END, "⚙️ Intermediate Representation (IR):\n", "header")
        output_box.insert(tk.END, f"{ir_code}\n\n", "code")

        # IR Execution
        result = ir_executor.execute_ir(ir_code)
        output_box.insert(tk.END, "✅ Output:\n", "header")
        output_box.insert(tk.END, f"{result}\n", "result")

    except Exception as e:
        output_box.insert(tk.END, "❌ Error:\n", "header")
        output_box.insert(tk.END, f"{str(e)}\n", "error")

# GUI Setup
root = tk.Tk()
root.title("💻 Mini Interpreter - Compiler Design Project")
root.geometry("800x650")
root.config(bg="#f7f7f7")

# Fonts & Styles
header_font = ("Arial", 14, "bold")
code_font = ("Consolas", 11)

# Title
tk.Label(root, text="Mini Interpreter GUI", font=("Helvetica", 18, "bold"), fg="#3e3e3e", bg="#f7f7f7").pack(pady=10)

# Input Label
tk.Label(root, text="Enter your code below:", font=header_font, bg="#f7f7f7").pack()
input_text = tk.Text(root, height=5, width=90, font=code_font, wrap=tk.WORD, bg="#eef5ff")
input_text.pack(padx=10, pady=5)

# Run Button
tk.Button(root, text="▶️ Run Code", command=run_interpreter, font=("Arial", 12, "bold"),
          bg="#4caf50", fg="white", activebackground="#45a049", padx=15, pady=5).pack(pady=10)

# Output Label
tk.Label(root, text="Output:", font=header_font, bg="#f7f7f7").pack()

# Scrollable Output Area
output_box = scrolledtext.ScrolledText(root, height=20, width=95, font=code_font, wrap=tk.WORD, bg="#ffffff")
output_box.tag_config("header", foreground="#003366", font=("Arial", 12, "bold"))
output_box.tag_config("code", foreground="#222222")
output_box.tag_config("result", foreground="#008000", font=("Consolas", 12, "bold"))
output_box.tag_config("error", foreground="red")
output_box.pack(padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
