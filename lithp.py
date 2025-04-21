#!/usr/bin/env python3
import sys

class Environment:
    def __init__(self):
        self.variables = {}
    
    def set_variable(self, name, value):
        self.variables[name] = value
    
    def get_variable(self, name):
        if name not in self.variables:
            raise NameError(f"Variable '{name}' not defined")
        return self.variables[name]
    
    def has_variable(self, name):
        return name in self.variables
    
    def get_indexed_value(self, name, index):
        value = self.get_variable(name)
        if isinstance(value, str):
            try:
                return value[int(index)]
            except IndexError:
                raise IndexError(f"Index {index} out of range for string '{value}'")
            except ValueError:
                raise ValueError(f"Invalid index '{index}' for string indexing")
        else:
            raise TypeError(f"Cannot index non-string value '{value}'")

def lex(source):
    tokens = []
    current_token = ""
    in_quotes = False
    quote_char = None
    paren_level = 0
    paren_content = ""
    block_level = 0
    block_content = ""
    
    for char in source:
        if char in ['"', "'"]:
            if not in_quotes:
                # Start of quoted string
                in_quotes = True
                quote_char = char
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            elif char == quote_char:
                # End of quoted string
                in_quotes = False
                tokens.append(current_token)
                current_token = ""
            else:
                # Quote character inside string
                current_token += char
        elif char == '{' and not in_quotes:
            if block_level == 0:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            block_level += 1
            if block_level > 1:
                block_content += char
        elif char == '}' and not in_quotes:
            block_level -= 1
            if block_level == 0:
                tokens.append(f"{{{block_content}}}")
                block_content = ""
            elif block_level > 0:
                block_content += char
        elif block_level > 0:
            block_content += char
        elif char == '(' and not in_quotes:
            if paren_level == 0:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            paren_level += 1
            if paren_level > 1:
                paren_content += char
        elif char == ')' and not in_quotes:
            paren_level -= 1
            if paren_level == 0:
                tokens.append(f"({paren_content})")
                paren_content = ""
            elif paren_level > 0:
                paren_content += char
        elif paren_level > 0:
            paren_content += char
        elif char.isspace() and not in_quotes:
            if current_token:
                tokens.append(current_token)
                current_token = ""
        else:
            current_token += char
    
    # Add the last token if there is one
    if current_token:
        tokens.append(current_token)
    
    return tokens

def handle_thet(env, tokens, i):
    if i + 2 >= len(tokens):
        print("Error: Incomplete thet statement")
        return i, None
    name = tokens[i + 1]
    value = tokens[i + 2]
    
    # If the value is a parenthesized expression, evaluate it
    if value.startswith('(') and value.endswith(')'):
        expr_tokens = lex(value[1:-1])
        _, value = process_expression(env, expr_tokens, 0)
    
    env.set_variable(name, value)
    return i + 3, value

def handle_dithplay(env, tokens, i):
    if i + 1 >= len(tokens):
        print("Error: Incomplete dithplay statement")
        return i, None
    
    value = tokens[i + 1]
    
    # If the value is a parenthesized expression, evaluate it
    if value.startswith('(') and value.endswith(')'):
        expr_tokens = lex(value[1:-1])
        _, result = process_expression(env, expr_tokens, 0)
        print(result)
        return i + 2, result
    else:
        # Otherwise treat it as a variable name
        value = env.get_variable(value)
        print(value)
        return i + 2, value

def handle_pluth(env, tokens, i):
    if i + 2 >= len(tokens):
        print("Error: Incomplete pluth statement")
        return i, None
    
    # Get first operand
    a = tokens[i + 1]
    if a.startswith('(') and a.endswith(')'):
        expr_tokens = lex(a[1:-1])
        _, a = process_expression(env, expr_tokens, 0)
    else:
        a = env.get_variable(a)
    
    # Get second operand
    b = tokens[i + 2]
    if b.startswith('(') and b.endswith(')'):
        expr_tokens = lex(b[1:-1])
        _, b = process_expression(env, expr_tokens, 0)
    else:
        b = env.get_variable(b)
    
    result = a + b
    return i + 3, result

def handle_timethh(env, tokens, i):
    if i + 2 >= len(tokens):
        print("Error: Incomplete timeth statement")
        return i, None
    
    # Get first operand
    a = tokens[i + 1]
    if a.startswith('(') and a.endswith(')'):
        expr_tokens = lex(a[1:-1])
        _, a = process_expression(env, expr_tokens, 0)
    else:
        a = env.get_variable(a)
    
    # Get second operand
    b = tokens[i + 2]
    if b.startswith('(') and b.endswith(')'):
        expr_tokens = lex(b[1:-1])
        _, b = process_expression(env, expr_tokens, 0)
    else:
        b = env.get_variable(b)
    
    result = a * b
    return i + 3, result

def handle_athk(env, tokens, i):
    if i + 2 >= len(tokens):
        print("Error: Incomplete athk statement")
        return i, None
    
    prompt = tokens[i + 1]
    var_name = tokens[i + 2]
    
    # If prompt is a variable, get its value
    if not (prompt.startswith('"') or prompt.startswith("'")):
        prompt = env.get_variable(prompt)
    
    # Remove quotes if present
    if prompt.startswith('"') or prompt.startswith("'"):
        prompt = prompt[1:-1]
    
    # Get user input
    value = input(prompt + " ")
    
    # Try to convert to number if possible
    try:
        value = float(value)
    except ValueError:
        pass
    
    # Set the variable (this will create it if it doesn't exist)
    env.set_variable(var_name, value)
    return i + 3, value

def handle_repeathh(env, tokens, i):
    if i + 3 >= len(tokens):
        print("Error: Incomplete for statement")
        return i, None
    
    var_name = tokens[i + 1]
    count = tokens[i + 2]
    block = tokens[i + 3]
    
    # Get the count value
    if count.startswith('(') and count.endswith(')'):
        expr_tokens = lex(count[1:-1])
        _, count = process_expression(env, expr_tokens, 0)
    else:
        count = env.get_variable(count)
    
    # Get the block content
    if not block.startswith('{') or not block.endswith('}'):
        print("Error: For loop requires a block of code")
        return i, None
    
    block_content = block[1:-1]
    
    # Execute the block count times
    for iteration in range(int(count)):
        # Set the iteration variable
        env.set_variable(var_name, iteration)
        
        # Execute the block
        block_tokens = lex(block_content)
        process_tokens(env, block_tokens)
    
    return i + 4, count

def handle_indexth(env, tokens, i):
    if i + 2 >= len(tokens):
        print("Error: Incomplete indexth statement")
        return i, None
    
    # Get the string
    string = tokens[i + 1]
    if string.startswith('(') and string.endswith(')'):
        expr_tokens = lex(string[1:-1])
        _, string = process_expression(env, expr_tokens, 0)
    else:
        string = env.get_variable(string)
    
    # Get the index
    index = tokens[i + 2]
    if index.startswith('(') and index.endswith(')'):
        expr_tokens = lex(index[1:-1])
        _, index = process_expression(env, expr_tokens, 0)
    else:
        index = env.get_variable(index)
    
    # Convert to string if it's a number
    string = str(string)
    
    # Get the character at the index
    try:
        result = string[int(index)]
    except IndexError:
        print(f"Error: Index {index} out of range for string '{string}'")
        return i, None
    except ValueError:
        print(f"Error: Invalid index '{index}' for string indexing")
        return i, None
    
    return i + 3, result

def handle_iterateth(env, tokens, i):
    if i + 3 >= len(tokens):
        print("Error: Incomplete iterateth statement")
        return i, None
    
    char_var = tokens[i + 1]
    string = tokens[i + 2]
    block = tokens[i + 3]
    
    # Get the string value
    if string.startswith('(') and string.endswith(')'):
        expr_tokens = lex(string[1:-1])
        _, string = process_expression(env, expr_tokens, 0)
    else:
        string = env.get_variable(string)
    
    # Convert to string if it's a number
    string = str(string)
    
    # Get the block content
    if not block.startswith('{') or not block.endswith('}'):
        print("Error: Iterateth loop requires a block of code")
        return i, None
    
    block_content = block[1:-1]
    
    # Execute the block for each character
    for char in string:
        # Set the character variable
        env.set_variable(char_var, char)
        
        # Execute the block
        block_tokens = lex(block_content)
        process_tokens(env, block_tokens)
    
    return i + 4, len(string)

def process_expression(env, tokens, i):
    if i >= len(tokens):
        return i, None
    
    token = tokens[i]
    if token in KEYWORD_HANDLERS:
        return KEYWORD_HANDLERS[token](env, tokens, i)
    else:
        return i + 1, env.get_variable(token)

# Dictionary mapping keywords to their handler functions
KEYWORD_HANDLERS = {
    "thet": handle_thet,
    "dithplay": handle_dithplay,
    "pluth": handle_pluth,
    "timethh": handle_timethh,
    "athk": handle_athk,
    "repeathh": handle_repeathh,
    "indexth": handle_indexth,
    "iterateth": handle_iterateth
}

def process_tokens(env, tokens):
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in KEYWORD_HANDLERS:
            i, _ = KEYWORD_HANDLERS[token](env, tokens, i)
        else:
            i += 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python lithp.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            source_code = file.read()
            env = Environment()
            tokens = lex(source_code)
            process_tokens(env, tokens)
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()