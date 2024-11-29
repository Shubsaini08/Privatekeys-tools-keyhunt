import urllib3
from urllib3 import util
import json
import math
import os

LIMIT = 120
SATOSHI = 1e+8

# Define the file paths
INPUT_FILE = 'outputs.txt'
OUTPUT_FILE = 'balance.txt'
LOG_FILE = 'check.log'

def check_balance(fi, fo, log_file):
    # Load already checked addresses from log file
    checked_addresses = set()
    if os.path.exists(log_file):
        with open(log_file, 'r') as log:
            checked_addresses = set(line.strip() for line in log)

    print('loading addresses...')
    with open(fi) as f1:
        addresses = [l.strip() for l in f1 if l.strip() not in checked_addresses]

    print('addresses loaded:', len(addresses))
    if not addresses:
        print("No new addresses to check. Exiting.")
        return

    print('getting balances info...')
    http = urllib3.PoolManager(timeout=util.Timeout(10))

    total = len(addresses)
    steps = math.floor(total / LIMIT)
    remind = total % LIMIT

    # Initialize counters for addresses with and without balance
    addresses_with_balance = 0
    addresses_without_balance = 0

    with open(fo, 'a') as f2, open(log_file, 'a') as log:
        for step in range(steps + 1):
            url = 'https://blockchain.info/balance?active='
            if step < steps:
                for a in range(step * LIMIT, (step + 1) * LIMIT):
                    url += addresses[a] + '|'
            else:
                for a in range(steps * LIMIT, steps * LIMIT + remind):
                    url += addresses[a] + '|'
            url = url[:-1]

            try:
                res = http.request('GET', url, timeout=util.Timeout(10), retries=util.Retry(10))
                data = json.loads(res.data.decode('utf-8'))

                for address in data:
                    balance = data[address]['final_balance'] / SATOSHI
                    n_tx = data[address]['n_tx']
                    
                    # Log and save based on balance
                    if balance > 0:
                        addresses_with_balance += 1
                        b = '{0:.8f} '.format(balance)
                        f2.write(f"{address}\t\t\t{b}\t\t\t{n_tx}\n")
                    else:
                        addresses_without_balance += 1
                        print(f"Address {address} has zero balance.")
                    
                    # Add checked address to log
                    log.write(address + '\n')

            except Exception as e:
                print(f"Error occurred while processing step {step}: {e}")

    print('complete')
    
    # Print summary in colors
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print(f"\033[92mNumber of addresses having balance: {addresses_with_balance}\033[0m")
    print(f"\033[91mNumber of addresses not having balance: {addresses_without_balance}\033[0m")

if __name__ == '__main__':
    check_balance(INPUT_FILE, OUTPUT_FILE, LOG_FILE)

