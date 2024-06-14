# IMPORTS

import json
import simplejson
import requests

#constants

url = "http://user3:password3@127.0.0.1:8332"
headers = {'Content-type': 'application/json'}

#functions 

def query_bitcoind(payload):
    r = requests.post(url, headers=headers, data=json.dumps(payload)).json()
    return r

def generate_payload(method, params):
    payload = {"jsonrpc": "1.0", "id": "curltest", "method": method, "params": params}
    return payload


# FIRST CONNECTION

payload = generate_payload("getblockcount", [])
r = query_bitcoind(payload)
print(r)

latest_block_number = r['result']
print(latest_block_number)

payload = generate_payload("getblockhash", [latest_block_number])
r = query_bitcoind(payload)
print(r)


payload = generate_payload("getblock", [r['result'], 2])
r = query_bitcoind(payload)
print(r)

print(f"the block {latest_block_number} has {len(r['result']['tx'])} transactions.")


#get raw transaction
