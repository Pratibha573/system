import sys

# Check if exactly 3 command-line arguments are given
if len(sys.argv) == 4:
    prices = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
else:
    print("No proper parameters given. Please enter values manually...")
    prices = []
    prices.append(float(input("Enter price1: ")))
    prices.append(float(input("Enter price2: ")))
    prices.append(float(input("Enter price3: ")))

minimum = min(prices)
maximum = max(prices)
average = sum(prices) / len(prices)

print("Minimum price:", minimum)
print("Maximum price:", maximum)
print("Average price:", average)
