import re



name = input("what your name? ").strip()

if matches := re.search("^(.+), *(.+)$", name ):
    name =  matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")

#