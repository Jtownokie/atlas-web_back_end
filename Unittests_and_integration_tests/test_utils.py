#!/usr/bin/env python3
""" This module contains the TestAccessNestedMap Class """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ This class tests the access_nested_map() function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests basic functionality """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Tests exception raising """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(expected))


class TestGetJson(unittest.TestCase):
    """ This class tests the get_json() function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Tests basic functionality """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ This class tests the memoize decorator """

    def test_memoize(self):
        """ Tests the memoized wrapper """
        class TestClass:
            """ For testing memoize decorator"""
            def a_method(self):
                """ Test method """
                return 42

            @memoize
            def a_property(self):
                """ Property returned by memoize"""
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            test_class = TestClass()

            result1 = test_class.a_property
            result2 = test_class.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()
