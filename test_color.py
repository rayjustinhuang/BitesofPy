from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

test_colors = [(117, 156, 138, '#759C8A'),
                (25, 100, 50, '#196432')]

@pytest.mark.parametrize('red, blue, green, expected', test_colors)
@patch('color.sample')
def test_gen_hex_color(mock_sample, gen, red, blue, green, expected):
    mock_sample.return_value = red, blue, green
    assert next(gen) == expected
    pass