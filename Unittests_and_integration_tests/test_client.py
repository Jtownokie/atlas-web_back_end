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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Tests public_repos() method """
        mock_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl"}},
        ]
        mock_get_json.return_value = mock_payload
        mock_url = "https://api.github.com/orgs/google/repos"

        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_url
            client = GithubOrgClient("google")

            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            repos = client.public_repos(license="mit")
            self.assertEqual(repos, ["repo1"])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Tests has_license static method """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )
