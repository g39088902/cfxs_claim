from rpc import w3
mint_contract_address = "0xC6e865c213C89Ca42A622c5572D19f00d84d7a16"
mint_conrtract_abi = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"CFXsCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"CFXsDeleted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"string","name":"data","type":"string"}],"name":"CFXsEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"CFXsId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"etherAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"locktime","type":"uint256"}],"name":"CFXsLocked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"CFXsId","type":"uint256"}],"name":"CFXsUnlocked","type":"event"},{"inputs":[],"name":"CFXsCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"CFXss","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"data","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CreateCFXs","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"CFXsId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"DangerTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"LockedCFXs","outputs":[{"internalType":"uint256","name":"_ether","type":"uint256"},{"internalType":"uint256","name":"locktime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"CFXsId","type":"uint256"},{"internalType":"uint256","name":"_ether","type":"uint256"},{"internalType":"uint256","name":"locktime","type":"uint256"}],"name":"LockingScript","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"CFXsId","type":"uint256"}],"name":"OwnerUnlockingScript","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"CFXsId","type":"uint256"}],"name":"UnlockingScript","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getLockStates","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"CFXsId","type":"uint256"},{"internalType":"string","name":"_data","type":"string"}],"name":"inscribe","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256[]","name":"inputs","type":"uint256[]"},{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"data","type":"string"}],"internalType":"struct CFXsContract.OutputCFXsData[]","name":"outputs","type":"tuple[]"}],"internalType":"struct CFXsContract.Transaction","name":"_tx","type":"tuple"}],"name":"processTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'
mint_contract = w3.eth.contract(address=mint_contract_address, abi=mint_conrtract_abi)