from app.alert import get_price

def test_price():
    price = get_price("bitcoin")
    assert isinstance(price, float)
    assert price >= 0
