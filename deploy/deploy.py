from brownie1 import Recycle, accounts


def main():
    deployer = accounts.load(input('brownie1 account: '))
    return Recycle.deploy({'from': deployer})
