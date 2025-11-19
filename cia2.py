import sys

# If user does NOT give 3 parameters → use default values
if len(sys.argv) != 4:
    print("No proper parameters given. Using default values...")
    prices = [10.0, 30.0, 20.0]  # Default values
else:
    prices = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]

minimum = min(prices)
maximum = max(prices)
average = sum(prices) / len(prices)

print("Minimum price:", minimum)
print("Maximum price:", maximum)
print("Average price:", average)
