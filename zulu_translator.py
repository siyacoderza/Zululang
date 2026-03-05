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
        
# Zululang translator V0.2.0 
# Added JavaScript syntax highlighting
# Copyright (c) 2026 Siyabonga Ngcobo
# Licensed under MIT License


function runZululang(code) {

const lines = code.split("\n");

lines.forEach((line, index) => {

const words = line.trim().split(" ");
const command = words[0];

switch(command) {

case "khuluma":
if(words.length < 2){
console.log(`Line ${index+1}: Error -> khuluma needs a message`);
} else {
console.log(words.slice(1).join(" "));
}
break;

case "engeza":
if(words.length !== 3){
console.log(`Line ${index+1}: Error -> engeza needs two numbers`);
} else {
let result = Number(words[1]) + Number(words[2]);
console.log(result);
}
break;

case "susa":
if(words.length !== 3){
console.log(`Line ${index+1}: Error -> susa needs two numbers`);
} else {
let result = Number(words[1]) - Number(words[2]);
console.log(result);
}
break;

case "phinda":
if(words.length !== 3){
console.log(`Line ${index+1}: Error -> phinda needs two numbers`);
} else {
let result = Number(words[1]) * Number(words[2]);
console.log(result);
}
break;

case "hlukanisa":
if(words.length !== 3){
console.log(`Line ${index+1}: Error -> hlukanisa needs two numbers`);
} else if(Number(words[2]) === 0){
console.log(`Line ${index+1}: Error -> cannot divide by zero`);
} else {
let result = Number(words[1]) / Number(words[2]);
console.log(result);
}
break;

default:
console.log(`Line ${index+1}: Unknown Zululang command -> ${command}`);
}

});
}
