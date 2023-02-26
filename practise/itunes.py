# application programming interface

'''
json java script object notation

language agnostic access data from somewhere
sys.exit() to exit the program
to read json you can use python
'''

import json
import requests
import sys


if len(sys.argv) !=2:
    sys.exit()


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

print("check",response)

#print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    print((result["trackName"]))