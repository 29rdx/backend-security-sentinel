import unittest

def suite():
    loader = unittest.TestLoader()
    return loader.discover("tests", pattern="test_*.py")

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    if not result.wasSuccessful():
        exit(1)
