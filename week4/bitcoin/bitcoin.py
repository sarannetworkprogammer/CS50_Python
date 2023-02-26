
import json
import sys
import requests

if len(sys.argv) !=2:
    sys.exit("Missing command line argument")
else:
    if float(sys.argv[1]) > 0:
        n = float(sys.argv[1])
        #print(n)
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(json.dumps(response.json(), indent=2))

        o = response.json()

        #print(o["bpi"]["USD"]["rate"])

        a = (o["bpi"]["USD"]["rate_float"])
        #b = a.split(",")
        single_cost = a

        cost1 = n * float(single_cost)
        format_float = "{:.4f}".format(cost1)
        #print(float(format_float))
        print(f"${float(format_float):,}")
















