import sys

# Define the upper limit of the hexadecimal and decimal range
HEX_MAX = "fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140"
DEC_MAX = 115792089237316195423570985008687907852837564279074904382605163141518161494336

# Function to convert hex to decimal
def hex_to_dec(hex_val):
    try:
        dec_val = int(hex_val, 16)
        return dec_val
    except ValueError:
        return None

# Function to convert decimal to hex
def dec_to_hex(dec_val):
    try:
        hex_val = hex(int(dec_val))[2:].zfill(64)  # Convert to hex and pad with leading zeros
        return hex_val
    except ValueError:
        return None

# Prompt for user input: option 1 for hex to decimal, option 2 for decimal to hex
def get_user_option():
    print("Choose an option:")
    print("1. Hexadecimal to Decimal")
    print("2. Decimal to Hexadecimal")
    return input("Enter option (1 or 2): ")

# Main loop
def main():
    while True:
        option = get_user_option()
        if option == "1":
            # Hexadecimal to Decimal conversion
            hex_input = input("Enter hexadecimal value: ").strip().lower()
            
            # Validate range
            if len(hex_input) > 64 or int(hex_input, 16) > int(HEX_MAX, 16):
                print("Hexadecimal input exceeds maximum range.")
                continue
            
            dec_output = hex_to_dec(hex_input)
            if dec_output is None:
                print("Invalid hexadecimal input.")
            else:
                print(f"Decimal output: {dec_output}")
        
        elif option == "2":
            # Decimal to Hexadecimal conversion
            dec_input = input("Enter decimal value: ").strip()
            
            # Validate range
            try:
                dec_input = int(dec_input)
                if dec_input > DEC_MAX:
                    print("Decimal input exceeds maximum range.")
                    continue
            except ValueError:
                print("Invalid decimal input.")
                continue
            
            hex_output = dec_to_hex(dec_input)
            if hex_output is None:
                print("Error converting decimal to hexadecimal.")
            else:
                print(f"Hexadecimal output: {hex_output}")
        
        else:
            print("Invalid option. Please select 1 or 2.")
        
        # Ask if the user wants to continue or exit
        continue_option = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if continue_option != 'y':
            sys.exit()

if __name__ == "__main__":
    main()

