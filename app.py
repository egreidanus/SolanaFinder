import time
import requests
import base58
import nacl.signing
from colorama import Fore, Style, init
import sys

class SolanaFinder:
    def __init__(self):
        self.generated_wallets = 0
        self.found_wallets_with_balance = 0
        self.wallet_file = "solana_wallets.txt"
        self.rpc_url = "https://api.mainnet-beta.solana.com"
        self.running = False

    def generate_solana_address(self):
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        sol_address = base58.b58encode(verify_key.encode()).decode()
        solana_private_key = signing_key.encode() + verify_key.encode()
        private_key_base58 = base58.b58encode(solana_private_key).decode()
        return sol_address, private_key_base58

    def get_solana_balance(self, address):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [address]
        }
        try:
            response = requests.post(self.rpc_url, json=payload, timeout=5)
        except requests.exceptions.RequestException:
            return None
        if response.status_code != 200:
            return None
        data = response.json()
        return data.get("result", {}).get("value", 0)

    def save_wallet(self, address, private_key, balance):
        with open(self.wallet_file, "a") as file:
            file.write(
                f"Address: {address}\n"
                f"Private Key: {private_key}\n"
                f"Balance: {balance} lamports\n"
                f"{'-'*40}\n"
            )
        print(Fore.MAGENTA + f"Wallet saved to {self.wallet_file}")

    def print_status(self, wallet_info):
        sys.stdout.write("\033[H")  # move cursor to top left
        sys.stdout.write(wallet_info)
        sys.stdout.flush()

    def main(self):
        self.running = True
        print("\033[2J")  # clear screen once
        while True:
            sol_address, private_key_base58 = self.generate_solana_address()
            balance = self.get_solana_balance(sol_address)
            self.generated_wallets += 1

            if balance is None:
                time.sleep(0.2)
            else:
                lamports = balance
                sol = lamports / 1000000000
                info = (
                    f"╔════════════════════════════════════════════════════════════════════════════════════╗\n"
                    f"║                                Solana Wallet Finder                                ║\n"
                    f"╚════════════════════════════════════════════════════════════════════════════════════╝\n\n"
                    f"Total generated wallets:                {self.generated_wallets}\n"
                    f"Total found wallets with balance:       {self.found_wallets_with_balance}\n\n"
                    f"Current Job:\n"
                    f"Solana Address:   {sol_address}\n"
                    f"Private Key:      {private_key_base58}\n"
                    f"Balance:          {lamports} lamports ({sol} SOL)\n"
                )
                if lamports > 0:
                    self.found_wallets_with_balance = self.found_wallets_with_balance + 1
                    self.save_wallet(sol_address, private_key_base58, lamports)

            self.print_status(info)
            time.sleep(0.175)

if __name__ == "__main__":
    app = SolanaFinder()
    app.main()
