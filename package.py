import requests
import json
import sys
import os

# package = sys.argv[1]
package = "0x5511b2d3550fcdce424bc24623d97e7ac99e4acf968d1cb61aacbb6e4c6605e5"

def get_package_disassembled(package):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "sui_getObject",
        "params": [
            package,
            {
                "showType": False,
                "showOwner": False,
                "showPreviousTransaction": False,
                "showDisplay": False,
                "showContent": True,
                "showBcs": False,
                "showStorageRebate": False
            }
        ]
    }

    response = requests.post(url='https://fullnode.mainnet.sui.io', json=payload)

    if response.status_code == 200:
        result = response.json()

        try:
            return result['result']['data']['content']['disassembled']
        except Exception as e:
            print(result)
            raise e


def save_disassembled(disassembled, prefix):
    os.mkdir(prefix)

    for name, code in disassembled.items():
        # print(f"File: {name}")
        with open(f"{prefix}/{name}.mv", "w") as file:
            file.write(code)