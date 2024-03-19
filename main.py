import os
import time

import httpx
from web3 import Web3
mint_contract_address = "0xC6e865c213C89Ca42A622c5572D19f00d84d7a16"
claim_contract_address = "0x5C3C1a119300669990863861a854616eCb04b463"
w3 = Web3(Web3.HTTPProvider('https://evm.confluxrpc.com'))
if w3.is_connected():
    print("Connected to Conflux Network")
else:
    print("Not connected to Conflux Network")
    exit(1)
w3.eth.account.enable_unaudited_hdwallet_features()
acct = w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
minted_ids = []
claimed_ids = []
print("Address:",acct.address)
print("Balance:",w3.from_wei(w3.eth.get_balance(acct.address), 'ether'), "CFX")
tx_list = []
page_tx_list = ["1"]
page = 0
while len(page_tx_list) > 0:
    page += 1
    resp = httpx.request("GET", f"https://evmapi.confluxscan.io/api?module=account&action=txlist&address={acct.address}&page={page}&offset=100&sort=desc")
    page_tx_list = resp.json()["result"]
    tx_list += page_tx_list
    print(f"Page {page} Transactions:",len(page_tx_list))
    time.sleep(0.2)
print("Total Transactions:",len(tx_list))
mint_tx_list = [x for x in tx_list if x["to"] == mint_contract_address]
print("Mint Transactions:",len(mint_tx_list))
claim_tx_list = [x for x in tx_list if x["to"] == claim_contract_address]
print("Claim Transactions:",len(claim_tx_list))
