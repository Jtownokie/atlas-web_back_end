#!/usr/bin/env python3
""" This module contains testing classes for client.py """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock

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

    def test_public_repos_url(self):
        """ Tests public_repos_url property """
        expected_url = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }

        with patch.object(
                GithubOrgClient,
                'org',
                PropertyMock(return_value={'repos_url': expected_url})):

            client = GithubOrgClient('google')

            result = client._public_repos_url

            self.assertEqual(result, expected_url)
