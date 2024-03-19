import time
from rpc import w3,acct
from mint_contract import mint_contract
from my_tx import mint_tx_list,claim_tx_list

minted_ids = []
claimed_ids = []
for tx in mint_tx_list:
    time.sleep(0.1)
    receipt = w3.eth.get_transaction_receipt(tx["hash"])
    event_log = mint_contract.events.CFXsCreated().process_receipt(receipt)
    for event in event_log:
        if event['args']['to'] == acct.address:
            minted_ids.append(event['args']['id'])
print("Minted IDs:",minted_ids)
print("Minted IDs Count:",len(minted_ids))