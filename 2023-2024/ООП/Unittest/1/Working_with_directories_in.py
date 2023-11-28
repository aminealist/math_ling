from unittest import TestCase
from os import mkdir as make_dir
from os.path import isfile
from shutil import rmtree as remove_path


def create_directory_with_file(path: str, text: str) -> None:
    make_dir(path)
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

    def tearDown(self):
        remove_path(self.path)

    def test_file_content(self):
        if isfile(self.path):
            with open(self.path) as test_file:
                if len(test_file.read()) > 1:
                    return True
                else:
                    return False
        else:
            return False
