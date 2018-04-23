import smoke_test_cases as tc

BASE_URL = "http://localhost:8080/math"


def test_add(x, y):
    route = "/add"
    url = BASE_URL + route
    assert not tc.verify_add(url, int(x), int(y), route.replace("/", ""))


def test_minus(x, y):
    route = "/minus"
    url = BASE_URL + route
    assert not tc.verify_minus(url, int(x), int(y), route.replace("/", ""))


def test_multiply(x, y):
    route = "/multiply"
    url = BASE_URL + route
    assert not tc.verify_multiply(url, int(x), int(y), route.replace("/", ""))


def test_divide(x, y):
    route = "/divide"
    url = BASE_URL + route
    assert not tc.verify_divide(url, int(x), int(y), route.replace("/", ""))


def test_sqrt(x, y):
    route = "/sqrt"
    url = BASE_URL + route
    assert not tc.verify_sqrt(url, int(x), int(y), route.replace("/", ""))
