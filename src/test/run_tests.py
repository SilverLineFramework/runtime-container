import unittest
import os

loader = unittest.TestLoader()
start_dir = os.path.abspath(os.path.dirname(__file__))
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
