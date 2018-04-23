import smoke_test_cases as tc

BASE_URL = "http://localhost:8080/math"


def test_add():
    route = "/add"
    url = BASE_URL + route
    assert not tc.verify_add(url, route.replace("/", ""))


def test_minus():
    route = "/minus"
    url = BASE_URL + route
    assert not tc.verify_minus(url, route.replace("/", ""))


def test_multiply():
    route = "/multiply"
    url = BASE_URL + route
    assert not tc.verify_multiply(url, route.replace("/", ""))


def test_divide():
    route = "/divide"
    url = BASE_URL + route
    assert not tc.verify_divide(url, route.replace("/", ""))


def test_sqrt():
    route = "/sqrt"
    url = BASE_URL + route
    assert not tc.verify_sqrt(url, route.replace("/", ""))
