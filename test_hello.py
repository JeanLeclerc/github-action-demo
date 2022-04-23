from hello import add

import pytest

def test_add():
    assert 2 == add(1,1)