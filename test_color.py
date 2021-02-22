from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    with patch('random.sample') as random_sample_mock:
        random_sample_mock.return_value = 117, 156, 138
        
        assert next(gen) == '#759C8A'
    pass