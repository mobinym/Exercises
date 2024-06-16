import requests
import sys

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
    except requests.RequestException:
        print("Error: Unable to reach CoinDesk API.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    price_per_bitcoin = get_bitcoin_price()
    total_cost = num_bitcoins * price_per_bitcoin

    print(f"The current cost of {num_bitcoins} Bitcoins is ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
