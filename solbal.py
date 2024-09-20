import json
import os
import requests

def check_balance_rpc(url, address):
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [address]
    })

    try:
        response = requests.post(url, headers=headers, data=payload, timeout=5)
        result = response.json()

        if 'error' in result:
            return 0  # Error retrieving balance

        if 'result' in result and 'value' in result['result']:
            return result['result']['value']
        else:
            return 0  # Unexpected response structure
    except requests.exceptions.RequestException:
        return None  # Connection error

def format_balance(lamports):
    sol_balance = lamports / 1_000_000_000  # Convert lamports to SOL
    return f"◎{sol_balance:.9f}"  # Format to 9 decimal places

def green(text):
    os.system("")  # Ensures the terminal supports ANSI escape codes
    faded = ""
    green = 250
    for line in text.splitlines():
        blue = 255
        for character in line:
            blue -= 5
            if blue < 0:
                blue = 0
            faded += (f"\033[38;2;0;{green};{blue}m{character}\033[0m")
        faded += "\n"
    return faded

def save_to_file(solana_address, balance):
    with open("found.txt", "a") as file:
        file.write(f"Solana Address: {solana_address}, Balance: {format_balance(balance)}\n")

def check_address_balance_and_save(rpc_urls, solana_address):
    balance = None
    for rpc_url in rpc_urls:
        balance = check_balance_rpc(rpc_url, solana_address)
        if balance is not None:
            break

    if balance is not None and balance > 0:
        save_to_file(solana_address, balance)
        return f"Found! Address: {solana_address}, Balance: {format_balance(balance)}"
    return f"Checked Address: {solana_address}, Balance: {format_balance(0 if balance is None else balance)}"

def main():
    rpc_urls = [
        "https://api.mainnet-beta.solana.com",
        "https://api.testnet.solana.com",
        "https://api.devnet.solana.com"
    ]

    checked_addresses = set()  # To keep track of already checked addresses
    total_found = 0  # Initialize the count of found addresses with positive balance
    total_scanned = 0  # Initialize the count of total addresses scanned

    print(green("Starting address balance checking...\n"))

    with open("sol.txt", "r") as file:
        for line in file:
            solana_address = line.strip()
            if solana_address not in checked_addresses:
                checked_addresses.add(solana_address)
                total_scanned += 1
                result = check_address_balance_and_save(rpc_urls, solana_address)
                print(result)

    print(f"\nTotal addresses scanned: {total_scanned}")
    print(f"Total addresses found with positive balance: {total_found}")
    print(green("\nScript execution completed."))
    print(green("\nCREDIT GOES TO CLOUD NATHY @cloudnathy"))
    print(green("\nJOIN https://t.me/cloud_hunter_sa TeleGroup -Reeditied by shub"))
if __name__ == "__main__":
    main()
