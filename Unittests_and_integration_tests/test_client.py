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
