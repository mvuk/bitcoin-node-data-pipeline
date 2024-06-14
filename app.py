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


# FIRST CONNECTION

payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblockcount", "params": []}
r = query_bitcoind(payload)

# r = requests.post(url, headers=headers, data=json.dumps(payload)).json()
print(r)

latest_block_number = r['result']
print(latest_block_number)

payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblockhash", "params": [latest_block_number]}
r = query_bitcoind(payload)
print(r)


payload = {"jsonrpc": "1.0", "id": "curltest", "method": "getblock", "params": [r['result']]}
r = query_bitcoind(payload)
print(r['result']['tx'])
print(f"the block {latest_block_number} has {len(r['result']['tx'])} transactions.")