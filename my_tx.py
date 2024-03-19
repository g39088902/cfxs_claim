from mint_contract import *
from claim_contract import *
import time
import httpx
from rpc import acct

tx_list = []
page_tx_list = ["1"]
# TODO: set page to 0
page = 9
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