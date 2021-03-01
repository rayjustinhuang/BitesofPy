from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

test_colors = [(117, 156, 138, '#759C8A'),
                (25, 100, 50, '#196432'),
                (203, 196, 204, '#CBC4CC'),
                (1, 1, 1, '#010101'),
                (255, 255, 255, '#FFFFFF')]
                
def replace_sample(sample_space, n):
    if sample_space != range(0, 256):
        raise ValueError
    if n != 3:
        raise ValueError
    return (117,156,138)

@patch('color.sample', replace_sample)
def test_gen_hex_color(replace_sample, gen):
    assert next(gen) == '#759C8A'
    replace_sample.assert_called_with(range(0, 256), 3)
    pass

@pytest.mark.parametrize('red, blue, green, expected', test_colors)
@patch('color.sample')
def test_gen_hex_color(mock_sample, gen, red, blue, green, expected):
    mock_sample.return_value = red, blue, green
    assert next(gen) == expected
    mock_sample.assert_called_with(range(0, 256), 3)
    pass