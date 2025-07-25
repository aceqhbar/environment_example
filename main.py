#!/usr/bin/env python3
"""
Advanced Calculator Application
Supports both command-line and GUI interfaces
Features: Basic arithmetic, scientific functions, history, and memory operations
"""

import math
import sys
import re
from typing import List, Union

# Try to import tkinter, but handle gracefully if not available
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False

class Calculator:
    """Core calculator engine with scientific functions and memory operations."""
    
    def __init__(self):
        self.memory = 0
        self.history: List[str] = []
        self.last_result = 0
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a: float, b: float) -> float:
        return a ** b
    
    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    
    def sin(self, a: float) -> float:
        return math.sin(math.radians(a))
    
    def cos(self, a: float) -> float:
        return math.cos(math.radians(a))
    
    def tan(self, a: float) -> float:
        return math.tan(math.radians(a))
    
    def log(self, a: float) -> float:
        if a <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        return math.log10(a)
    
    def ln(self, a: float) -> float:
        if a <= 0:
            raise ValueError("Cannot calculate natural logarithm of non-positive number")
        return math.log(a)
    
    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if n > 170:  # Prevent overflow
            raise ValueError("Number too large for factorial calculation")
        return math.factorial(n)
    
    def evaluate_expression(self, expression: str) -> float:
        """Safely evaluate mathematical expressions."""
        # Remove spaces and convert to lowercase
        expr = expression.replace(' ', '').lower()
        
        # Replace mathematical functions with proper parentheses handling
        import re
        
        # Handle trigonometric functions (convert degrees to radians)
        expr = re.sub(r'sin\(([^)]+)\)', r'math.sin(math.radians(\1))', expr)
        expr = re.sub(r'cos\(([^)]+)\)', r'math.cos(math.radians(\1))', expr)
        expr = re.sub(r'tan\(([^)]+)\)', r'math.tan(math.radians(\1))', expr)
        
        # Handle other functions
        expr = re.sub(r'sqrt\(([^)]+)\)', r'math.sqrt(\1)', expr)
        expr = re.sub(r'log\(([^)]+)\)', r'math.log10(\1)', expr)
        expr = re.sub(r'ln\(([^)]+)\)', r'math.log(\1)', expr)
        
        # Replace constants
        expr = expr.replace('pi', 'math.pi')
        expr = expr.replace('e', 'math.e')
        expr = expr.replace('^', '**')
        
        # Safety check: only allow safe characters for math operations
        allowed_chars = set('0123456789+-*/.()mathsincostanqrtlogpiedruh_ ')
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Invalid characters in expression")
        
        try:
            result = eval(expr)
            self.last_result = result
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def memory_store(self, value: float):
        """Store value in memory."""
        self.memory = value
    
    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory
    
    def memory_clear(self):
        """Clear memory."""
        self.memory = 0
    
    def memory_add(self, value: float):
        """Add value to memory."""
        self.memory += value
    
    def get_history(self) -> List[str]:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()

class CalculatorGUI:
    """Modern GUI calculator interface using tkinter."""
    
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.root.title("Advanced Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Configure style
        self.setup_styles()
        
        # Current display value
        self.display_var = tk.StringVar(value="0")
        self.current_expression = ""
        
        self.create_widgets()
    
    def setup_styles(self):
        """Configure modern styling."""
        self.root.configure(bg='#2c3e50')
        
        # Configure button styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Number buttons
        style.configure('Number.TButton',
                       font=('Arial', 12, 'bold'),
                       foreground='white',
                       background='#34495e',
                       borderwidth=1)
        
        # Operator buttons
        style.configure('Operator.TButton',
                       font=('Arial', 12, 'bold'),
                       foreground='white',
                       background='#e74c3c',
                       borderwidth=1)
        
        # Function buttons
        style.configure('Function.TButton',
                       font=('Arial', 10),
                       foreground='white',
                       background='#3498db',
                       borderwidth=1)
    
    def create_widgets(self):
        """Create and arrange GUI widgets."""
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Display frame
        display_frame = tk.Frame(main_frame, bg='#2c3e50')
        display_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Expression display
        expr_label = tk.Label(display_frame, textvariable=tk.StringVar(),
                             font=('Arial', 10), bg='#2c3e50', fg='#bdc3c7',
                             anchor='e')
        expr_label.pack(fill=tk.X)
        
        # Main display
        display = tk.Entry(display_frame, textvariable=self.display_var,
                          font=('Arial', 20, 'bold'), justify='right',
                          state='readonly', bg='#34495e', fg='white',
                          borderwidth=2, relief='sunken')
        display.pack(fill=tk.X, ipady=10)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scientific functions row
        sci_frame = tk.Frame(button_frame, bg='#2c3e50')
        sci_frame.pack(fill=tk.X, pady=(0, 5))
        
        sci_buttons = [
            ('sin', lambda: self.add_function('sin(')),
            ('cos', lambda: self.add_function('cos(')),
            ('tan', lambda: self.add_function('tan(')),
            ('√', lambda: self.add_function('sqrt(')),
            ('log', lambda: self.add_function('log(')),
            ('ln', lambda: self.add_function('ln(')),
            ('π', lambda: self.add_text('pi')),
            ('e', lambda: self.add_text('e'))
        ]
        
        for i, (text, command) in enumerate(sci_buttons):
            btn = ttk.Button(sci_frame, text=text, command=command,
                           style='Function.TButton', width=6)
            btn.grid(row=0, column=i, padx=2, pady=2, sticky='ew')
        
        # Configure grid weights for scientific buttons
        for i in range(len(sci_buttons)):
            sci_frame.grid_columnconfigure(i, weight=1)
        
        # Memory and utility buttons
        mem_frame = tk.Frame(button_frame, bg='#2c3e50')
        mem_frame.pack(fill=tk.X, pady=(0, 5))
        
        mem_buttons = [
            ('MC', self.memory_clear),
            ('MR', self.memory_recall),
            ('MS', self.memory_store),
            ('M+', self.memory_add),
            ('History', self.show_history),
            ('Clear', self.clear_all)
        ]
        
        for i, (text, command) in enumerate(mem_buttons):
            btn = ttk.Button(mem_frame, text=text, command=command,
                           style='Function.TButton', width=8)
            btn.grid(row=0, column=i, padx=2, pady=2, sticky='ew')
        
        for i in range(len(mem_buttons)):
            mem_frame.grid_columnconfigure(i, weight=1)
        
        # Main calculator buttons
        calc_frame = tk.Frame(button_frame, bg='#2c3e50')
        calc_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            [('C', self.clear), ('±', self.toggle_sign), ('%', lambda: self.add_operator('%')), ('÷', lambda: self.add_operator('/'))],
            [('7', lambda: self.add_number('7')), ('8', lambda: self.add_number('8')), ('9', lambda: self.add_number('9')), ('×', lambda: self.add_operator('*'))],
            [('4', lambda: self.add_number('4')), ('5', lambda: self.add_number('5')), ('6', lambda: self.add_number('6')), ('-', lambda: self.add_operator('-'))],
            [('1', lambda: self.add_number('1')), ('2', lambda: self.add_number('2')), ('3', lambda: self.add_number('3')), ('+', lambda: self.add_operator('+'))],
            [('0', lambda: self.add_number('0')), ('.', lambda: self.add_number('.')), ('(', lambda: self.add_text('(')), (')', lambda: self.add_text(')'))],
            [('x²', self.square), ('^', lambda: self.add_operator('**')), ('=', self.calculate), ('Del', self.delete)]
        ]
        
        for row, button_row in enumerate(buttons):
            for col, (text, command) in enumerate(button_row):
                if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')']:
                    style = 'Number.TButton'
                elif text in ['+', '-', '×', '÷', '=', '^', '%']:
                    style = 'Operator.TButton'
                else:
                    style = 'Function.TButton'
                
                btn = ttk.Button(calc_frame, text=text, command=command,
                               style=style)
                btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(4):
            calc_frame.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons)):
            calc_frame.grid_rowconfigure(i, weight=1)
    
    def add_number(self, number):
        if self.display_var.get() == "0" or self.display_var.get() == "Error":
            self.display_var.set(number)
            self.current_expression = number
        else:
            self.display_var.set(self.display_var.get() + number)
            self.current_expression += number
    
    def add_operator(self, operator):
        current = self.display_var.get()
        if current != "Error":
            self.current_expression += operator
            self.display_var.set(self.current_expression)
    
    def add_function(self, func):
        self.current_expression += func
        self.display_var.set(self.current_expression)
    
    def add_text(self, text):
        self.current_expression += text
        self.display_var.set(self.current_expression)
    
    def calculate(self):
        try:
            result = self.calc.evaluate_expression(self.current_expression)
            self.display_var.set(str(result))
            self.current_expression = str(result)
        except Exception as e:
            self.display_var.set("Error")
            messagebox.showerror("Error", str(e))
    
    def clear(self):
        self.display_var.set("0")
        self.current_expression = ""
    
    def clear_all(self):
        self.clear()
        self.calc.clear_history()
        self.calc.memory_clear()
    
    def delete(self):
        current = self.current_expression
        if current:
            self.current_expression = current[:-1]
            self.display_var.set(self.current_expression if self.current_expression else "0")
    
    def toggle_sign(self):
        current = self.display_var.get()
        try:
            value = float(current)
            result = -value
            self.display_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
    
    def square(self):
        try:
            current = float(self.display_var.get())
            result = current ** 2
            self.display_var.set(str(result))
            self.current_expression = str(result)
            self.calc.history.append(f"{current}² = {result}")
        except:
            self.display_var.set("Error")
    
    def memory_store(self):
        try:
            value = float(self.display_var.get())
            self.calc.memory_store(value)
            messagebox.showinfo("Memory", f"Stored: {value}")
        except:
            messagebox.showerror("Error", "Invalid number")
    
    def memory_recall(self):
        memory_value = self.calc.memory_recall()
        self.display_var.set(str(memory_value))
        self.current_expression = str(memory_value)
    
    def memory_clear(self):
        self.calc.memory_clear()
        messagebox.showinfo("Memory", "Memory cleared")
    
    def memory_add(self):
        try:
            value = float(self.display_var.get())
            self.calc.memory_add(value)
            messagebox.showinfo("Memory", f"Added {value} to memory")
        except:
            messagebox.showerror("Error", "Invalid number")
    
    def show_history(self):
        history = self.calc.get_history()
        if not history:
            messagebox.showinfo("History", "No calculations yet")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x300")
        history_window.configure(bg='#2c3e50')
        
        text_widget = tk.Text(history_window, bg='#34495e', fg='white',
                             font=('Arial', 10), wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for calculation in history:
            text_widget.insert(tk.END, calculation + '\n')
        
        text_widget.configure(state='disabled')
    
    def run(self):
        """Start the GUI calculator."""
        self.root.mainloop()

class CalculatorCLI:
    """Command-line interface for the calculator."""
    
    def __init__(self):
        self.calc = Calculator()
    
    def print_help(self):
        """Print help information."""
        help_text = """
Advanced Calculator - Command Line Interface

Basic Operations:
  +, -, *, /        : Basic arithmetic
  **  or  ^         : Power (exponentiation)
  sqrt(x)           : Square root
  
Scientific Functions:
  sin(x), cos(x), tan(x)  : Trigonometric functions (degrees)
  log(x)                  : Base-10 logarithm
  ln(x)                   : Natural logarithm
  pi                      : π constant
  e                       : Euler's number
  
Memory Operations:
  ms <value>        : Memory store
  mr                : Memory recall
  mc                : Memory clear
  m+ <value>        : Memory add
  
Utility Commands:
  history           : Show calculation history
  clear             : Clear history
  help              : Show this help
  quit or exit      : Exit calculator
  
Examples:
  2 + 3 * 4
  sqrt(16) + sin(30)
  log(100) * pi
  (2 + 3) ** 2
        """
        print(help_text)
    
    def run(self):
        """Run the command-line calculator."""
        print("Advanced Calculator CLI")
        print("Type 'help' for instructions, 'quit' to exit")
        print("-" * 40)
        
        while True:
            try:
                user_input = input("calc> ").strip()
                
                if not user_input:
                    continue
                
                # Handle special commands
                if user_input.lower() in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'help':
                    self.print_help()
                    continue
                elif user_input.lower() == 'history':
                    history = self.calc.get_history()
                    if history:
                        print("\nCalculation History:")
                        for calc in history[-10:]:  # Show last 10
                            print(f"  {calc}")
                    else:
                        print("No calculations yet")
                    continue
                elif user_input.lower() == 'clear':
                    self.calc.clear_history()
                    print("History cleared")
                    continue
                elif user_input.lower() == 'mc':
                    self.calc.memory_clear()
                    print("Memory cleared")
                    continue
                elif user_input.lower() == 'mr':
                    print(f"Memory: {self.calc.memory_recall()}")
                    continue
                elif user_input.lower().startswith('ms '):
                    try:
                        value = float(user_input[3:])
                        self.calc.memory_store(value)
                        print(f"Stored {value} in memory")
                    except ValueError:
                        print("Error: Invalid number for memory store")
                    continue
                elif user_input.lower().startswith('m+ '):
                    try:
                        value = float(user_input[3:])
                        self.calc.memory_add(value)
                        print(f"Added {value} to memory")
                    except ValueError:
                        print("Error: Invalid number for memory add")
                    continue
                
                # Evaluate mathematical expression
                result = self.calc.evaluate_expression(user_input)
                print(f"= {result}")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main entry point for the calculator application."""
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Run command-line interface
        cli = CalculatorCLI()
        cli.run()
    else:
        # Run GUI interface if available, otherwise CLI
        if TKINTER_AVAILABLE:
            gui = CalculatorGUI()
            gui.run()
        else:
            print("GUI not available (tkinter not installed). Running CLI version...")
            print("To use GUI mode, install tkinter: sudo apt-get install python3-tk")
            print()
            cli = CalculatorCLI()
            cli.run()

if __name__ == '__main__':
    main()
