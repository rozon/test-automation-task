import allure
import requests
import math


@allure.step("Verify /add API Method")
def verify_add(url, x, y, route):
    verification_list = verify(url, x, y, route)
    print_list(verification_list, route)
    return len(verification_list)


@allure.step("Verify /minus API Method")
def verify_minus(url, x, y, route):
    verification_list = verify(url, x, y, route)
    print_list(verification_list, route)
    return len(verification_list)


@allure.step("Verify /multiply API Method")
def verify_multiply(url, x, y, route):
    verification_list = verify(url, x, y, route)
    print_list(verification_list, route)
    return len(verification_list)


@allure.step("Verify /divide API Method")
def verify_divide(url, x, y, route):
    verification_list = verify(url, x, y, route)
    print_list(verification_list, route)
    return len(verification_list)


@allure.step("Verify /sqrt API Method")
def verify_sqrt(url, x, y, route):
    verification_list = verify(url, x, y, route)
    print_list(verification_list, route)
    return len(verification_list)


def verify(url, x, y, route):
    verification_errors = []
    for a in range(x, y):
        if "sqrt" not in route:
            for b in range(x, y):
                with allure.step(
                        "Verify method with values a=%d and b=%d" % (a, b)):
                    request = get_request(url, a, b)
                    local = parse_route(route, a, b)
                    try:
                        assert local == request
                    except AssertionError:
                        error = {'a': a,
                                 'b': b,
                                 'expected': local,
                                 'response': request
                                 }
                        verification_errors.append(error)
        else:
            with allure.step("Verify method with value a=%d" % a):
                request = get_request(url, a)
                local = parse_route(route, a)
                try:
                    assert local == request
                except AssertionError:
                    error = {'a': a,
                             'expected': local,
                             'response': request
                             }
                    verification_errors.append(error)
    return verification_errors


def get_request(url, a, b=None):
    payload = {'a': a}
    if "/sqrt" not in url:
        payload['b'] = b
    r = requests.get(url, params=payload)
    return r.json()


def parse_route(route, a, b=None):
    if "add" in route:
        return a + b
    elif "minus" in route:
        return a - b
    elif "multiply" in route:
        return a * b
    elif "divide" in route:
        return "Infinity" if b == 0 else a / b
    elif "sqrt" in route:
        return "NaN" if a < 0 else math.sqrt(a)


def print_list(error_list, route):
    for error in error_list:
        if "sqrt" in route:
            print("ERROR: on operation sqrt(%d)" % error.get('a'))
        elif "add" in route:
            print("ERROR: on operation %d + %d"
                  % (error.get('a'), error.get('b')))
        elif "minus" in route:
            print("ERROR: on operation %d - %d"
                  % (error.get('a'), error.get('b')))
        elif "multiply" in route:
            print("ERROR: on operation %d * %d"
                  % (error.get('a'), error.get('b')))
        elif "divide" in route:
            print("ERROR: on operation %d / %d"
                  % (error.get('a'), error.get('b')))
        print("\tExpected value: %s" % str(error.get('expected')))
        print("\tResponse value: %s" % str(error.get('response')))
        print("=" * 50)
