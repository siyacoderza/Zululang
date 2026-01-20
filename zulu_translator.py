# Zululang Translator v0.1
# Copyright (c) 2026 Siyabonga Ngcobo
# Licensed under MIT License

import re

def run_zululang(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.readlines()

    python_code = []
    for line in code:
        line = line.rstrip()
        # Variable assignment
        line = re.sub(r'(\w+)\s+kuba\s+(.+)', r'\1 = \2', line)
        # Print
        line = re.sub(r'bonisa\s+(.+)', r'print(\1)', line)
        # If statement
        line = re.sub(r'uma\s+(.+)\s+khona', r'if \1:', line)
        # Else
        if line.strip() == "kungenjalo":
            line = "else:"
        # While loop
        line = re.sub(r'ngenkathi\s+(.+)', r'while \1:', line)
        # Function
        line = re.sub(r'umsebenzi\s+(\w+)\((.*)\)', r'def \1(\2):', line)
        # Return
        line = re.sub(r'buyisa\s+(.+)', r'return \1', line)

        python_code.append(line)

    # Join translated code
    python_code_str = "\n".join(python_code)
    exec(python_code_str)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Sebenzisa: python zululang_translator.py <file.zulu>")
    else:
        run_zululang(sys.argv[1])

      
