from random import randint
from web3 import Web3, TestRPCProvider, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract
from web3 import Account
import requests
import time
import os
import json
from solc import compile_source
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def compile_source_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()

    return compile_source(source)


class OwnerTokenFactory(object):
    PRIVATE_KEY = os.environ['PRIVATE_KEY']
    ADDRESS = os.environ['ADDRESS']

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def create_contract_tx_hash(self):
        compiled_sol = compile_source_file('%s/contract/OwnerToken.sol' % BASE_DIR)
        contract_interface = compiled_sol['<stdin>:OwnerToken']

        # web3.py instance
        w3 = Web3(HTTPProvider('https://rinkeby.infura.io/SKMV9xjeMbG3u7MnJHVH'))

        # Instantiate and deploy contract
        contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

        with open('%s/contract/owner_contract_abi.json' % BASE_DIR, 'w') as outfile:
            json.dump(contract_interface['abi'], outfile)

        data = contract._encode_constructor_data(args=(self.name, self.symbol))
        transaction = {'data': data,
                       'gas': w3.toHex(1000000),
                       'gasPrice': w3.toWei('1000', 'gwei'),
                       'chainId': 4,
                       'to': '',
                       'from': self.ADDRESS,
                       'nonce': w3.eth.getTransactionCount(self.ADDRESS, "pending")
                       }
        acct = Account.privateKeyToAccount(self.PRIVATE_KEY)
        signed = acct.signTransaction(transaction)
        tx = w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_hash = w3.toHex(tx)
        return tx_hash


# print(OwnerTokenFactory('Owner coin', 'OWN').create_contract_tx_hash())
