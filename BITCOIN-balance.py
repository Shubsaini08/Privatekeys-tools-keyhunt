import sys
import re
from time import sleep

try:    # if Python 3
    from urllib.request import urlopen
except ImportError: # if Python 2
    from urllib2 import urlopen

def check_balance(address):

    # Modify the value of the variable below to False if you do not want Bell Sound when the Software finds balance.
    SONG_BELL = True

    # Add time different from 0 if you need more security on the checks
    WARN_WAIT_TIME = 0

    blockchain_tags_json = [ 
        'total_received',
        'final_balance',
    ]

    SATOSHIS_PER_BTC = 1e+8

    check_address = address.strip()

    parse_address_structure = re.match(r' *(1[0-9A-Za-z]{25,34}|3[0-9A-Za-z]{25,34}|bc1[0-9A-Za-z]{25,100})', check_address)
    if parse_address_structure is not None:
        check_address = parse_address_structure.group(1)
    else:
        print("\nThis Bitcoin Address is invalid: " + check_address)
        return

    # Read info from Blockchain about the Address
    reading_state = 1
    while reading_state:
        try:
            htmlfile = urlopen("https://blockchain.info/address/%s?format=json" % check_address, timeout=10)
            htmltext = htmlfile.read().decode('utf-8')
            reading_state = 0
        except Exception as e:
            reading_state += 1
            print("Checking... " + str(reading_state) + " (Error: %s)" % str(e))
            if reading_state >= 5:
                print("Failed to retrieve data for address: %s. Skipping after multiple attempts." % check_address)
                return
            sleep(60 * reading_state)

    print("\nBitcoin Address = " + check_address)

    blockchain_info_array = []
    tag = ''
    try:
        for tag in blockchain_tags_json:
            blockchain_info_array.append(float(re.search(r'%s":(\d+),' % tag, htmltext).group(1)))
    except Exception as e:
        print("Error processing tag '%s': %s" % (tag, str(e)))
        return

    with open('balance.txt', 'a') as arq1:
        for i, btc_tokens in enumerate(blockchain_info_array):
            sys.stdout.write("%s \t= " % blockchain_tags_json[i])
            if btc_tokens > 0.0:
                print("%.8f Bitcoin" % (btc_tokens / SATOSHIS_PER_BTC))
            else:
                print("0 Bitcoin")

            if SONG_BELL and blockchain_tags_json[i] == 'final_balance' and btc_tokens > 0.0:
                # If you have a balance greater than 0 you will hear the bell
                sys.stdout.write('\a\a\a')
                sys.stdout.flush()

                arq1.write("Bitcoin Address: %s" % check_address)
                arq1.write("\t Balance: %.8f Bitcoin" % (btc_tokens / SATOSHIS_PER_BTC))
                arq1.write("\n")
                if WARN_WAIT_TIME > 0:
                    sleep(WARN_WAIT_TIME)

    with open('check.log', 'a') as log_file:
        log_file.write("%s\n" % check_address)

# Read the log of already checked addresses
try:
    with open('check.log', 'r') as log_file:
        checked_addresses = set(line.strip() for line in log_file)
except FileNotFoundError:
    checked_addresses = set()

# Add the filename of your list of Bitcoin Addresses for checking all.
with open("bit.txt") as file:
    for line in file:
        address = line.strip()
        if address in checked_addresses:
            print("Address %s already checked. Skipping." % address)
            continue
        print("__________________________________________________\n")
        check_balance(address)

print("__________________________________________________\n")

