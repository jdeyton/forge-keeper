# coding: utf-8
"""
This module tests some of the main script functionality.
"""
import pathlib
import unittest

from digital.forge.drone.__main__ import _load_config


class TestMain(unittest.TestCase):
    """
    Unit tests for the program entrypoint.
    """

    def setUp(self):
        current_dir = pathlib.Path(__file__).parent.absolute()
        self.cfg = current_dir.joinpath('py-drone.json')
        self.cfg_with_url = current_dir.joinpath('py-drone-url.json')
        self.bad_cfg = current_dir.joinpath('py-drone-bad.json')

    def test_load_config(self):
        """
        Tests the config file is loaded properly.
        """
        expected = {
            "port": "/dev/ttyS0",
            "rate": 9600,
            "drone": "f26ba799-f4a8-4968-b44b-6a29421695c5",
            "archives": [
                "6adb613e-9642-4264-af53-cec6d96dfdae",
                "b5280bf4-786e-4769-f2ce-88e1d24344de"
            ]
        }
        actual = _load_config(self.cfg)
        self.assertEqual(expected, actual)

        expected['url'] = "https://foobar:12345"
        actual = _load_config(self.cfg_with_url)
        self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            _load_config(self.bad_cfg)


if __name__ == "__main__":
    unittest.main()
