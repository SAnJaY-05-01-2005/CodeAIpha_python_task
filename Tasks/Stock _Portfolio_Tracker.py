def track_portfolio():
    # 1. SETUP: Hardcoded dictionary of stock prices
    # In a real app, you would fetch these from an API like Yahoo Finance
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 135.50,
        "AMZN": 145.00,
        "MSFT": 320.00
    }

    portfolio_holdings = [] # List to store the user's added stocks
    total_portfolio_value = 0.0

    print("--- Simple Stock Portfolio Tracker ---")
    print("Available stocks: " + ", ".join(stock_prices.keys()))

    # 2. INPUT LOOP: Ask user for stocks until they are done
    while True:
        symbol = input("\nEnter stock symbol (or type 'DONE' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        # Check if the stock exists in our price list
        if symbol in stock_prices:
            try:
                quantity = float(input(f"How many shares of {symbol} do you own? "))
                
                # 3. CALCULATIONS: Arithmetic logic
                price = stock_prices[symbol]
                holding_value = price * quantity
                total_portfolio_value += holding_value
                
                # Save this entry to our list
                portfolio_holdings.append((symbol, quantity, holding_value))
                print(f"Added: {quantity} shares of {symbol} at ${price} each.")
                
            except ValueError:
                print("Error: Please enter a valid number for quantity.")
        else:
            print("Sorry, we don't have price data for that stock. Try AAPL, TSLA, etc.")

    # 4. OUTPUT: Display Summary
    print("\n" + "="*30)
    print("PORTFOLIO SUMMARY")
    print("="*30)
    
    for item in portfolio_holdings:
        # item[0]=Symbol, item[1]=Qty, item[2]=Value
        print(f"{item[0]}:\t {item[1]} shares \t= ${item[2]:.2f}")
        
    print("-" * 30)
    print(f"TOTAL INVESTMENT VALUE: ${total_portfolio_value:.2f}")
    print("=" * 30)

    # 5. FILE HANDLING: Save to a text file
    save_choice = input("\nWould you like to save this to a file? (yes/no): ").lower()
    
    if save_choice == 'yes':
        try:
            with open("portfolio.txt", "w") as file:
                file.write("--- Portfolio Report ---\n")
                for item in portfolio_holdings:
                    file.write(f"{item[0]}: {item[1]} shares = ${item[2]:.2f}\n")
                file.write("-" * 20 + "\n")
                file.write(f"TOTAL VALUE: ${total_portfolio_value:.2f}\n")
            print("Success! Data saved to 'portfolio.txt'.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

# Run the tracker
track_portfolio()