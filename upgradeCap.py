import requests
import json

def get_package_history(upgradeCap):
    payload = {
        "method": "suix_queryTransactionBlocks",
        "jsonrpc": "2.0",
        "params": [
            {
                "filter": {
                    "ChangedObject": upgradeCap
                },
                "options": {
                    "showInput": False,
                    "showRawInput": False,
                    "showEffects": True,
                    "showEvents": False,
                    "showObjectChanges": False,
                    "showBalanceChanges": False
                }
            },
            None,
            200,
            True
        ],
        "id": "1"
    }

    response = requests.post(url='https://fullnode.mainnet.sui.io', json=payload)

    if response.status_code == 200:
        result = response.json()
        publish_data = filter(lambda d: 'created' in d['effects'], result['result']['data'])
        created_objs = map(lambda d: d['effects']['created'], publish_data)
        flattened = sum(created_objs, [])
        packages = [p['reference']['objectId'] for p in flattened if p['owner'] == 'Immutable']
        return packages

# print(get_package_history("0x38527d154618d1fd5a644b90717fe07cf0e9f26b46b63e9568e611a3f86d5c1a"))