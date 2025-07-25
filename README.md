# Advanced Calculator

A comprehensive calculator application with both GUI and CLI interfaces, featuring basic arithmetic, scientific functions, memory operations, and calculation history.

## Features

### Basic Operations
- Addition, subtraction, multiplication, division
- Exponentiation (using `**` or `^`)
- Parentheses for operation precedence
- Decimal number support

### Scientific Functions
- **Trigonometric functions**: `sin()`, `cos()`, `tan()` (input in degrees)
- **Square root**: `sqrt()`
- **Logarithms**: `log()` (base-10), `ln()` (natural logarithm)
- **Constants**: `pi` (π), `e` (Euler's number)

### Memory Operations
- **Memory Store** (`MS`): Store current value
- **Memory Recall** (`MR`): Recall stored value
- **Memory Clear** (`MC`): Clear memory
- **Memory Add** (`M+`): Add current value to memory

### Additional Features
- **Calculation History**: Track all calculations
- **Error Handling**: Graceful error messages for invalid operations
- **Both GUI and CLI**: Use the interface that suits your needs

## Usage

### Running the Calculator

#### GUI Mode (Default)
```bash
python3 main.py
```

If tkinter is not available, it will automatically fall back to CLI mode with installation instructions.

#### CLI Mode (Force)
```bash
python3 main.py --cli
```

### GUI Interface

The GUI provides a modern calculator interface with:
- **Display**: Shows current calculation and result
- **Number buttons**: 0-9 and decimal point
- **Operation buttons**: +, -, ×, ÷, =, ^, %
- **Scientific function buttons**: sin, cos, tan, √, log, ln, π, e
- **Memory buttons**: MC, MR, MS, M+
- **Utility buttons**: C (clear), ± (sign toggle), Del (delete), History, Clear All

### CLI Interface

#### Basic Calculations
```
calc> 2 + 3 * 4
= 14

calc> sqrt(16) + sin(30)
= 4.5

calc> (2 + 3) ** 2
= 25

calc> log(100) * pi
= 6.283185307179586
```

#### Memory Operations
```
calc> ms 50        # Store 50 in memory
Stored 50.0 in memory

calc> mr           # Recall memory
Memory: 50.0

calc> m+ 25        # Add 25 to memory
Added 25.0 to memory

calc> mc           # Clear memory
Memory cleared
```

#### Special Commands
- `help` - Show help information
- `history` - Display calculation history
- `clear` - Clear calculation history
- `quit` or `exit` - Exit calculator

## Examples

### Basic Arithmetic
```
2 + 3 * 4          # Result: 14
(5 + 3) / 2        # Result: 4.0
2^3                # Result: 8
```

### Scientific Calculations
```
sin(30)            # Result: 0.5 (30 degrees)
cos(60)            # Result: 0.5 (60 degrees)
sqrt(16)           # Result: 4.0
log(100)           # Result: 2.0 (base-10)
ln(e)              # Result: 1.0 (natural log)
pi * 2             # Result: 6.283185307179586
```

### Complex Expressions
```
sqrt(sin(30)^2 + cos(30)^2)    # Result: 1.0
log(10^3)                      # Result: 3.0
(pi/2) * sin(90)              # Result: 1.5707963267948966
```

## Installation

### Prerequisites
- Python 3.6 or higher

### GUI Support (Optional)
For GUI mode, install tkinter:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**CentOS/RHEL:**
```bash
sudo yum install tkinter
# or
sudo dnf install python3-tkinter
```

**macOS:**
```bash
# Usually included with Python installation
# If not, install via Homebrew:
brew install python-tk
```

**Windows:**
```bash
# Usually included with Python installation from python.org
```

## File Structure
```
main.py           # Main calculator application
README.md         # This documentation
```

## Error Handling

The calculator handles various error conditions gracefully:
- **Division by zero**: Shows appropriate error message
- **Invalid expressions**: Provides helpful error descriptions
- **Mathematical domain errors**: Prevents invalid operations (e.g., sqrt of negative numbers)
- **Memory operations**: Validates input before storing

## License

This project is open source and available under the MIT License.
