#!/usr/bin/env python

import unittest
import subprocess


def execute(*command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


class Test(unittest.TestCase):

    def test_hello(self):
        status, stdout, stderr = execute("m", "hello")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "hello, world\n")


if __name__ == "__main__":
    unittest.main()
