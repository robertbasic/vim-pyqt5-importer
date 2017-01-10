import unittest
from importer import is_pyqt5_class, is_import_line, is_pyqt5_class_imported

class ImporterTestCase(unittest.TestCase):

    import_lines = [
        'import QDialog',
        'from PyQt5.QtCore import QTimer',
        'import os,sys',
        'from PyQt5.QtWidgets import QLineEdit, QPushButton,QFormLayout',
        'import QLineEdit, QPushButton,QFormLayout'
    ]

    def test_is_pyqt5_class(self):
        class_name = 'QDialog'
        self.assertTrue(is_pyqt5_class(class_name))

    def test_is_not_pyqt5_class(self):
        class_name = "not_a_QClass"
        self.assertFalse(is_pyqt5_class(class_name))

    def test_pyqt_package_is_not_pyqt5_class(self):
        class_name = 'QtWidgets'
        self.assertFalse(is_pyqt5_class(class_name))

    def test_import_line(self):
        line = 'import os, sys'
        self.assertTrue(is_import_line(line))

    def test_from_import_line(self):
        line = 'from re import match'
        self.assertTrue(is_import_line(line))

    def test_not_import_line(self):
        line = 'this is not an import line'
        self.assertFalse(is_import_line(line))

    def test_not_from_import_line(self):
        line = 'this is not a from import line'
        self.assertFalse(is_import_line(line))

    def test_imported_on_import_line(self):
        class_name = "QDialog"
        self.assertTrue(is_pyqt5_class_imported(class_name, self.import_lines))

    def test_imported_on_from_import_line(self):
        class_name = 'QTimer'
        self.assertTrue(is_pyqt5_class_imported(class_name, self.import_lines))

    def test_imported_on_line_with_multiple_from_imports(self):
        class_name = 'QPushButton'
        self.assertTrue(is_pyqt5_class_imported(class_name, self.import_lines))

    def test_imported_on_line_with_multiple_imports(self):
        class_name = 'QPushButton'
        self.assertTrue(is_pyqt5_class_imported(class_name, self.import_lines))

    def test_not_imported(self):
        class_name = 'QApplication'
        self.assertFalse(is_pyqt5_class_imported(class_name, self.import_lines))

    def test_not_imported_lookalike(self):
        class_name = 'QDial'
        self.assertFalse(is_pyqt5_class_imported(class_name, self.import_lines))

if __name__ == '__main__':
    unittest.main()
