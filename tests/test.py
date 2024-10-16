#!/usr/bin/env python

import unittest
import subprocess


def execute(*command):
    result = subprocess.run(
        ["../makedown.py"] + list(command), capture_output=True, text=True
    )
    return result.returncode, result.stdout, result.stderr


class Test(unittest.TestCase):

    def test_hello(self):
        status, stdout, _stderr = execute("hello")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "hello, world\n")

    def test_hashbang(self):
        status, stdout, _stderr = execute("hashbang")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "hello, world\n")


if __name__ == "__main__":
    unittest.main()
