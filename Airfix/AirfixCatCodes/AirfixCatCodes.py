# Airfix catalogue number parity check digit generator
# Converted from Pascal to Python
# Original (c) 2013 Steven S. Pietrobon
# Conversion by ChatGPT (GPT-5), 2025

def main():
    ca = [3, 7, 9, 3, 7]
    print("Airfix catalogue number parity check digit generator.")
    print("Enter five digit catalogue number to get parity check digit.")
    print("Enter negative number to exit program.")
    print("For catalogue code ABCDE-F, then F = (7A+3B+9C+7D+3E) modulo 10.")
    print("Copyright (c) 2013 Steven S. Pietrobon. Version 1.0 14 Mar 2013.\n")

    while True:
        try:
            c = int(input("Enter code: "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue

        e = c
        d = 0

        if c < 0:
            print("Exiting program.")
            break

        # Calculate check digit
        for coeff in ca:
            d += (c % 10) * coeff
            c //= 10

        # Display formatted result
        print(f"Code = {e:05d}-{d % 10}\n")


if __name__ == "__main__":
    main()