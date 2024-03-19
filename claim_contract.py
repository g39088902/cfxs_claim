from rpc import w3
claim_contract_address = "0x5C3C1a119300669990863861a854616eCb04b463"
claim_contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256[]","name":"id","type":"uint256[]"},{"indexed":false,"internalType":"address","name":"to","type":"address"}],"name":"CFXsCreated","type":"event"},{"inputs":[],"name":"CFXsOldCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"Id","type":"uint256[]"}],"name":"ExTestToMain","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_oldAddr","type":"address"},{"internalType":"address","name":"_newAddr","type":"address"}],"name":"SetupCFXsAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"_setting","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"allowed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newAddr","type":"address"}],"name":"changeSetupAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"counterinfo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"minted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
claim_contract = w3.eth.contract(address=claim_contract_address, abi=claim_contract_abi)