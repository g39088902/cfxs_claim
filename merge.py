import re
import httpx
from rpc import acct
from merge_contract import merge

resp = httpx.get(f"https://www.cfxs.world/api/cfxs/my/new?index=0&market=0&merged=1&owner={acct.address}&size=2000")
merge_ids = []
for item in resp.json()['rows']:
    id = item['id']
    match = re.search(r'(\\d)\\1{4}', id)
    if match:
        print("Protect ID:",id)
    else:
        merge_ids.append(int(id))
    while len(merge_ids) >= 24:
        if merge(merge_ids):
            merge_ids = []
while len(merge_ids) > 12:
    if merge(merge_ids):
        merge_ids = []