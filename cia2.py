import sys

# Check if exactly 3 command-line arguments are passed (script name + 3 values)
if len(sys.argv) == 4:
    print("Using user-provided values...")
    price1 = float(sys.argv[1])
    price2 = float(sys.argv[2])
    price3 = float(sys.argv[3])
else:
    print("No proper parameters given. Using default values...")
    price1 = 10
    price2 = 30
    price3 = 20.00

minimum = min(price1, price2, price3)
maximum = max(price1, price2, price3)
average = (price1 + price2 + price3) / 3

print("Minimum price:", minimum)
print("Maximum price:", maximum)
print("Average price:", average)
