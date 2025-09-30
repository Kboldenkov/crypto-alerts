import requests

def get_price(coin_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url, timeout=10).json()
    return data.get(coin_id, {}).get("usd", 0.0)

def check_alert(coin: str, min_price: float = None, max_price: float = None):
    price = get_price(coin)
    print(f"{coin.upper()} price: ${price:.2f}")

    if min_price is not None and price < min_price:
        print(f"⚠️ ALERT: {coin.upper()} ниже минимума {min_price}")
    if max_price is not None and price > max_price:
        print(f"⚠️ ALERT: {coin.upper()} выше максимума {max_price}")
