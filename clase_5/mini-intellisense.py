import keyword
import re

BUILTINS = {
    "print", "len", "range", "list", "dict", "str", "int",
    "float", "bool", "sum", "min", "max", "sorted"
}

def get_prefix(source):
    match = re.search(r"[A-Za-z_][A-Za-z0-9_]*$", source)
    return match.group(0) if match else ""

def get_words(source):
    words = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", source))
    return words - set(keyword.kwlist)

def complete(source):
    prefix = get_prefix(source)

    if not prefix:
        return []

    candidates = set(keyword.kwlist) | BUILTINS | get_words(source)

    suggestions = [
        word
        for word in candidates
        if word.startswith(prefix) and word != prefix
    ]

    return sorted(suggestions, key=len)[:5]

source = ""

print("Mini IntelliSense")
print("Escribí código línea por línea.")
print("Comandos: :q para salir, :show para ver el código acumulado")
print()

while True:
    line = input(">>> ")

    if line == ":q":
        break

    if line == ":show":
        print(source)
        continue

    source += line + "\n"

    suggestions = complete(source.rstrip())

    if suggestions:
        print("Sugerencias:", ", ".join(suggestions))
    else:
        print("Sin sugerencias")