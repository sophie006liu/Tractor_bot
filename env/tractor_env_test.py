import unittest
import tractor_env

class TractorEnvTest(unittest.TestCase):
    def test_initialize(self):
        tractor_env.TractorEnv()

if __name__ == "__main__":
    unittest.main()
