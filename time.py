import math

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def calculate_time_needed(keys_per_sec, target_keys):
    seconds_per_day = 60 * 60 * 24
    days = target_keys / keys_per_sec / seconds_per_day
    weeks = days / 7
    months = days / 30
    years = days / 365
    decades = years / 10
    
    print_green(f"MINUTES: {target_keys / keys_per_sec / 60:.2f}")
    print_green(f"HOURS: {target_keys / keys_per_sec / 3600:.2f}")
    print_green(f"DAYS: {days:.2f}")
    print_green(f"WEEKS: {weeks:.2f}")
    print_green(f"MONTHS: {months:.2f}")
    print_green(f"YEARS: {years:.2f}")
    print_green(f"DECADES: {decades:.2f}")

def main():
    target = 73786976294838206464
    options = {
        1: 1_000_000,
        2: 10_000_000,
        3: 100_000_000,
        4: 1_000_000_000,
        5: 10_000_000_000
    }
    
    print("Choose an option:")
    for key, value in options.items():
        print(f"Option {key}: {value}")

    option = int(input("Option (or type 6 to enter a custom amount): "))

    if option == 6:
        amount = int(input("Enter the amount: "))
    elif option in options:
        amount = options[option]
    else:
        print("Invalid option.")
        return

    keys_per_sec = target / amount
    print_red(f"{target} ÷ {amount} = {keys_per_sec:.2f} keys/second")

    calculate_time_needed(keys_per_sec, target)

if __name__ == "__main__":
    main()

