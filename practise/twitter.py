#standarding the data possible valid inputs take baby steps in regular experessions each of those steps correct inclination

# try to find more incrementally final improvements py


import re

url = input("URL: ").strip()

if matches := re.search("^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE):
    print(f"username:" , matches.group(1))

