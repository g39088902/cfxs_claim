import os

from rpc import w3,acct
claim_contract_address = w3.to_checksum_address("0x5c3c1a119300669990863861a854616ecb04b463")
claim_contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256[]","name":"id","type":"uint256[]"},{"indexed":false,"internalType":"address","name":"to","type":"address"}],"name":"CFXsCreated","type":"event"},{"inputs":[],"name":"CFXsOldCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"Id","type":"uint256[]"}],"name":"ExTestToMain","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_oldAddr","type":"address"},{"internalType":"address","name":"_newAddr","type":"address"}],"name":"SetupCFXsAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"_setting","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"allowed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newAddr","type":"address"}],"name":"changeSetupAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"counterinfo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"minted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'
claim_contract = w3.eth.contract(address=claim_contract_address, abi=claim_contract_abi)

def claim(ids:list):
    func = claim_contract.functions.ExTestToMain(ids)
    try:
        tx = func.build_transaction(
            {
                "from": acct.address,
                "nonce": w3.eth.get_transaction_count(acct.address),
                "gas": 15000000,
                "gasPrice": 20000000000,
            }
        )
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print("Claiming IDs:",ids)
        print("Claiming TX Hash:",tx_hash.hex())
        # wait for the transaction to be mined
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print("Claiming IDs:",ids)
        print("Claiming Error:",e)
        return False

if __name__ == "__main__":
    print("Gas price:",w3.eth.gas_price)
    unclaimed_ids = [1930433, 1928665, 1927371, 1924964, 1923377, 1922729, 1922237, 1921598, 1920369, 1919554, 1916779, 1915978, 1915022, 1913464, 1913006, 1909051, 1908026, 1906847, 1903616, 1903147, 1902538, 1899638, 1899248, 1896835, 1896014, 1895142, 1894148, 1892996, 1891475, 1890085, 1889220, 1888242, 1887767, 1887067, 1886084, 1884472, 1882524, 1881825, 1879568, 1878975, 1878154, 1877358, 1872578, 1872136, 1870980, 1870449, 1869856, 1869589, 1869003, 1868509, 1867726, 1862079, 1861118, 1860638, 1860035, 1859200, 1857620, 1856943, 1853362, 1851676, 1850459, 1849706, 1846465]
    claim(unclaimed_ids[:32])