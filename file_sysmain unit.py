import unittest
from unittest.mock import patch
from file_Sysmain import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.initialize_file_system()

    def test_create_file(self):
        with patch('builtins.input', side_effect=['file1.txt', 'rw-', 'file2.txt', 'rw-']):
            self.fs.create_file('file1.txt', 'rw-')
            self.fs.create_file('file2.txt', 'rw-')
        self.assertEqual(len(self.fs.files), 2)

    def test_create_directory(self):
        with patch('builtins.input', side_effect=['dir1', 'rwx', 'dir2', 'rwx']):
            self.fs.create_directory('dir1', 'rwx')
            self.fs.create_directory('dir2', 'rwx')
        self.assertEqual(len(self.fs.files), 2)

    def test_read_file(self):
        self.fs.create_file('file1.txt', 'rw-')
        with patch('builtins.input', return_value='file1.txt'):
            with patch('builtins.print') as mocked_print:
                self.fs.read_file('file1.txt')
        mocked_print.assert_called_with("Content of file 'file1.txt':\n")

    def test_write_file(self):
        self.fs.create_file('file1.txt', 'rw-')
        with patch('builtins.input', side_effect=['file1.txt', 'Hello, world!']):
            with patch('builtins.print') as mocked_print:
                self.fs.write_file('file1.txt', 'Hello, world!')
        mocked_print.assert_called_with("Content written to file 'file1.txt'.")

    def test_delete_file(self):
        self.fs.create_file('file1.txt', 'rw-')
        with patch('builtins.input', return_value='file1.txt'):
            self.fs.delete_file('file1.txt')
        self.assertEqual(len(self.fs.files), 0)

    def test_display_file_permissions(self):
        self.fs.create_file('file1.txt', 'rw-')
        with patch('builtins.input', return_value='file1.txt'):
            with patch('builtins.print') as mocked_print:
                self.fs.display_file_permissions('file1.txt')
        mocked_print.assert_called_with("Permissions of 'file1.txt': rw-")

    def test_set_file_permissions(self):
        self.fs.create_file('file1.txt', 'rw-')
        with patch('builtins.input', side_effect=['file1.txt', 'r-x']):
            with patch('builtins.print') as mocked_print:
                self.fs.set_file_permissions('file1.txt', 'r-x')
        mocked_print.assert_called_with("Permissions of 'file1.txt' set to r-x.")

    def test_list_files(self):
        self.fs.create_file('file1.txt', 'rw-')
        self.fs.create_directory('dir1', 'rwx')
        with patch('builtins.print') as mocked_print:
            self.fs.list_files()
        mocked_print.assert_called_with("Files in the system:\nName: file1.txt, Type: File\nName: dir1, Type: Directory")

if __name__ == '__main__':
    unittest.main()
