import unittest
import os
from packages import find_class_package

class PackagesTestCase(unittest.TestCase):

    def test_find_class_package(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_json_file = "%s/test_packages.json" % (test_dir)
        class_name = "QPushButton"

        self.assertEqual(find_class_package(class_name, test_json_file), "QtWidgets")

    def test_does_not_find_class_package(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_json_file = "%s/test_packages.json" % (test_dir)
        class_name = "QLineEdit"

        self.assertFalse(find_class_package(class_name, test_json_file))

if __name__ == '__main__':
    unittest.main()
