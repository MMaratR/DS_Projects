import pytest
from financial import financial

def test_one():
    assert financial('MSFT','Total Revenue') == ('Total Revenue', '254,190,000', '245,122,000', '211,915,000', '198,270,000', '168,088,000')

def test_two():
    assert isinstance(financial('MSFT','Total Revenue'), tuple)

def test_three():
    with pytest.raises(Exception):
        financial('sdfsdf', 'Total Revenue')

def test_four():
    with pytest.raises(Exception):
        financial('MSFT', 'Total')