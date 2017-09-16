
import unittest

# Get all files finished with Test.py
test_files = ["logo_test",
              "logobot_test",
              "progressbar_test"]

# Create the suites
suites = [unittest.defaultTestLoader.loadTestsFromName(
    file_name) for file_name in test_files]

# Create and run the suite
suite = unittest.TestSuite(suites)
unittest.TextTestRunner().run(suite)
