import unittest

from hello_world import HelloWorld


class TestHelloWorld(unittest.TestCase):

    def test_txt_to_say_hello_with_default_value(self):

        # prepare
        hello_world_txt = HelloWorld.txt_to_say_hello()
        expected_txt = "Hello Armando"

        # Verification
        self.assertEqual(hello_world_txt, expected_txt)

    def test_txt_to_say_hello_with_informed_value(self):

        # prepare
        hello_world_txt = HelloWorld.txt_to_say_hello('World')
        expected_txt = "Hello World"

        # Verification
        self.assertEqual(hello_world_txt, expected_txt)