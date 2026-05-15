import csv

stock = {"AAPL": 180, "MSFT": 420, "TSLA": 250}
portfolio = {}
total = 0

file_name = input("Enter file name: ")

if file_name.strip() == "":
    print("Invalid file name")
else:
    file = open(file_name + ".csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["Stock", "Price", "Investment"])

    while True:

        stock_name = input("Enter stock (AAPL/MSFT/TSLA or stop): ")

        if stock_name == "stop":
            break

        if stock_name not in stock:
            print("Invalid stock name")
            continue

        shares = int(input("Enter number of shares: "))

        price = stock[stock_name]
        investment = shares * price

        if stock_name in portfolio:
            portfolio[stock_name]["shares"] += shares
            portfolio[stock_name]["investment"] += investment
        else:
            portfolio[stock_name] = {
                "shares": shares,
                "investment": investment
            }

        total += investment

        writer.writerow([stock_name, price, investment])

        print("Portfolio:", portfolio)
        print("Total Investment:", total)

    file.close()
    print("File saved successfully!")