import unittest
from generate import generate_tutorial

class TestGeneration(unittest.TestCase):
    def test_generate_python(self):
        result = generate_tutorial("Python", "Functions")
        self.assertIsNotNone(result)