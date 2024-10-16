#!/usr/bin/env python

import unittest
import subprocess
import os


def execute(cwd, makedown, *commands):
    result = subprocess.run(
        [makedown] + list(commands),
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    return result.returncode, result.stdout, result.stderr


def execute_in_test(*commands):
    return execute(".", "../makedown.py", *commands)


def execute_in_help(*commands):
    return execute("./help", "../../makedown.py", *commands)


class Test(unittest.TestCase):

    def test_hello(self):
        status, stdout, stderr = execute_in_test("hello")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "hello, world\n")
        self.assertEqual(stderr, "")

    def test_hashbang(self):
        status, stdout, stderr = execute_in_test("hashbang")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, "hello, world\n")
        self.assertEqual(stderr, "")

    def test_help(self):
        status, stdout, stderr = execute_in_help("--help")
        self.assertEqual(status, 0)
        self.assertEqual(stdout, f"""
{os.getcwd()}/help/help.md

$ makedown uno     # Uno
$ makedown duo     # Duo
$ makedown tre

""")
        self.assertEqual(stderr, "")


if __name__ == "__main__":
    unittest.main()
