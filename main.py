import time
from rpc import w3
from mint_contract import mint_contract
from claim_contract import claim_contract
from my_tx import mint_tx_list,claim_tx_list
from claim_contract import claim

unclaimed_ids = []
for tx in mint_tx_list:
    time.sleep(0.2)
    receipt = w3.eth.get_transaction_receipt(tx["hash"])
    event_log = mint_contract.events.CFXsCreated().process_receipt(receipt)
    for event in event_log:
        unclaimed_ids.append(event['args']['id'])
        print("Add unclaimed ID:",event['args']['id'])
for tx in claim_tx_list:
    time.sleep(0.2)
    transaction = w3.eth.get_transaction(tx["hash"])
    input_data = claim_contract.decode_function_input(transaction.input)
    for id in input_data[1]['Id']:
        if id in unclaimed_ids:
            unclaimed_ids.remove(id)
print("Unclaimed IDs:",unclaimed_ids)
print("Unclaimed IDs Count:",len(unclaimed_ids))
while len(unclaimed_ids) > 0:
    tx_ids = unclaimed_ids[:32]
    if claim(tx_ids):
        unclaimed_ids = unclaimed_ids[32:]
    else:
        time.sleep(2)
    time.sleep(2)
