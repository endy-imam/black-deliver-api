"""Testing utility function for deliver.models.utils
"""

import pytest

from deliver.models.utils import to_lower_camel


# to_lower_camel

def test_empty_to_lower_camel():
    """Testing to_lower_camel on empty string
    """
    input_ = ''
    output = to_lower_camel(input_)
    expect = ''
    assert output == expect

@pytest.mark.parametrize('test_input, expected', [
    ('hello'  , 'hello'  ),
    ('foo'    , 'foo'    ),
    ('bar'    , 'bar'    ),
    ('for1'   , 'for1'   ),
    ('4runner', '4runner'),
])
def test_single_to_lower_camel(test_input, expected):
    """Testing to_lower_camel on single word
    """
    output = to_lower_camel(test_input)
    assert output == expected

@pytest.mark.parametrize('test_input, expected', [
    ('hello_world', 'helloWorld'),
    ('foo_bar_baz', 'fooBarBaz'),
])
def test_multi_to_lower_camel(test_input, expected):
    """Testing to_lower_camel on multi word
    """
    output = to_lower_camel(test_input)
    assert output == expected
