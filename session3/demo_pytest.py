import pytest


def calculate_mean(values):
    return sum(values) / len(values)


@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3], 2.0),
    ([4, 5, 6], 5.0),
    ([7, 8, 9], 8.0),
])
def test_calculate_mean(values, expected):
    result = calculate_mean(values)
    assert result == pytest.approx(expected, abs=1e-9)


@pytest.mark.slow
def test_calculate_mean_with_large_values():
    values = [1000000, 1000001, 1000002]
    expected = 1000001.0
    result = calculate_mean(values)
    assert result == pytest.approx(expected, abs=1e-9)
