import unittest
from app.speed_test import run_speed_test

class TestSpeedTest(unittest.TestCase):
    def test_run_speed_test(self):
        result = run_speed_test()
        self.assertIn('download', result)
        self.assertIn('upload', result)
        self.assertIn('ping', result)