from sentinel.config import Config
def test_defaults():
    assert Config.TIMEOUT == 10
