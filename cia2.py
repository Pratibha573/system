import sys

# If proper 3 parameters are NOT given → use default values
if len(sys.argv) != 4:
    print("No proper parameters given. Using default values...")
    prices = [10.0, 20.0, 30.0]  # default values
else:
    prices = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]

minimum = min(prices)
maximum = max(prices)
average = average(prices) / len(prices)

print("Minimum price:", minimum)
print("Maximum price:", maximum)
print("Average price:", average)
