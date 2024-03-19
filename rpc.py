from web3 import Web3
import os
w3 = Web3(Web3.HTTPProvider('https://evm.confluxrpc.com'))
if w3.is_connected():
    print("Connected to Conflux Network")
else:
    print("Not connected to Conflux Network")
    exit(1)
w3.eth.account.enable_unaudited_hdwallet_features()
acct = w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
print("Address:",acct.address)
print("Balance:",w3.from_wei(w3.eth.get_balance(acct.address), 'ether'), "CFX")