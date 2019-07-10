import unittest
from unittest.mock import patch

import pic_factory
import py_test_app
import os


class PicFactoryTestCase(unittest.TestCase):
    filename = "test_unit.jpg"

    def setUp(self):
        if os.path.exists(PicFactoryTestCase.filename):
            os.remove(PicFactoryTestCase.filename)

    @patch('pic_factory.create_empty_one')
    def test_multiprocessing(self, mock_create_empty):

        mock_create_empty.return_value = [1]
        print(dir(mock_create_empty))
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename_template = os.path.join(dir_path, "pics", "test%d.jpeg")

        filenames = py_test_app.get_random_names(100, filename_template)

        log = pic_factory.create_empty(32, 32, filenames)
        print(mock_create_empty.call_count)
        self.assertEqual(len(log), len(filenames))


    def test_create_empty(self):
        self.assertTrue(pic_factory.create_empty(10, 10, PicFactoryTestCase.filename))
        self.assertFalse(pic_factory.create_empty(10, 10, PicFactoryTestCase.filename))


if __name__ == '__main__':
    unittest.main()
