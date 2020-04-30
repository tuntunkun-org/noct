import pytest

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
	pass

