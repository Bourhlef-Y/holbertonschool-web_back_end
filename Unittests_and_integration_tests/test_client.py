#!/usr/bin/env python3
"""Module de tests unitaires pour la classe GithubOrgClient"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Classe de test pour GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Dict) -> None:
        """Test que la méthode org retourne la valeur correcte"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """Test que la propriété _public_repos_url retourne la bonne URL"""
        known_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        with patch(
            'client.GithubOrgClient.org',
            new_callable=property,
            return_value=known_payload
        ):
            test_client = GithubOrgClient("testorg")
            self.assertEqual(
                test_client._public_repos_url,
                known_payload["repos_url"]
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test que public_repos retourne la liste attendue de repos"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = test_payload
        test_url = "https://api.github.com/orgs/test/repos"

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=property,
            return_value=test_url
        ):
            test_client = GithubOrgClient("test")
            result = test_client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(test_url)
