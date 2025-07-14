import re
import random
import string

def random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscate_code(code):
    # پیدا کردن نام متغیرها و فانکشن‌ها با یک regex ساده (اسم‌هایی که با حرف یا _ شروع میشن)
    names = set(re.findall(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b', code))
    
    # اسم‌هایی که نمی‌خوای تغییر کنن (کلمات کلیدی پایتون و توابع اصلی)
    keywords = set([
        'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
        'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
        'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
        'print', 'input', 'int', 'str', 'float', 'list', 'dict', 'set', 'tuple',
        'open', 'range', 'len', 'type', 'id', 'help', 'dir', 'abs', 'sum',
    ])
    
    # فقط اسامی که خودمون نباید تغییر بدیم حذف میشن
    to_replace = [name for name in names if name not in keywords]
    
    # ساختن دیکشنری برای جایگزینی اسامی
    replacements = {name: random_name() for name in to_replace}
    
    # جایگزینی اسامی توی کد
    def replace_names(match):
        word = match.group(0)
        return replacements.get(word, word)
    
    pattern = re.compile(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b')
    obfuscated_code = pattern.sub(replace_names, code)
    
    return obfuscated_code

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python obfuscate_simple.py input.py output.py")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()

    obfuscated = obfuscate_code(code)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(obfuscated)

    print(f"Obfuscated code saved to {output_file}")
