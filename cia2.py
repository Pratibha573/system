import sys

# Check if exactly 3 command-line arguments are passed (script name + 3 values = length 4)
if len(sys.argv) == 4:
    price1 = float(sys.argv[1])
    price2 = float(sys.argv[2])
    price3 = float(sys.argv[3])
else:
    print("No proper parameters given. Using default values...")
    price1 = 10
    price2 = 30
    price3 = 20.00

# Calculations
maximum = max(price1, price2, price3)
minimum = min(price1, price2, price3)
average = (price1 + price2 + price3) / 3

# Output
print("Prices:", price1, price2, price3)
print("Maximum Price =", maximum)
print("Minimum Price =", minimum)
print("Average Price =", average)
