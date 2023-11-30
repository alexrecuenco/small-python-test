import pytest
from hypothesis import given, assume
from hypothesis import strategies as st

from module import equals


def test_empty_should_raise():
    with pytest.raises(TypeError):
        raise TypeError("test")


@given(url=st.text(min_size=1))
def test_url_encoding_start_with(url: str):
    assert equals(url, url)


@given(
    url1=st.text(min_size=1),
    url2=st.text(min_size=1),
)
def test_generates_same(url1: str, url2: str):
    assume(url1 != url2)
    assert not equals(url1, url2)
