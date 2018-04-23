import pytest


def pytest_addoption(parser):
    parser.addoption("--x", action="store", default=-10,
                     help="number")
    parser.addoption("--y", action="store", default=10,
                     help="number")


@pytest.fixture
def x(request):
    return request.config.getoption("--x")


@pytest.fixture
def y(request):
    return request.config.getoption("--y")