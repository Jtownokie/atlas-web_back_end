#!/usr/bin/env python3
""" This module contains testing classes for client.py """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ This class tests the GithubOrgClient class """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """ Tests the org property """
        client = GithubOrgClient(org_name)
        org_result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(org_result, {'key': 'value'})
