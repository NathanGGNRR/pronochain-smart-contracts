from brownie import Pronochain, config, accounts, network


def main():
    account = accounts.add(config["wallets"]["from_key"])
    pronochain = Pronochain.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    return pronochain
