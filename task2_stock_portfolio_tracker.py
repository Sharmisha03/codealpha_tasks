# -------------------------------
# Stock Portfolio Tracker
# -------------------------------

# Dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 300
}

total_investment = 0

print("===================================")
print("📈 STOCK PORTFOLIO TRACKER")
print("===================================")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.\n")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"✅ Added: {stock} → {quantity} × ${price} = ${investment}\n")

print("-----------------------------------")
print(f"💰 Total Investment Value: ${total_investment}")
print("-----------------------------------")

# Optional file saving
save = input("Do you want to save this data? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write(f"Total Investment: ${total_investment}")
    file.close()
    print("✅ Data saved to portfolio.txt")
else:
    print("📁 Data not saved")
