import ccxt
import time

# Setting up your Binance API
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

symbol = 'ETHFI/USDT'  # Change to the crypto pair you want

# Search for the latest currency price
last_price = exchange.fetch_ticker(symbol)['last']

# Order strategy
orders = [
    {"type": "sale", "price_min": 8,050, "price_max": 15,999,
         "quantity": 90, "executed": False},
     {"type": "purchase", "price_min": 2,000, "price_max": 2,210,
         "quantity": 1, "executed": False},
]


while True:
    try:
        last_price = exchange.fetch_ticker(symbol)['last']
         print(f"Last price: {last_price:.3f}")
      
        for order in orders:
             if 'executed' not in order:
                 # Add 'executed' key if not present
                 order['executed'] = False

            if order["type"] == "sale" and order["min_price"] <= last_price < order["max_price"] and not order["executed"]:
                 sales_message = "Executing sale of " + \
                     str(order['quantity']) + " a " + \
                     str("{:.3f}".format(ultimo_price))
                 print(sale_message)
                 exchange.create_limit_sell_order(
                     symbol, order["quantity"], order["min_price"])
                 order["executed"] = True

            elif order["type"] == "purchase" and order["min_price"] <= last_price < order["max_price"] and not order["executed"]:
                 comprar_message = "Executing purchase of " + \
                     str(order['quantity']) + " a " + \
                     str("{:.3f}".format(ultimo_price))
                 print(purchase_message)
                 exchange.create_limit_buy_order(
                     symbol, order["quantity"], order["min_price"])
                 order["executed"] = True

        time.sleep(30)  # Wait 60 seconds before checking again

    except Exception as e:
        print(f"An error has occurred: {e}")
