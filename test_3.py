import pytest
from main import add


def test_simple():
    assert add(1, 2) == 3


@pytest.mark.parametrize(
    'failed_value',
    ((), {}, [], None, "str", sum, object),
)
def test_bad_value(failed_value):
    assert add(failed_value, 1) == "Bad value"
