import argparse
from app.alert import check_alert

def main():
    parser = argparse.ArgumentParser(prog="crypto-alerts")
    parser.add_argument("--coin", type=str, default="bitcoin", help="ID монеты (CoinGecko)")
    parser.add_argument("--min", type=float, default=None, help="Минимальный порог")
    parser.add_argument("--max", type=float, default=None, help="Максимальный порог")
    args = parser.parse_args()

    check_alert(args.coin, args.min, args.max)

if __name__ == "__main__":
    main()
