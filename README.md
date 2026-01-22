## Solana Wallet Generator & Balance Checker

## 📃 Description
This Python script automatically generates new Solana addresses, checks their balance, and saves wallets with a non-zero balance to the `solana_wallets.txt` file, 24h and you will find a wallet with balance.

## 📝 Features
- Generates random Solana addresses and private keys.
- Checks wallet balance using the Solana JSON-RPC API.
- Automatically saves wallets with a balance > 0 to `solana_wallets.txt`.

## 🛠 Requirements
- Python 3.6+
- Installed dependencies (see below)

## ⚙️ Installation & Usage
1. **Clone the repository or download the script**:
   ```bash
   git clone https://github.com/egreidanus/SolanaFinder.git
   cd solana-wallet-checker
   ```
2. **Install required libraries**:
   ```bash
   pip install requests pynacl base58 colorama
   ```
3. **Run the script**:
   ```bash
   python app.py
   ```

## 🔄 How It Works?
1. The script creates a new key pair (private + public).
2. The public key is converted into a Solana address.
3. A request is sent to `https://api.mainnet-beta.solana.com` to check the balance.
4. If the balance is greater than 0, the wallet is saved to `solana_wallets.txt`.
5. Gen 5 wallets per second

## 📁 Saved Wallet Format
If an address has a balance, it is recorded in `solana_wallets.txt` in the following format:
```
Address: 3nBg2Z...k1T8
Private Key: 5H2pZ...6yF5
Balance: 1000000000 lamports (1 SOL)
----------------------------------------
```

## ⚠️ Warning!
- **Do not share your private keys!** Anyone with a private key can steal funds from the wallet.
- Use this tool **for educational purposes only**.

## 👨‍💻 Author
**Eelco Greidanus** – [GitHub](https://github.com/Tieuvanna)

## ✅ License
This project is distributed under the **MIT** license.

## 🪙 Support Me
Any donation will make me happy and will keep this project online :)
SOL: `DMWGUXuEEaVY4xT4jcEZPace76J2DYV4FXPBmk9411sc`
BTC: `bc1qtj5c7mg9c5mmg0mv84reh7emwl5j9scqnwzfak`
ETH: `0xe547e12225a52A6cc9A4a4ea6a352fFCAF38ae4C`
