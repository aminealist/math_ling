import unittest
from unittest import TestCase
from os import mkdir as make_dir
from os.path import isfile
from shutil import rmtree as remove_path


def create_directory_with_file(path: str, text: str) -> None:
    try:
        make_dir(path)
    except:
        pass
    output_path = path.strip("\\") + "\\text.txt"
    with open(output_path, "w+") as file_for_test:
        file_for_test.write(text)


class TestDirectoryCreation(TestCase):
    def __init__(self, path: str, text: str):
        super().__init__()
        self.path = path
        self.text = text

    def setUp(self) -> None:
        create_directory_with_file(self.path, self.text)

    def test_file_content(self) -> bool:
        if isfile(self.path):
            with open(self.path) as test_file:
                if len(test_file.read()) > 1:
                    return True
                else:
                    return False
        else:
            return False

    def tearDown(self):
        remove_path(self.path)


if __name__ == '__main__':
    testing_text = "Hi"
    testing_path = r"D:\Apps\Programming\GitHub\math_ling\2023-2024\ООП\Unittest\1\For_test_fiiles"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectoryCreation(testing_path, testing_text))
    unittest.TextTestRunner().run(suite)
    # unittest.main()
