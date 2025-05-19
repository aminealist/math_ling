import unittest
from unittest import TestCase
from os import mkdir as make_dir
from os.path import isfile
from shutil import rmtree as remove_path


def create_directory_with_file(path: str, text: str) -> str:
    try:
        make_dir(path)
    except FileExistsError:
        pass
    output_path = path.strip("\\") + "\\text.txt"
    with open(output_path, "w+") as file_for_test:
        file_for_test.write(text)
    return output_path


class TestDirectoryCreation(TestCase):

    def setUp(self) -> None:
        self.testing_path = r"D:\Apps\Programming\GitHub\math_ling\2023-2024\ООП\Unittest\1\For_test_fiiles"
        self.testing_text = "txt"
        self.testing_path = create_directory_with_file(self.testing_path, self.testing_text)

    def test_file_content(self):
        if isfile(self.testing_path):
            with open(self.testing_path) as test_file:
                self.assertTrue(len(test_file.read()) > 0)
        else:
            self.assertTrue(False)

    def tearDown(self):
        remove_path(self.testing_path.replace("\\text.txt", ""))


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestDirectoryCreation)
    unittest.TextTestRunner().run(suite)
