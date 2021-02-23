from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    with patch('random.sample', return_value = 1):
        assert next(gen) == '#010101'
    pass